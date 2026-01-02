---
date: "2025-12-08"
title: "Zed, OpenCode, and crow"
---

I ported the agent backend of [opencode.ai](https://opencode.ai) to rust and I couldn't figure out how I wanted to put together the frontend. I started with dioxus, realized doing web editor with syntax highlighting in the browser with rust is like putting a man on the moon, and decided I needed monaco. 

I would eventually decide that yeah, I guess the future of what I want to build is sort of desktop apps. Even if it has to communicate to some remote backend, like this is **my** software I'm talking about building here. Of course I'm going to take the time to install it. I don't actually hate apps. I hate _other people's_ apps.

So I'm building this thing which I've decided to call `crow` that's the backend of opencode ported to rust and I'm putting together a monaco text editor for it in tauri and I'm like "bro. wtf am I doing? use zed man. just use zed."

Because I've been mad at zed. They closed my PR without reviewing or even really reading it and no it wasn't the most thrilling PR ever but I was able to get zed's native agent working again with my workplace's litellm + bedrock anthropic and they didn't even care enough to read the fucking PR. Just _rude_. So yeah I'm building on zed and I don't really have amazingly great things to say about them at this time. I use their editor. I'm in the process of making it my editor.


I just want a rust IDE and don't want to have to build my own so yeah, building on top of zed now.

To me it makes sense to start over and build inside of zed instead of trying to perfect ACP inside my rust port of opencode. For one, I use zed agents. Until just a few weeks ago they were the only kind of agents I really used for work. 


:::{figure} ../images/crow-sc.png
we've got a whole website
:::


---
# Why?

> Q: There are a million and one agent IDEs out there, why am I doing this?

Because this is **my** agent IDE. I'm doing this to control my own tools. To own my own software stack. Nothing to get me to understand my IDE like forking it.


But really okay glad to be hashing this out here. The real reason is that I bought an AMD Ryzen AI Max+ 395 and I want to keep the thing continually busy. It is slow, so I need some kind of feedback to keep the react loop party going.

I've written extensively about trae-agent and how it is more of a fire and forget type of tool from the way it loops continually with no human feedback.

I wanted the same type of behavior in my agent IDE, so I'm building it with _zed-becomes-crow_.

# Journey

So I started out coding using emacs and at the time everyone was using sublime because we were all moving away from using visual studio. This was before visual studio code became the de facto IDE for developers. I got into using atom editor, which was like an open source sublime but it came late and ended up being like vs code at the same time as vs code was coming on the scene and yeah I used VS Code for years and years. From like shit I think 2015-2025 almost? That doesn't seem right but something not too dissimilar from that.

Anyway agents for coding become a thing. Copilot yada yada. I try out Cody from Sourcegraph and I was impressed. This thing was good. And only $9/month it's doing my job for me hell yeah. Anyway I started to feel like it was getting buggier and buggier and sourcegraph had this new more like claude code type deal they were calling Amp and they decided to discontinue Cody like 5 days after I cancelled my subscription and jumped ship to cursor.

I'm using cursor at this time and I'm like freshly rug pulled by sourcegraph and everyone is telling me I've got to try out claude code, but I'm getting to the point I'm like alright I've had enough of this shit, I'm about to check out the open source versions of claude code.

I find trae-agent and start using it. It's phenomenal. I find out about zed and I start using it. It's phenomenal. The agent is really top rate, but they're not really developing it actively as much anymore in favor of their ACP system and its external agents, which is like well fuck.

So I buy this AMD Ryzen AI Max+ 395 and I am using with zed native agent and it's _good_. Like really good. But it's slow as fuck because I'm running glm-4.5-air, a 106B param model on a fucking micro-itx desktop so I really want to be able to use it more like trae-agent with the fire and forget style.

I'm building the PRs for llama.cpp that support tool calling for glm-4.5+ models along with qwen and a bunch of other new models that use XML for their tool calling output schema and I see someone say "I tested it out in opencode" and I'm like "what the heck is opencode?" so yeah that was like a couple of months ago now and I've basically been working on converting the codebase to rust ever since.

I went down so many routes. First it was going to be a dioxus web IDE then I tried to do syntax highlighting in a rust web editor and was like whaaaaaa web editors have hands so I am like okay fuck it I'll use monaco then for some reason I'm like "this is going to be my own app. I don't want to use it through a browser. I'm going to install my app on whatever device I'm trying to access this from." and I start building a desktop tauri app from my rust port of opencode and I'm like how do I do this? Okay fucking monaco. Jesus wept I started all of this to bring the agent into rust and I'm going back to javascript for the frontend with tauri and like...I'm doing all of this through my IDE zed, which I've forked and fixed before.


So like last week I said fuck it I'm doing this shit in zed native agent and I did. I have a whole dual agent that sort of works in zed native agent. But it's a hack. the todo list and the plan visualization in ACP client aren't as much, those are legit awesome and the dual agent certainly has the potential, but like I'm buidling it from like coding agents. Fully mature coding agents and I'm like hacking this shit together and that plus the 30 minute build times of the "last 10% is 90% of the work" stuff from my work on the native agent had me decide to build yet another rust coding agent cli. I think this is like my fifth in the last two months and I can tell I've been getting a bit better about it each time.

The focus has been on observability/telemetry. You don't need to connect langfuse to crow-agent it's got langfuse telemetry built into the CLI. You can run SQL queries across the tables we keep spans in from the CLI. It's an agent library build by agents, FOR agents. That's why it's a cli. That's why telemetry as first class citizen from that same CLI.

So yeah I'm still working on my own fork of zed. I still want to do work with the native agents to improve them, but I'm a little less worried about it than I was before. I want to integrate my external agent into zed's ACP the way claude code has been integrated into the ACP. It looks really good. It works well. I've got my crow-agent working with zed ACP. Well really it's crow, but I'm not going to try to break ACP in the process of doing what I want to the zed source code, but yeah I'm sort of focused more on the external agent and integration with zed's ACP as UI/IDE for my coding agent.

I do have all sorts of things I want to do with zed. I am imagining either building on top of the crates that are actually separable crates to get to some sort of minimal "monaco for rust" type of situation with zed so I can use gpui and the lsp and rope stuff more as libraries than having to fork zed the application if I want to re-use their work.
