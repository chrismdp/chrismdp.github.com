---
layout: post
title: A fresh take on DCI with C++ (with example)
date: 2012-04-16 12:20:48.000000000 +01:00
categories:
- code
- c++
- dci
- sol trader
redirect_from:
- "/2012/04/a-fresh-take-on-dci-with-c-plus-plus"
- "/2012/04/a-fresh-take-on-dci-with-c-plus-plus/"
---
{% include callout.html color="#d9edf7" text="If you'd like to purchase Sol Trader you can now do so at soltrader.net!" %}

I've been reading quite a lot about [DCI](http://en.wikipedia.org/wiki/Data,_Context,_and_Interaction) recently, both from the point of view of the [original paper](http://heim.ifi.uio.no/~trygver/2009/commonsense.pdf) published in 2009 and various other sources on the Internet. There's been a discussion around beginning to use it with Ruby on Rails, but at the moment I'm more interested in how to apply the principles to [Sol Trader](http://soltrader.net) in C++.

## What is DCI?

DCI stands for Data, Context and Interaction. It places behaviour at the forefront of your design by setting the stage for a particular use-case through Context objects, and having all the behaviour exist in Role objects seperate to your basic persisted Data objects.  For example, you might have an `Account` "Data" class, which just contains the data representation and basic methods such as `IncrementBalance` and `DecrementBalance`. You'd then have a use-case `TransferMoney` with two roles: `SourceAccount` and `DestinationAccount`. These roles would be played by `Account` objects, but the behaviour of the objects would depend on the roles they play in the use case. The behaviour of the system is therefore captured in one place: it's in the interaction between the roles within a particular use case context, rather than being spread all over different data classes.

This design paradigm is very interesting. We've known for a while that if you mix persistence and behaviour you'll get into somewhat of a mess with your code design after a while. What's new is that whilst we avoid mixing persistence and behaviour, we still often mix *data* and behaviour: that is, we put code describing what the object *does* in the same class as the code which describes what it *is*. This is a subtle violation of the [Single Responsibility Principle](http://en.wikipedia.org/wiki/Single_responsibility_principle); I hadn't noticed this violation before reading about DCI.

The  proponents of DCI advocate injecting methods describing the Role in any given use case directly into the data object when setting the use case up. This is easy in a language like Smalltalk or Ruby, but is considerably harder in C++. What approach should we take in C++ with Roles? Is this the right approach at all?

## The templating method for injection of role behaviour

One way around this it to use templates: subclass your Data objects with a templated class which includes the roles you want the object to play. For example, to take our account example earlier, we could have:

{% highlight cpp %}

    class DestinationAccount {
    public:
      virtual ~DestinationAccount() {}

      virtual void DepositMoney(int amount) = 0;
    };

    template <class DataClass> class DestinationAccountCollaborator :
      public DataClass, public DestinationAccount
    {
      DestinationAccountCollaborator(int id) : DataClass(id) {}
      virtual void DepositMoney(int amount) {
        DataClass::IncrementBalance(amount);
      };
    };
{% endhighlight %}

We would also have a similar set up for `SourceAccount`. This way we can pass a pointer to the `DestinationAccount` interface to our Context to set up the use case:

{% highlight cpp %}

    class TransferMoneyContext {
      DestinationAccount& _dest;
      SourceAccount& _source;
    public:
      TransferMoneyContext(DestinationAccount& dest,
        SourceAccount& source) : _dest(dest), _source(source) {}
    };

    ...

    DestinationAccountCollaborator<Account> dest(accountNumberId);
    SourceAccountCollaborator<Account> source(sourceAccountId);
    TransferMoneyContext context(dest, source);

{% endhighlight %}

The DataClass would then instantiate itself from the account id and the role contains the description of the behaviour.

In practice however, I found this extremely unwieldy. My data classes all had slightly different interfaces, especially as many of them served as API endpoints. The templates ended up being 'clever' code - they saved very little space at the expense of a good amount of readability. The whole point of DCI is to try and capture behaviour in the Role classes to improve readability and create a cleaner design, and this approach wasn't serving that purpose. There might be better ways of doing it, and I'd be grateful if you'd let me know if you know of a better approach.

