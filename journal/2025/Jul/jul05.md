---
date: "2025-07-05"
title: "Qwen3 and trae-agent"
---

# `trae-agent`

So cursor apparently realized now that Cody is dead they're the king of the mountain and the features they currently offer for \$20 a month are now going to retail for \$200/month. So I've been setting up [continue][continue] with huggingface providers because Qwen3-235B-A22B is a damn good model for only \$0.22 per 1M input tokens and \$0.88 per 1M output tokens.

I mean it too. Tool calling is just as good as the proprietary frontier models. Deepseek-R1-05-28 is \$3 per 1M input and \$8 per 1M output tokens and it's only a _slightly_ stronger model.



So now I'm using continue with my huggingface router at home and there are problems with the agentic features so I'm like okay no worries. I see [`trae-agent`][trae-agent] with claude 4 (probably opus) is now at 75% on swe-bench-hard and at the top of the leaderboard so I'm like okay let's see what's going on with `trae-agent`.

I wire it up and it's using the Response API from openai, so I am like damn huggingface providers only supports chat completion API so I decide to hell with it I'll just set up an account on fireworks. I see in their docs they do support Response API, but then I get into it and they only support github mcp servers as tools currently.

So I start refactoring trae-agent's openai-client to use the standard openai chat completions and it's taking me forever to figure this out but eventually after instrumenting up trae agent with [arize phoenix][arize-phoenix] I figured out how to get it to use the tools available to trae-agent. I'm still debugging the way it adds the responses to the tool calling to the messages history but I quit at around 16:00 today because it's Saturday and I was like screw it. I'll get to it later.


# lerobot-sim2real

So my cameras finally showed up and I started going through the process of getting the camera calibrated for sim2real and it is a **HUGE** pain in the ass. Where the camera sits and points makes it very difficult to calibrate due to its proximity to the robot. I got so frustrated I decided to just start modeling the entire base + camera mounts I have STL files in Sapien so I don't have to fiddle with alignment. I mean I have a digital twin of every part of this.

Also there's a better damn way to do this with surface geometries and whatnot from the real robot to the simulated version rather than doing it by hand. Driving me bananas. Spent all night working on just aligning a fucking camera position and target and it's still not working. Cannot get them aligned by hand. I mean wow. I should probably just start with very basic top down probably because the geometry of moving the camera position while keeping the target stationary makes for some complicated tuning when I just need to put this all in the URDF and know the camera positon deterministically. I can model the webcam as a cylinder. It'll be fine. Then I just tune the view/orientation instead of the position, which should be easier.

:::{figure} ../images/alignment-problem.png
:label: misaligned-robot
A robot out of alignment with its digital twin
:::


I kind of do want to use computer vision to calculate the normals on the real robot and use those to align the camera position tbh.



But yeah this is two days of not doing work stuff 10 hours a day. We shipped a new on demand feature this week and it was a lot of work. Tons of moving parts. Pretty tired honestly and what do I start doing? Coding and robotics.


Looking at this image in my journal it's making me think of Clausewitz and [Friction][friction], which is of course in this context defined as
> "the force that makes the apparently easy so difficult."

I just want to take the damn images and move them transversely. Free the viewpoint to move too that's fine we're in fucking tuning Floyd Rose tremolo territory here. Ugh I wish it were actually a damn quaternion instead of some fucking position it's staring at. 

Okay maybe I need to do a post on quaternion math so I can move the point along with the position. Define an orientation and then I can just translate the camera where I need it to be. That's the problem. Need to work on that and put it in latex after putting it into code.

:::{tip} Change the target in an intelligent way
Write functions to 
- calculate the quaterion that represents the orientation of the camera give its current target and position
- Given a camera position vector and quaternion representing its orientation, compute the target value of the camera
:::
This will allow simple transverse motion when modifying the coordinates in the geometry represented in [`env_config.json`][sim2real-camera].


I do want to get into doing this with a 3D computer vision based approach that doesn't require manual fine tuning of the camera alignment.

# Value in DIY

