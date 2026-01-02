---
date: "2026-01-02"
title: Back on my bullshit
---

Back on my bullshit.

I don't really feel like giving the whole rundown but I'll just give a current snapshot of where I'm at today.

`karla` is a letta agent that I've created in python that has most of the capabilities of letta-code. I built it to be a CLI agent and an ACP agent primarily. Mostly focused on the ACP angle.

The big deal was finding out about [`marimo`](https://marimo.io). They're a new reactive jupyter notebook framework and they _just so happen_ to have an ACP client! In their reactive jupyter app. And of course they've got a terminal, a filesystem, and a minimal editor so I'm like you know what I'm in fucking business here. This is exactly what I was trying to carve out of `zed`.

So now I've abandoned my purity of desktop apps in rust for web apps but I have playwright to do all of the testing of the system end to end for me and honestly it's just a lot more relaxing to be able to tell the system to use the ACP client through the actual system I'll use it through than all of these hacks and tricks to use through the cli. They're brilliant and super important, but honestly using through the ACP client directly is the way to go.

Just using python and not trying to build the whole ecosystem myself is the way to go. I've done a lot of work inside my forks of various letta components, but I'm not really there yet with a full refactor to have my own letta clone. I did get started on it, treating their openapi.json more like a spec/protocol to be implemented, but I found I had more important things to work on, especially after asking claude about what other ACP clients are out there and I hear about marimo.

So yeah it's game on: I've got the web IDE I convinced myself I didn't want to build because I was too pure for monaco and it was going to be a pain in the fucking ass. I've got marimo having done a lot of the heavy lifting and I've got claude code working on creating a curriculum of coding examples we can use to train my letta agent to be as good at coding as claude code, basically.


So yeah I'm not writing in rust anymore. Shit I'm not even writing in python anymore. I'm prompting and working in the realm of concepts and ideas and the machine reports back what's available out there for us. And right now the best bet is to take marimo and to adapt what they've done to my purposes.


And also the whole web angle has me thinking about using it as a journal again and incorporating the planner app I built into it because like half of the tasks are coding tasks that karla/claude code can be scheduled to do? Like maybe while I'm working on this stuff I work on a way to use claude code on a task that's sufficiently difficult that karla fails on it? And we fallback?

That's sort of one way of doing this. Right now I have claude code using it to improve it, but at some point I'm going to start using it to improve it and I don't know if I'll just rush out to cancel my subscription immediately.

Claude code has this thing where they look at their response and autogenerate a response for the user based on the question being asked and like I want to do that for karla/crow so freaking bad.

So yeah I don't know about how long I'll be building on top of letta. I have a feeling I might do something even more opinionated, but first I'm really just trying to hook up my letta agent with the letta-code tools I've smuggled out of typescript and into python to this ACP client I'm putting together. Marimo doesn't really support custom ACP clients, and I'm not really trying to build notebooks as cool as marimo is (if I ever need that I'll just use marimo!) and honestly yeah I sort of feel like I'm building this on top of letta and marimo which is build on top of other things that's how it goes.

I've made some opinionated forks that I've had to make because of my local LLM constraints. And yeah they have an AI native editor? Completions and all that shit and we don't have to worry about it. Yeah I'm just going to use the parts of marimo as much as possible.


And there's going to be the part where I sit down and actually look at all this code with the agent guiding me through.

:::{figure} ../images/zed-purple.png
fork of zed I've been working on
:::

Same with actually using it too.
