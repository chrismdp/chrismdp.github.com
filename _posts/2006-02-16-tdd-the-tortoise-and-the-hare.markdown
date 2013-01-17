---
layout: post
title: TDD ~ The Tortoise and the Hare
date: 2006-02-16 09:43:00 +00:00
categories:
  - tdd
---
<div class='alert'><h1>By the way...</h1><p>This content is now pretty old: check <a href='/'>the homepage</a> for the latest.</p></div>
<p>Test Driven Development. Some people just don't get it.</p>
<p>Some people say: "A test for each feature? But that would mean writing twice as much code!"</p>
<p>These people usually go on to say: "It's just not worth it. I've finished my code, and it works, and you're still writing the test! I leave you in dust, 
you slow coding type!"</p>
<p>Then again, some people choose platforms, frameworks and even programming languages based on how easy it is to do TDD using them. If they can't do TDD ea
sily, they pick something else. They're that committed to it.</p>
<p>The hare starts out faster. The tortoise is much slower out of the gate. </p>
<p>The tortoise knows that the finish line isn't when the code is written, it's when the customer has a working product. The hare might think they've finish
ed, so they sit down and have a nap (or to stretch the analogy slightly, get bogged down fixing unnecessary bugs). That's when the tortoise overtakes.</p>
<p>I used to be a hare, running frantically back and forth over the whole codebase, changing things here and there until I thought I was done with a feature
. Invariably I wasn't; there were bugs to be fixed and features missed. I thought just because I could write code quickly, I was adding value quickly.</p>
<p>And then I fell in love with TDD. Since I discovered it after reading "Extreme Programming explained"  by Kent Beck (buy: <a href="http://www.amazon.co.u
k/exec/obidos/redirect?link_code=ur2&amp;tag=chrisparsonbl-21&amp;camp=1634&amp;creative=6738&amp;path=ASIN%2F0201616416">uk</a>   <a href="http://www.amazo
n.co.uk/exec/obidos/redirect?link_code=ur2&amp;tag=chrisparsonbl-21&amp;camp=1634&amp;creative=6738&amp;path=http%3A%2F%2Fwww.amazon.com%2Fgp%2Fproduct%2F03
21278658%2Fref%3Dpd_kar_gw_1%3F%255Fencoding%3DUTF8%252CUTF8%26ref%3Dpd%255Fkar%255Fgw%255F1%26v%3Dglance%26n%3D283155">us</a>), I've not looked back. All o
f my clients (like it or not), suddenly got test frameworks for free just so that I could develop using TDD. I rarely do any coding at all in any other way.
</p>
<p>Why use TDD? Here are my main reasons:</p>
<p><em>Refactoring power.</em> If I have a unit test testing each feature of my code module, I can merrily move stuff around internally as much as I like, 
without worrying if it's broken. At the end, I just run the tests. If it still works, I'm done.</p>
<p><em>Remembering what you are doing.</em> It's very easy in a large application to get lost on which feature you are currently coding. If you are coding 
using TDD, then you can't get lost. There's a very simple cycle to follow: Write failing test. Write code so test passes. Refactor if necessary. If you forg
et where you are, just run the tests. If they pass, you need to move to a new feature. If they fail, fix them. Simple.</p>
<p><em>Peace of mind.</em> I've written a large application recently which bills customers weekly for products. When I release a new version of the applica
tion, I <i>have</i> to know the billing is going to work. If it doesn't I get in a lot of trouble. Now I know the application is working before I release it
, just by running "ant test" and waiting a couple of minutes.</p>
<p>Hares start out faster. But they get complacent, they have a nap, and invariably run into problems in the end. Tortoises get to the finish line first.</p
>
<p>If you'd like to know more about TDD, visit these links:</p>
<p><a href="http://www.agiledata.org/essays/tdd.html">A nice TDD essay</a>, comparing TDD to MDD (model driven development).<br />
<a href="http://www.jamesshore.com/Blog/Microsoft-Gets-TDD-Completely-Wrong.html">A rebuttal</a> of Microsoft's version of TDD, with a very good intro to 'real' TDD, by <a href="http://www.jamesshore.com/">James Shore</a>.</p> 
