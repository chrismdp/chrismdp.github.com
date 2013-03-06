---
layout: post
title: "BDD without tools: testing shell script"
date: 2013-03-06 08:49:20 +0000
categories:
  - bdd
  - shell script
  - code

---

Doing BDD without tools like Cucumber and RSpec [sounds fine in theory](http://chrismdp.com/2013/01/bdd-is-not-cucumber), but is it feasible in practice?

On one [one of the projects](http://github.com/alphagov/redirector) I'm working on currently, we're handling tens of thousands of existing UK government URLs from old websites, ensuring they redirect correctly to the right place on [GOV.UK](http://gov.uk/government). This involves a lot of bash scripting, and using a combination of unix tools and our own small tools to process large amounts of CSV data.

The principles of BDD work here just as much as they do on a comfortable Ruby project using Cucumber and RSpec, so let's look at how we might apply them to this problem.

## Acceptance testing

In a simplified example case, we need to take an input CSV file, clean the urls contained with it, substitute one type of URL for another, and write it out. The inputs and output formats are clear and well defined, so our tests can start with a standard set of output files.

{% highlight bash %}

    #!/bin/sh

    # Feature: Gettings url mappings ready for redirection
    # Scenario: Ensure urls are sanitized and remapped

    # Given a mapping of /new-url to /real-new-url
    cat > /tmp/remap <<!
    Old Url,New Url,Status
    http://gov.uk/new-url,http://gov.uk/real-new-url,301
    !

    # And a mapping from old to new which needs sanitization
    cat > /tmp/input <<!
    Old Url,New Url,Status
    http://old.gov.UK/,https://gov.uk/new-url,301
    !

    # When I run the readying process
    ./run-readying-process.sh < /tmp/input /tmp/remap > /tmp/output

    # Then the output should be sanitized and remapped
    diff /tmp/output - <<!
    Old Url,New Url,Status
    http://old.gov.uk,https://gov.uk/real-url,301
    !

    [ $? -ne 0 ] && { echo "$0: FAIL" ; exit 1; }

    rm -f /tmp/{input,remap,output}

    echo "$0: OK"

{% endhighlight %}

(I'm grateful to [Paul Downey](http://blog.whatfettle.com/) for coming up with the original shell script testing pattern shown here.)

This script will return a success error code if everything works fine, and a failure error code if there was a difference between the expected and the actual output. This means we can run the script in a build server such as [Jenkins](http://jenkins-ci.org) and everything will work as expected.

Now we have our outer layer of acceptance testing, let's see how we can apply this idiom to our inner layer of unit tests.

## Unit testing

For unit tests we can test the individual tools, rather than testing the whole pipeline process:

{% highlight bash %}

    #!/bin/sh

    # test: Sanitize
    # Lower case for urls
    # Remove trailing slashes
    # Remove trailing query strings

    cat > /tmp/input <<!
    Old Url,New Url,Status
    http://old.gov.UK,https://gov.uk/new-url,301
    http://old.gov.uk/,https://gov.uk/new-url,301
    http://old.gov.uk/?should-be-removed,https://gov.uk/new-url,301
    !

    ./tools/sanitize < /tmp/input > /tmp/output

    diff /tmp/output - <<!
    Old Url,New Url,Status
    http://old.gov.uk,https://gov.uk/new-url,301
    http://old.gov.uk,https://gov.uk/new-url,301
    http://old.gov.uk,https://gov.uk/new-url,301
    !

    [ $? -ne 0 ] && { echo "$0: FAIL" ; exit 1; }

    rm -f /tmp/{input,output}

    echo "$0: OK"

{% endhighlight %}

We're testing a greater level of detail here by checking three different things: that the case is always lower case, that trailing slashes are removed and that query strings are removed.

## The BDD cycle, intact

We can just as easily use the BDD cycle in this context. We can start with the first type of test: an outward facing acceptance test for our customer's benefit which describes the goal we're trying to achieve with our software. As always, it's important to [to talk to our customer during the process](http://chrismdp.com/2012/11/the-integration-testing-trap/).

Once we have that, we run it and watch it fail. Then we write an individual unit test, perhaps like the one above, which tests an individual component of the pipeline.

We don't need much more than this: all we really need to use the BDD cycle is some way of checking the whole pipeline, and some way of checking fine-grained behaviour.

## Customer readable documentation

One way of printing human readable steps would be to use a command like this:

{% highlight bash %}

    cat tests/features/*.sh | grep -E "^# (Feature|Scenario|And|Given|When|Then)"

{% endhighlight %}

This will print out any comment which contains a word we might use to describe the scenario that we're running.

## You don't _need_ BDD tools

There's nothing to stop you going through this process using Cucumber and Aruba to drive tests being run on the command line. It would also be reasonably easy to build a minature framework around this to help us with pretty printing and better errors.

The tests we have above will cause us to tend to writing unit tests around small standalone tools doing one thing well, which is a [old and proven philosophy of systems architecture](http://en.wikipedia.org/wiki/Unix_philosophy).

However, I don't think I'd necessarily persist with this approach long term. We have an earlier form of this approach running on the project now, but we may well switch to a more standard testing library. The point is to that BDD can easly be applied without the trappings of tools: we don't need to use BDD tools to use BDD principles.

Are you doing anything similar? How are you using BDD principles without the "standard" toolset?

<div class='alert alert-info'>
  <p>If you like what you read, and you'd like to learn more, a quick reminder that we are running <a href='http://bddkickstart.com'>BDD Kickstart</a> in Edinburgh <a href='http://bddkickstart.com/dates#edinburgh'>this coming week</a>: there are only a few tickets left so be quick!
  </p>
</div>
