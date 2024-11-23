---
layout: post
title: 'Cucumber: keeping the build passing'
date: 2012-12-11 08:40:48.000000000 +00:00
categories:
- cucumber
- bdd
- testing
- process
- code
redirect_from:
- "/2012/12/cucumber-keeping-the-build-passing"
- "/2012/12/cucumber-keeping-the-build-passing/"
---
One benefit we have when using BDD techniques properly is that we always have a failing acceptance test to guide us. The idea is that we write a failing feature, then make it pass by iterating using the standard red-green-refactor procedure. However, this is a challenge as well, as our acceptance test is going to be failing for most of the time that we're working on the feature, and we have to decide how to handle that.

This is a problem because it's good to make small commits into source control, sometimes only representing a few minutes work. This helps future source code readers to see the train of thought I went through when working on the feature, and allows us to use tools such as `git bisect` to discover which commit might have broken something.

However, if the tests don't pass for every commit, then our ability to use git bisect and other similar tools is more limited. If we don't have a clean state from which to test, we can't tell whether or not a build is broken for a reason that's expected or unexpected.

What do we do at this point? Do we continue to make small commits to our codebase, knowing that we are going to be checking in code that breaks the build each time? Is it more important to have a detailed history of the change, or a clean history that always passes?

There are a few options here:

## Check in the feature file at the end

I like this option the least, as it's unclear what's being worked on, and our source control history doesn't show the code being driven out by the acceptance tests.

## Go back and edit our commits later

Assuming we have a source control system that allows us to do this, we can always rewrite our history and insert the feature at the beginning of the change. Some have success with this, but it strikes me as dangerous and risky: there's always a danger we might rewrite pushed history.

## git squash

The squash command allows us to combine a number of commits into one when we've finished working on a feature. This will ensure that the one large commit passes, but then we've lost our "working": our history doesn't reflect our thought process.

## Cucumber WIP

Cucumber can be run in a special mode called `wip` mode. When we run `cucumber --wip`, the tool will fail *if any scenarios pass* (you might want to read that bit again.)

Normally we run cucumber in this way in conjunction with the `--tags` option, which ensures that only a set of scenarios run. Therefore, this command:

{% highlight bash %}

    $ cucumber --wip --tags @wip

{% endhighlight %}

...will ensure that we only run the scenarios tagged `@wip`, failing if any pass, and succeeding if they fail.

We can also run cucumber excluding certain tags, too:

{% highlight bash %}

    $ cucumber --tags ~@wip

{% endhighlight %}

This command will ensure that cucumber skips all of the `@wip` scenarios for a normal run, which means that all the features should pass.

Armed with these tools, we can come up with a workflow which will allow us to keep our source code history, but also to ensure that our changes don't break the build.

## How to use Cucumber WIP in practice

Here's an example of how this process might work:

* *Pair A start work on a new feature.* They check out the code, switch to a new feature branch, and write a failing feature, which they tag `@wip`. They work on this feature, checking in liberally whenever their unit tests pass.

* *Pair A push their code to their branch.* They can push the code any time they like, as they're pushing to a branch. Should anyone check out and start working on their branch, all the tests will continue to pass: the tests are run with a similar command to the following:

* *Pair B start another feature.* They use the same process as above.

{% highlight bash %}

    $ run_unit_tests && cucumber --tags ~@wip && cucumber --wip --tags @wip

{% endhighlight %}

* *When Pair A's feature is finished, they remove the @wip tag.* Eventually the feature starts passing, and therefore the build fails: `@wip` scenarios aren't supposed to pass. Removing the `@wip` tag from the feature ensures the build passes again.

* *Pair A push their code to master.* This can be a straight merge, or if no-one else is working off the feature branch, (and we're using something like git to do source control) we can rebase it and push it to master as a fast-forward.

* *Later, Pair C debugs an old commit.* Pair C have found a bug, and they check out one of Pair A's interim commits to find out if the issue presents itself in that commit. They run the build and it passes - the `@wip` feature fails, but build is set up to handle that. Pair C aren't distracted by meaningless 'work in progress' failures and can get on with solving the problem they're trying to fix.

A couple of important notes on this process:

* *We don't check in failing unit tests.* The build as run by a similar script to the one above will pass, even with a failing `@wip` scenario, but will not pass if unit tests are failing. Passing unit tests are a sign of basic code integrity: if any of them fail it's very hard to trust the code at all.

* *We don't push @wip scenarios to the master branch.* If pairs A and B in the example above were both working in the master branch, they would get the other pair's failing scenarios when they attempt check their own `@wip` scenario. This introduces unnecessary noise into their work flow.

With a little build setup, and some effort and discipline on behalf of the team not to check `@wip` features to master, this workflow can be used to ensure that the build passes at each stage and yet the history of the development of features is preserved.

Do you have a preferred way of solving this problem? How would you do it?
