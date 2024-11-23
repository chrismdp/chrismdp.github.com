---
layout: post
title: 'How I''m testing iPhone apps: part 2'
date: 2011-12-06 16:02:54.000000000 +00:00
categories:
- code
- ios
- tdd
- bdd
redirect_from:
- "/2011/12/how-im-testing-iphone-apps-part-2"
- "/2011/12/how-im-testing-iphone-apps-part-2/"
---
<p><i>I've recently been doing some iOS development, and working out the best way to test-drive the development of iOS apps was high on my priority list. I know that the automated testing of iOS applications is still not widely practiced and isn't well documented, so I decided to write a series of posts to start to rectify that. You may wish to read <a href="/2011/12/how-im-testing-iphone-apps-part-1">part 1</a> first.</i></p>

## Kiwi

We were looking for a testing framework which supported iOS's asynchronous programming model and [Kiwi](https://github.com/allending/Kiwi) answered the call. It has a great syntax, [comprehensive set up assistance](https://github.com/allending/Kiwi/wiki/Guide:-Up-and-Running-with-Kiwi), asynchronous support and built in mocking. I'd highly recommend you check it out: the syntax helps me to think in the right way and it has pretty much all the features we needed.

Kiwi's block syntax looks like this:

{% highlight objectivec %}
describe(@"Team", ^{
    context(@"when newly created", ^{
        it(@"should have a name", ^{
            id team = [Team team];
            [[team.name should] equal:@"Black Hawks"];
        });
    });
});
{% endhighlight %}

Much better than the old fashioned xUnit style of testing, in my opinion. You might hate it, of course. You can use Kiwi's features [without having to use the block syntax](https://github.com/allending/Kiwi/issues/73) if you want.

## Objective-C's delegate model

Many of the Apple core libraries use a delegate pattern for handling callbacks from a class. This is similar to Java's interfaces, and superficially similar to blocks in Ruby and anonymous functions in Javascript.

As an example, let's take CoreLocation. When wanting to find the location of a phone, you create a new `CoreLocationManager` and call `startUpdatingLocation` on it:

{% highlight objectivec %}
CLLocationManager *manager = [[CLLocationManager alloc] init];
[manager startUpdatingLocation];
{% endhighlight %}

This call returns immediately: so how do you execute code when the location is found? You use a delegate: an object with responds to the `locationManager: didUpdateToLocation: fromLocation` method:

{% highlight objectivec %}
-(void)locationManager:(CLLocationManager *)manager didUpdateToLocation:(CLLocation *)newLocation fromLocation:(CLLocation *)oldLocation
{
  NSLog("$@ I AM IN YOU", newLocation);
  foundLocation = YES;
}
{% endhighlight %}

Then you set this object to be the CLLocationManager's delegate before calling `startUpdatingLocation`. Often you set the delegate to `self` and define the delegate method on the calling object.

{% highlight objectivec %}
CLLocationManager *manager = [[CLLocationManager alloc] init];
manager.delegate = self;
[manager startUpdatingLocation];
{% endhighlight %}

There's more about this model in [this article from Apple](http://developer.apple.com/library/IOs/#documentation/iPhone/Conceptual/iPhone101/Articles/02_DesignPatterns.html).

## Testing delegates

This is tricky to test, because we can't simply do this:

{% highlight objectivec %}
it("should call the delegate when ready", ^{
  [testObject startUpdatingLocation];
  [[testObject.foundLocation should] equal:theValue(YES)];
});
{% endhighlight %}

The test will call `startUpdatingLocation`, and then immediately check the `foundLocation` property to see whether it's been set. It won't have been, because the delegate won't have been called yet.

How were we to stub endpoints such as the location system for for our app? We found two ways of doing this, with varying effectiveness:

* Using Objective-C categories to redefine class methods
* Using a Kiwi stub to inject a derived class which mocks out key methods

Next post, I'll dive into some detail on both of these methods and show some of the pros and cons of each.

<i>How are you testing iPhone apps? Do chime in throughout the series with suggestions and comments, and I'll edit the posts as appropriate.</i>

