---
layout: post
title: How I'm writing my book using Vim, Git and Ruby
date: 2010-11-02 15:35:27.000000000 +00:00
categories:
- git
- ruby
- writing
- pragprowrimo
redirect_from:
- "/2010/11/how-im-writing-my-book-using-git-and-ruby"
- "/2010/11/how-im-writing-my-book-using-git-and-ruby/"
---
I'm taking another shot at [PragProWriMo](http://forums.pragprog.com/forums/190) this year. For those who don't know, PragProWriMo is the Pragmatic Programmer's counterpart to [NaNoWriMo](http://www.nanowrimo.org/), which encourages participants to write a novel in a month, or at least make a good start. Last year, I got about 2,000 words into an interesting idea relating to the concept of quality, and I'm going to take that further this month.

Like any self-respecting geek trying to write a book, I've wasted a bunch of writing time trying to find the optimal workflow for the project. I tried [the new version of Scrivener](http://www.literatureandlatte.com/scrivener.php), and while it is feature rich and powerful, I found I was missing my programmer tools far too much. I've now settled on quite a nice workflow using 750words, Vim and Git, and I thought I'd take a few minutes to pen it for posterity.

## Step 1: Fling thoughts, ideas, and concepts into [750words](http://750words.com)

I love 750words and have written about my use of the site [previously](/2010/07/seven-hundred-and-fifty-words/). It's a great capture tool for random thoughts, words and feelings. I find it really helpful not to constrain my writing with too much structure to start with. It's a clean slate every day to write down what's inspiring me that particular day. I can also write these words from anywhere: on my phone as the moment strikes, on the iPad, whatever.

I try and get several hundred words done early in the morning: there's evidence that [your brain works better first thing in the morning](http://ezinearticles.com/?Alpha-Brain-Waves---How-to-Relax-Deeply&id=1905868). Whether or not this is true is debatable, but I know I'm certainly more aware of deeper thoughts and ideas first thing, and there are some fairly deep concepts in the book.

Using 750words also ensures that I write enough during any particular day. I know that if I write that many words, then at least some of the content is going to be interesting enough for the next step.

## Step 2: Organise my thoughts using Vim

I copy and paste the best and most interesting snippets from 750words into [Vim](http://vim.org). Vim is a fantastic editor for editing text. In full screen mode it's distraction free, the modal editing mean that I can move whole sentences around very easily without ever reaching for the mouse. I try to keep each file fairly short and express different thoughts and sections in different files. I'm using [maruku](http://maruku.rubyforge.org/maruku.html) (thanks to [@glv](http://twitter.com/glv)) to tag each text file with tags, such as 'first-draft', 'revised-draft', 'todo', and so on. My hope is that this will become useful later on when I start to pull things together.

These files are checked into [Git](http://git-scm.com) and I've put the repository on my [Dropbox](http://dropbox.com) folder so it's backed up. So far, so good.

## Step 3: Structure the content

I've started on a super simple Ruby DSL for organising the content into a real book:

{% highlight ruby %}
book "Title" do
  part "Introduction" do
    section "Section Title", "documents/intro.md"
    section "How to read this book", "document/how_to_read_this_book.md"
  end

  chapter "The first chapter" do
    section "Section Title", "documents/intro_to_chapter_one.md"
  end
end
{% endhighlight %}

This DSL currently has no code behind it, but it feels like it makes sense. It's easy to read and modify, and to swap sections of the book around as my thoughts take shape.

## Step 4: The future

That's enough workflow for now. In the future I want to write a gem that you can use in the following way:

{% highlight bash %}
# Open a random document tagged with draft in Vim
$ book revise

# Export the book to PDF (or epub, etc)
$ book compile

# Check how many pages/words are currently present in the final structure.
# Perhaps even draw some graps and put together nifty stats from git...
$ book stats

# Check in everything to git for the day and write a comment
$ book commit <comment>
{% endhighlight %}

I know if I blog for too much longer I'm going to fall into the [Rimmer Trap](http://en.wikipedia.org/wiki/Arnold_Rimmer#Life_on_board_Red_Dwarf), so back to the book :)

Let me know if this is helpful, or if you plan to use a similar Ruby DSL: perhaps we can work together on the creation of it.

Good luck to all my fellow PragProWriMo writers!

*UPDATE:* Wow, what a lot of interest! There's now a repository for this gem [here](http://github.com/chrismdp/book) and an active community of developers already! Let me know if you want to be involved with coding it, and I'll keep this blog up to date with progress.

