---
layout: post
title: "On coding defensively"
date: 2012-02-17 18:57:25 +0000
categories:
  - code
  - ruby
  - craftsmanship

---

When writing code that will be used by others (and we do that 100% of the time, even if the other user is ourselves in a few weeks time), there's a tricky balance to strike between being generous to the users of our code, and ensuring that they get the information they want to ensure they're calling our code correctly. There are two coding maxims: "Be generous on input, and strict on output", and "fail fast", which we need to hold in tension. This post explores the trade-offs between the two.

## "Be generous on input, and strict on output"

This is another way of saying *code defensively:* we should allow the user to use our code a number of different ways, yet be careful about what we return to them to ensure they can't be easily confused.

For example, consider this method:

{% highlight ruby %}

    def calculate_total(products)
      total = 0
      products.each do |product|
        total += product.price
      end
      return total
    end

    calculate_total([product1, product2])

{% endhighlight %}

If we accept a array as an argument, we could code defensively and allow a single product to be passed as well:

{% highlight ruby %}

    def calculate_total(products)
      products = [products] unless.products.respond_to?(:each)
      total = 0
      products.each do |product|
        total += product.price
      end
      return total
    end

    calculate_total(product) # also works now

{% endhighlight %}

This is a nice feature and potentially allows our code to be used more flexibly.

Let's take this further. What happens when our user decides to pass in an invalid value, such as a string? Should we code defensively for that situation?

{% highlight ruby %}

    def calculate_total(products)
      return 0 if product.is_a?(String)
      products = [products] unless.products.respond_to?(:each)
      total = 0
      products.each do |product|
        total += product.price
      end
      return total
    end

    calculate_total("product") # return 0

{% endhighlight %}

In this case, we could argue our code is being defensive: it avoided the crash that would have happened when we tried to call the non-existent `price` method on the passed in string. Is this desirable?

## "If we're going to fail, we should fail quickly."

The programmer using our code probably made a mistake here. If we fail immediately, it's very easy for them to see where the error is. If we accept pretty much anything, and return '0' (or much worse, '-999' or some other abomination) we're just going to get incorrect prices: we're going to hide and propagate the error down the call stack and make it much harder to debug.

This is a tricky balance and it depends on the situation, but in general I think these principles are helpful to deciding what to do:

* *Fail if we cannot be strict with our output.* Coding defensively has two sides: generous with input, but also strict with output. If the output is changed by the way we recieve our argument, we're not being specific enough. In the above example, we're effectively giving a string a price of zero, which is extra behaviour we probably don't want. Likewise, make sure that if there's no way we can return a sensible result, then we should not accept the argument passed and fail instead.


* *Is our method doing too much?* In the case of the above method our user might be wanting to pass the name of the product as a string, and look up the product to work out the price. We could support that, but this will encourage duplication: if we persist with keeping methods that do "A and B", we'll find over time we code will spring up additional methods which do "A" and "B" separately. Our method is now too complex and needs to be split into two.

* *Be generous with types.* We have some advantages working in a weakly typed language such as Ruby. Use the power of Duck Typing: don't check if objects are certain types: check if they respond to the methods that we need to call on them.

* *Be generous at the edges of our code.* Being generous with private APIs and methods only used by ourselves in constrained circumstances is a waste of time: we should just ensure we're calling our own code correctly.

* *When we fail, we should fail hard. Really hard.* In its laudable determination to follow the [Principle of Least Astonishment](http://en.wikipedia.org/wiki/Principle_of_least_astonishment), Ruby has a weakness for over-generosity. It tends to return nil when it encounters an error in cases where in my opinion it should throw an exception. Programmers don't always check for the nils they receive correctly, which means they get passed around our codebase, eventually causing a crash when we least expect it. We should not return nil: that's not being specific enough with our outputs. We should throw an exception or terminate the program if we really need to get their attention.

What do you think? Do you tend to learn more towards coding defensively, or failing early?

(Thanks to [Alex Tomlins](http://www.unboxedconsulting.com/people/alex-tomlins) at Unboxed for the conversation that led to this post.)