## The composition method for roles

The DCI literature teaches us to inject behaviour into the Data objects, to prevent [self schizophrenia](http://en.wikipedia.org/wiki/Schizophrenia_(object-oriented_programming)). For complex use cases, I can see that it would be useful for roles to have access to the methods defined on data objects: but perhaps it would be better to have simpler use cases and have roles only be defined in terms of other roles? In that instance, the roles can simply compose the data objects and expose whichever methods seem appropriate to the other roles in the use case.

## A worked example

As an example, consider this use case that came up recently in Sol Trader: I have a `MarketListing` object which contains a particlar `Good` (such as Grain, or Water) available at a certain price. The GUI displays a list of these `MarketListing` objects in a table format. Whenever a change was detected to any of the listings I would clear the table and reconstruct the gui elements, rather than updating the original elements.

This worked fine, until I realised that the GUI library I'm using did not expect GUI elements to be deleted and recreated under the mouse cursor, and wouldn't fire "click" events correctly at the newly created elements.

Therefore I needed a way to synchronise the GUI table with the `MarketListings` somehow, add new listings that have appeared, update the text of any existing listings, and remove old elements that refer to listings that no longer exist in the set. I decided to try to implement this using DCI, using the composition approach to roles I've discussed.

The use case is quite simple:

* For each source data structure:
* Does it already exist? If so, update the elements
* If not, create new elements
* Remove any elements that weren't checked this run

After writing some tests, I started with the following context object:

{% highlight cpp %}

    class RowUpdater {
      role::TableSource& _source;
      role::TableRepresentation& _table;
      int _timestamp;
    public:
      RowUpdater(role::TableSource& source, role::TableRepresentation& table) : _source(source), _table(table), _timestamp(0) {}

      void execute();
      void checkRow(void const* rowIdentifier);
    };
{% endhighlight %}

Note the two role objects, `TableSource` and `TableRepresentation`. I'll come back to those later.

`execute()` and `checkRow()` were defined like this:

{% highlight cpp %}

    void RowUpdater::execute() {
      _timestamp = SDL_GetTicks(); // Could be any unique number
      _source.enumerateRows(boost::bind(&RowUpdater::checkRow, this, _1));
      _table.removeUncheckedRows(_timestamp);
    }

    void RowUpdater::checkRow(void const* rowIdentifier) {
      if (_table.rowExists(rowIdentifier))
        _table.updateRowFor(rowIdentifier, _source, _timestamp);
      else
        _table.addRowFor(rowIdentifier, _source, _timestamp);
    }

{% endhighlight %}

(In C++ you can't easily enumerate, so I used boost::bind to call `checkRow()` on each row in the `_source` object.)

This code is beautifully simple, and very close to the pseudo code I wrote earlier.

### Implementing TableRepresentation

What does this context require of the roles? Here are the methods needed for `TableRepresentation`, taken directly from the context above:

{% highlight cpp %}

    bool rowExists(void const* id);
    void updateRowFor(void const* id, TableSource const& source, int timestamp);
    void addRowFor(void const* id, TableSource const& source, int timestamp);
    void removeUncheckedRows(int timestamp);

{% endhighlight %}

This object is created with the data it needs to manipulate: in this case a `Rocket::Core::Element` object. When it needs to update elements, it is passed a `TableSource` role to give it the relevent data. Here's some of the code for the `addRowFor()` method:

{% highlight cpp %}

    void TableRepresentation::addRowFor(void const* id, TableSource const& source, int timestamp) {
      Rocket::Core::Element* entry = _element->GetOwnerDocument()->CreateElement("li");
      entry->SetAttribute("good", (void*)id);
      std::vector<std::string> columnList;
      source.fetchColumnList(columnList);
      std::vector<std::string>::iterator it = columnList.begin();
      for(; it != columnList.end(); it++) {
        ChildContentTag(entry, "div", it->c_str(), source.rowFor(it->c_str(), id).c_str());
      }
      _element->AppendChild(entry);
      entry->RemoveReference();
      entry->SetAttribute("updated_at", timestamp);
    }

{% endhighlight %}

There's a lot of noise here, but note the use of `source`. The code creates a new `li` element, gets the column list from the source and then asks the source for the string data for a particular row using `rowFor()`. The roles are interacting to provide the behaviour of the use case.

### Implementing TableSource

`TableSource` needed to be an interface in the end to manage both viewing a series of `MarketListings` and also a player `Inventory`. Here are the methods:

{% highlight cpp %}

    virtual void enumerateRows(boost::function<void(const void*)> action) = 0;
    virtual std::string rowFor(std::string const& key, void const* id) const = 0;
    virtual void fetchColumnList(std::vector<std::string>& list) const = 0;

{% endhighlight %}

For a `MarketListing`, here's the implementation of the key methods that the `TableRepresentation` needs:

{% highlight cpp %}

    void CommodityMarketTableSource::fetchColumnList(std::vector<std::string>& list) const {
      list.push_back("name");
      list.push_back("price");
      list.push_back("quantity");
    }

    std::string CommodityMarketTableSource::rowFor(std::string const& key, void const* id) const {
      MarketListing const* listing = _market.listings()[(Good const*)id];
      std::stringstream stream;
      if (key == "name")
        return listing->name();
      if (key == "price") {
        stream << "$";
        stream << listing->price().amount();
        return stream.str();
      }
      if (key == "quantity") {
        stream << listing->amountAtThisPrice();
        return stream.str();
      }
    }
{% endhighlight %}

The player `Inventory` table source code is very similar.

### Tying it together

How do I use this thing? Inside my controller for updating the GUI window, I do the following:


{% highlight cpp %}

    void MarketController::syncInventory() {
      Rocket::Core::Element* entries = _planetWindow->GetElementById("inventory")->GetLastChild();

      gui::role::TableRepresentation tableRole(entries);
      gui::role::InventoryTableSource sourceRole(_inventory);
      gui::RowUpdater(sourceRole, tableRole).execute();
    }

    void MarketController::syncMarketListings() {
      Rocket::Core::Element* entries = _planetWindow->GetElementById("market")->GetLastChild();

      role::TableRepresentation tableRole(entries);
      role::CommodityMarketTableSource sourceRole(_market);
      gui::RowUpdater(sourceRole, tableRole).execute();
    }

{% endhighlight %}

In each case the `TableRepresentation` is the same, with a different target element, and the source is different depending on what I want to show for that table.

## In conclusion

I could have simply used a list of `MarketListing` objects instead of my `TableSource`, and manipulated the `Element` objects in the GUI directly. That's what I did at first, but this approach gives me a number of advantages:

* The code for enumerating rows, and exposing certain data to to the GUI is kept out of `MarketListing`, which is great: it only makes sense in this Context which is exactly what a role is for.
* The actual guts of the synchronisation code is kept in the Context. I'm not sure this is the best place, but it's great to have it in one place.
* It was trivial to add a `role::InventoryDataSource` object: in another 30 minutes or so I had TDDed out the display of inventories of goods using the same Context and slightly different roles.
* I could potentially replace the `TableRepresentation` with anything which we need to sync lists of tabular data with.

I tested this using some real `CommodityMarket` objects, which contain `MarketListing` objects: I poked new goods into them and checked the elements were being created and removed successfully.

Here's a screenshot of the market at work:

![Sol markets](/assets/img/sol-trader-market-1.png)

In summary, I'm very pleased with how this turned out. There is a bit more code than just hard wiring it, but all my behaviour is in one place, and I've not loaded my market and goods classes with yet more functionality. I'm now looking for other use cases to implement using a similar method, as I move on to building a realistic (as opposed to random) economy.

How do you like my approach to DCI? Have I missed something profound, or how could I improve my approach?
