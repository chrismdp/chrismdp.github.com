---
layout: post
title: Archivey the Robot
date: 2010-03-08 16:15:00 +00:00
categories:
  - google wave
  - coding
---
Following hot on the heels of [Pushy](/2010/03/introducing-pushy/), I've implemented the companion application Archivey. This will delete all but the last five messages on a wave, excepting the top message. It's meant to be used in conjunction with Pushy and any other chatty robots to keep the number of messages in a wave down to a manageable level.

Potential other uses would be in a chatting context: you don't always want to see the complete history of a chat session and this could be a way to hide the noise. Remember that you can always see the complete history by clicking Playback on the wave, so the messages aren't lost: they're just archived.

*To use, add archiveyrobot@appspot.com to a wave.* Be warned, as soon as a new message is added it will merrily start deleting messages, so be careful!

Source code on [github](http://github.com/chrismdp/archivey). Hope you like it: let me know if you find it useful.
