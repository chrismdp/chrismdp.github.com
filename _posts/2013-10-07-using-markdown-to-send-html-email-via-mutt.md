---
layout: post
title: 'Use Markdown to send HTML email via Mutt: now working on iOS mail'
date: 2013-10-07 20:23:24.000000000 +01:00
categories:
- email
- config
- howto
- mutt
- ios
- markdown
redirect_from:
- "/2013/10/using-markdown-to-send-html-email-via-mutt"
- "/2013/10/using-markdown-to-send-html-email-via-mutt/"
---
A technical configuration post this time around. If you're a fan of the [Mutt](http://www.mutt.org) command line email program then read on...

For a while I've been writing HTML email using Markdown, on the odd occasion I feel the need to format my emails. I've followed the instructions on [this site](https://dgl.cx/2009/03/html-mail-with-mutt-using-markdown) and it's been working to great effect: except in one specific case.

If you also attach a regular file to the email, as well as the HTML output, the [text2mime-sendmail.pl](https://dgl.cx/2009/03/text2mime-sendmail.pl) script provided stuffs the attachments into the same `multipart/alternative` section. Many email clients can figure this out and display the attachments anyway, but crucially it seems that iOS mail can't, which means that you either only see the attachment, or you only see the HTML without an attachment.

In order to fix this, I rewrote `text2mime-sendmail.pl` in Ruby: the original Perl was doing manual text processing, and it seemed to be a good idea to use a proper mail library. I used the [Mail](https://github.com/mikel/mail/) library in Ruby to parse the email and send it out with the attachments outside the `multipart/alternative` block.

[text2mime-sendmail.rb](https://github.com/chrismdp/config_files/blob/fffbf8c9d24cdf1c03ee06f5f2cddd4b0c70007c/mutt/text2mime-sendmail.rb)

The full issue is described [here](https://github.com/mikel/mail/issues/590) - I think it's a bug in iOS Mail rather than anything else.

So, if you're using the approach referenced above to send HTML email in Mutt, you might want to switch to my script, or modify your scripts to do a similar thing so that your emails are still readable in iOS Mail. Good luck!
