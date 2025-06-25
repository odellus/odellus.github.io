---
date: "2025-06-25"
title: "I don't know."
subtitle: "That's not my job"
---



I'm still so extremely pleased I can reference my book or my journal or my articles inside my site like this from chapter one of the scientific computing with python book's [`sin` curve](#sin-curve).


I need to take a short break from the drive to push through the lerobot-sim2real tutorial and study the [SmolVLA paper][smol-vla] and write something up. That's going to be extremely useful for me as I write my own book on scientific computing with python.

Speaking of? What is the deal there? Am I still doing this or what?

I spent a fuckload of time getting a mystmd codemirror editor working and then fall back to using fucking sphinx and doc-utils to host my site. LMFAO what a goon. Oh well. It works. I'm going to get this figured out to where I have the whole login setup working with whtwnd and real time codemirror preview all on my website advanced-eschatonics.com. 


---

## Content now is worth more than content later

odellus.github.io is a bridge so I don't waste time just worrying about tooling instead of doing what I want the tooling for, which is to write, write, write. Don't worry about fancy user interfaces and landing pages and whatnot right now. Just fucking write a bunch of myst markdown documents.

I need to get in the habit of writing up everything I've been working on that I can share. Write it down. I have tons of thoughts and write out bullshit tweets all day on deer. At least it feels that way when I use it. It's because it's just a website I can visit in the browser. Why I want that hosted on advanced-eschatonics.



I mean I don't really need nox or doc-utils or sphinx or any of that. `myst start` is pretty much all you really need in terms of preview capabilities honestly.

---
## FreeCAD STL -> STEP Part pipeline

So I spent the longest trying to figure out how to split a part, and the key is to create a plane from Primitive Graphic in the part workbench and place it so it intersects where you want the cut. Then you select both and do Split -> Slice Apart.

I'm trying to figure out how I can extrude from one of these surfaces right now. I want to extend the split part back to join the original, at which point I will do a boolean union to get back the camera mount inverted T with a longer base. I'm not happy with how close the camera mount rests to the arm. It seems like an obstacle.



:::{figure} ../images/freecad-cam-mount-bottom.png
:label: split-cam-mount

Camera mount I've managed to recreate from STL into STEP in FreeCAD
:::


So I'm like 30% of the way done with that part. The next thing I want to do is figure out how to rotate the part like 30-45 degrees inward. Right now the camera faces straight forward.

I've got the end piece here. I can go nuts creating my own stand that connects to the base. The base is what I really don't feel like redesigning. You know what? I know how I'm going to do this. I'm not going to try to make it beautiful and smoothly interpolated. I'm just going to make a cut, turn it 30 or 45 degrees then fuse it back in with a boolean union.


:::{figure} ../images/freecad-cam-mount-rotated.png
:label: split-cam-mount-rotated
Camera mount rotated 45 degrees to facilitate better overlap in the robot's workspace
:::

Okay I figured it out. I just inserted a box with the same dimensions. I went a little overboard and inserted another one on the other side even though we only need to extend on side. Then we'll build another part that rotates the other way and is extended on the other side.

04:11
---

:::{figure} ../images/freecad-cam-mount-rotated-extended.png
:label: split-cam-mount-rotated-extended
Camera mount is now rotated 45 degrees and extended to avoid collision and give better separation between camera perspectives for training
:::

## Design the damn tower rack man!

Now I need to bring this same energy to designing a rack to hold towers and their return gutter out of plywood, 2x4s, and 

[smol-vla]: https://arxiv.org/abs/2506.01844