I firmly believe in the value of creating tools for yourself. I also firmly believe in reusing what's out there and has been shown to work instead of reinventing the wheel just to feel like you did something. I didn't really want to work on a coding agent this weekend, but it was just released and cursor is rent seeking now that sourcegraph has given up the fight in favor of the per API call billing model. And now I'm paying per API call. My qwen3:latest through ollama is great, but I really do need more capable models for coding agents so I can be as productive as possible.


I just see the price of these solidworks licenses and now cursor basically wants $2400/year for the level of use I've been putting into it and yeah. I'm hacking on [`trae-agent`][trae-agent] because it's not like I don't think I'll be able to afford \$200 a month for a tool that lets me fly at work, but because there are knock-on effects for doing things yourself.

I didn't want to get sucked into the pay per API call model but the free VC money API calls dried up with the competition to cursor.

I'd rather just pay for one of the [Spark DGX clones from Asus][ascent-gx10] when they come out. Supposed to be this month?


# Projects

Okay I **really** need to set up a projects directory to go along with the page. [I've mentioned this before](../jun/jun21) and I gave a nice little mermaid diagram to illustrate the projects.

Hell my front page is basically a redunant projects page. I need to fix that.


## PROJECTS
- sim2real
- hydroponics
- coding agent
- book


I was content with cody. I mean no I wasn't. The only project on my projects page is Humberto, which I haven't worked on in months and is pretty much just connecting MCP and Qwen3 to ollama and a zany system prompt.

I do believe that code is the way for agents to do things. Setting up all of the nodes and Send and Command/interrupt stuff in langgraph is cool and it is good at determining workflows on a rail, but more open ended agents don't need it. They just need to be able to run code. Which is why [`trae-agent`][trae-agent] is only 4 tools inside a trenchcoat, one of them being `bash` hahaha.

I mean I want to design generic agents to help with planning and be an all around assistant, but the first thing I've been tasking my assistant to do is code, so probably should stay with that theme. Let the other stuff drop out of the code. Math, chemistry, biology, physics, engineering. Let it fall out of the code.

Perfect sandbox for an AI to learn.

# AI4Research

So it looks like someone put together a survey of all of the AI for research papers out there. There are plenty of approaches to automating the aquisition of knowledge. I should spend some time reading these and experimenting with the different approaches.

I want a Deep Research I can run locally against a model I can host on a couple of [Ascent GX10s][ascent-gx10] that sits there and writes code to run experiments, evaluate the results, and refine its approach under the supervision of agents whose goal is more of an asshole PI filter that I will take on periodically as it brings important results to my attention. Results I direct the agent towards and independent discoveries it ranks as germane enough to warrant annotation.

I am going to create a data flywheel on my local system.

I forgot to mention the whole slurm cluster thing. I've got slurm installed on my three laptops and home, two of which have GPUs. Now I know the GX10s won't be connected through slurm necessarily but they actually might I don't know. I haven't spent the time to get it working past the hello world version of running slurm on the remote machine.

I then got into the deep end of wanting to create my own whtwnd fork that uses jupyter book/mystmd for rending executable books to make it easier for people to publish clean websites and enhance their literacy through advancements in typesetting. I really do believe in it. I think it was time well spent even if I haven't really used it since I gave up and started using `uv run nox` with sphinx and doc-utils. It's a hack. I'm going to get back into the codemirror myst editor preview before I know it and I'll have my pds at pds.advanced-eschatonics instead of right at the site and when you go there (not pds, www or whatever) you'll see a slick video landing page like I'm trying to take all of your money and I don't even feel bad about it. 

Sim2Real is a super cool way to make neat graphics too! 


[trae-agent]: https://github.com/bytedance/trae-agent/tree/main
[continue]: https://github.com/continuedev/continue
[arize-phoenix]: https://github.com/Arize-ai/phoenix
[ascent-gx10]: https://www.asus.com/event/asus-ascent-gx10/
[friction]: https://www.clausewitz.com/readings/Warfit1.htm
[sim2real-camera]: https://github.com/StoneT2000/lerobot-sim2real/blob/main/env_config.json
[ai4research]: https://ai-4-research.github.io/