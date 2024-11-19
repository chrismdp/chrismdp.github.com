---
layout: post
title: How face generation works in Sol Trader
date: 2015-05-06 10:52:27.000000000 +01:00
categories:
- game design
- sol trader
- game development
- code
redirect_from:
- "/2015/05/how-face-generation-works-in-sol-trader"
---
We're finally getting customised faces for characters in [Sol Trader](http://soltrader.net)! Here's a preview of some of the different faces that can be generated:

![Face piece selection](/assets/img/sol-trader-face-preview.jpg)

There are created from individual face pieces that are overlaid together to produce the final result:

![Face piece selection](/assets/img/sol-trader-face-breakdown.jpg)

Read on to find out how the code works under the hood.

## Faces are completely moddable

Our face generation configuration file is found in `face_pieces.csv`. All the main data files in Sol Trader are now in CSV format to make modding super easy:

{%highlight text %}

piece,gender,count,chance
male_base_face,MALE,1,100
male_nose,MALE,10,100
male_eyes,MALE,5,100
male_eyes_overlay_cyber_eye,MALE,1,5
male_hair,MALE,10,91
male_ear,MALE,5,100
male_mouth,MALE,1,100
male_scar,MALE,1,5
male_suit,MALE,1,100
male_t_shirt,MALE,1,0
male_beard,MALE,5,30
eyeware,MALE,2,5
female_base_face,FEMALE,1,100
...

{%endhighlight%}

Each piece has its own line, with the name of the piece, the gender it belongs to, the number of options for that piece, and the percentage chance the feature is present or not.

It's pretty trivial to add your own extra options or entirely new face features! The only current restriction is that there must be less that 256 options for a face piece, and under 12 different face pieces in total, although I can increase these limits if modders need more room.

## Faces are genetically inherited

Once thing that I really wanted to get right was generated characters looking similar to their parents. In the game the faces are stored for each individual as an array of numeric options, with each face only three bytes in total:

{%highlight c++ %}

struct Face {
  uint8 pieces[12];
};

{%endhighlight%}

The game chooses a new character's face in a similar way to the way it inherits other attributes from parents.  When deciding on a face (when the character reaches the age of two), we go through every face piece in turn. 50% of the time the character will inherit that piece from the parent they most resemble, 25% of the time they will inherit that piece from the other parent, and 25% of the time the face piece is random, to simulate genetic mutation.

This process produces faces that resemble their parents, but aren't exactly the same. There are currently 66,000 combinations of faces for each gender so you're unlikely to come across two the same.

## Still to do

We've currently only modelled Caucasian faces. We're adding in other ethnicities soon.

Notice also that there aren't any older faces: Sol Trader is set in the 24th century, but technology hasn't sufficiently advanced to make 94 year old characters look like they're in their late 20s!  I like that way the [Crusader Kings II](http://www.crusaderkings.com) does ageing with faces, where they visibly get older over time. The drawback is always artist time required to produce these, but we're hopefully going for a simple overlay which could have the right effect.

What do you think?
