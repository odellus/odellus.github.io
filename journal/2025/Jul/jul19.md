---
date: "2025-07-19"
title: "Gear"
---


I guess I absolutely need to get the mystmd system set up because I have been microblogging all week. I even used freaking whtwnd and it's plain jane vanilla markdown smdh.

Yeah that's it. The fork of whtwnd must continue.


Let's revisit this real quick and take stock of what we've already put towards this.

1. We have our own PDS running on advanced-eschatonics.com
2. We have created a fork of the mystmd.org page's sandbox that uses codemirror for editing 
3. In our fork we have a fully fledged preview for all the features of mystmd
4. We have a vision

# VISION

1. pds.advanced-eschatonics.com — figure out configuration to host here rather than www or just raw advanced-eschatonics learn about how to host on multiple domains
2. Fork of whtwnd — Add in our CodeMirror editor with full preview functionality
3. Fork of whtwnd — Add in projects and ability to use custom CSS and myst.yaml
4. Custom mystmd themes — Make fancy mystmd themes that users can remix and extend for custom book sites
5. AI assistant to help you organize your projects — and your life



# `trae-agent`
Not super impressed with capabilities. Don't want to turn loose on anything with model I have to pay per API call for.


# `smolagents`
Works very well with gemma3n:e4b on search. Needs visit page tools and some kind of mechanism for generating sets of related questions that will yield releveant results. Scatter those queries to parallel agents followed by a merging/gathering node that kind of thing.


# Lerobot
I should probably use blender to align these STL files because blender is mesh first while FreeCAD is not. I'm not trying to do any solid modeling like I did with the base, I just need to scale and translate the base into the same frame of reference as the base. Then I can yoink the camera coordinates right out of the URDF instead of fucking around with the problem of general alignment. Minimal calibration close to the optima will work. I should model the damn webcam too while I'm at it. A cyclinder will do the trick.

Trying to figure out how to scale meshes in FreeCAD is kind of a pain honestly.

# Farming

I haven't printed a single tower or even really thought of the planting towers. I really just need to build a damn scaffold out of 2X4s.

# Infrastructure

`coast-after-1` had been on the fritz. Nvidia drivers completely in revolt. I feel like I've purged them multiple times by now but nothing helps. For some reason I'm acting like updating all of the laptops (three of them) is a huge pain in the ass. For the amount of time I've spent crying and trying to fix the drivers I could have 24.04 installed on all three with slurm configured and running sglang distributed by now.

Got to get out of that mindset. Honestly I kind of want to learn more about ansible. Really need an NAS for all my files.

Check engine light cut on in my truck. Needs an oil change too but I checked the oil change light and that's not it. Hopefully it's not something too damn expensive. It does shake and knock something fierce. Been meaning to get it looked at.


---

This is why I don't have a projects page. Trying to constrain my writing before it happens is a losing battle. I should just yack and yack and figure out where it falls later, if I even care.


I started looking at NAS and I don't think it's a bad idea. I've got to start thinking like I've got a cluster instead of just a laptop. There are three gathered in my name.


# Humanoids

So apparently [Unitree][unitree-r1] just released a super capable humanoid for only around $6k and I'm buying one. I will fly to SV and go to their store in Mountain View. This thing is going to pick strawberries. Ah it doesn't have hands! That's going to be a blocker.

The [HOPEJr][hope-jr] being put together by Robot Studio and Lerobot is exciting! Being able to build your own robots is extremely good. Hell if I could buy a unitree r1 and put my own lightweight hands on there it'd probably save me a mint.


# Agents 

So I can't really go into depth about it like I can about `trae-agent` or `smolagents` here because it's work, but I spent some time working on some cool tool calling stuff with langgraph and I feel pretty good about it.

# Idea
Log into work computer from here and ssh/remote in so you don't have to code switch between macos and linux keyboard layouts. No seriously. I'm freaking serious. Looks like I don't have sshd running over there. Ah well. Probably for the best.



# Infrastructure, again — Infrastructure 2

Okay I'm going to upgrade everyone to Ubuntu 24.04. We're all making the switch. In for a penny, in for a pound. Then we're going to do a few things:

1. Configure drivers with ubuntu drivers BEFORE installing cuda
2. Install cuda through nvidia but NEVER drivers
3. Repeat on both machines
4. Think about what I'm going to miss the most and push it to huggingface or github or google drive
5. Look into SSD NAS — I see one here on amazon for $400 with four bays, 4 TB SSD is ~\$250
    - seems expensive at first, but when you upgrade from a 4 TB to a 16 TB SSD NAS for the same price again it'll be well worth it
    - I want to treat it like an 8 TB SSD and have them back each other up so when one fails I can swap it out for a new one and stop using cloud
6. Configure network and `ssh-copy-id` everyone onto the same page with funny names like `slurmotron` and `coast-after-1` and `coast-after-2`
7. Install SLURM and configure GPUs
8. Look into distributed inference platforms in addition to what we can already do and have done with distributed training
9. Put all of the more lightweight, non-GPU centered services into a helm chart or a series of helm charts and spin up microk8s on `slurmotron`
10. Figure out a way to connect our slurmotron/kube clusters to the cloud through our PDS
11. Add things as necessary in the development of AI assistants for program sythesis and information retreival research and development
12. Connect with Lerobot through VLMs
13. Buy a fancy Spark DGX clone when they come out and figure out how to network them together
14. Probably have to buy a mellanox nvidia connectx-7 NIC and put together a box just 

I never really understood the point of a NAS but with slurm and a distributed system I think it would behoove me to go ahead and have a NAS.

## Benefits of an SSD NAS over individual drives:

The initial cost of an SSD NAS might seem high, but it offers several key benefits compared to using individual SSDs and external enclosures:

* **Redundancy and Data Protection:** A multi-bay NAS (like the one mentioned with four bays) typically supports RAID configurations. RAID (Redundant Array of Independent Disks) allows you to mirror or stripe data across multiple drives. This means if one drive fails, your data is still safe on the other drive(s). This level of built-in data protection is complex and often requires additional setup and management with individual drives.
* **Centralized Data Storage:** A NAS provides a single, centralized location for all your files. This simplifies backups, sharing, and access for multiple users or machines.
* **Scalability:** As you mentioned, NAS systems are designed to be scalable. You can easily add more drives to the NAS over time to increase your storage capacity without needing to replace the entire system. This can be more cost-effective in the long run than constantly buying and managing individual external drives.
* **Performance:** Many NAS devices are designed with features that optimize data transfer speeds, especially in a network environment. This can lead to faster access to your files compared to using individual drives connected via USB.
* **Simplified Management:** NAS devices often come with user-friendly management interfaces that make it easier to configure, monitor, and maintain your data storage.

While you *could* use individual drives and external enclosures, it introduces complexities in managing backups, ensuring data redundancy, and potentially dealing with compatibility issues. An SSD NAS offers a more integrated and often more reliable solution for a distributed system like yours with Slurm.


Yeah I'm about to have to start spending on NAS. Going to be like okay might as well get the 8 bay hell. Oh lord.


--- 

# possible fix for nvidia drivers

Quick-and-dirty recovery without a full reinstall:

1. **Boot into recovery**  
   GRUB → “Advanced options …” → pick the *-recovery* kernel → root shell.

2. **Purge everything NVIDIA**  
   ```bash
   apt-get remove --purge '^nvidia-.*'
   apt-get autoremove
   rm -rf /etc/X11/xorg.conf /usr/lib/modprobe.d/blacklist-nvidia.conf
   ```

3. **Let Ubuntu pick the driver**  
   ```bash
   ubuntu-drivers devices          # see what it recommends
   ubuntu-drivers autoinstall    # installs only the .run file from repo
   reboot
   ```

4. **Install CUDA**  
   ```bash
   sudo apt-get install cuda-toolkit-12-4
   ```
   DO NOT INSTALL THE DRIVERS AT THE BOTTOM OF THE INSTRUCTIONS



That usually gets you back to a working GUI + CUDA in ~15 minutes.

Okay I'm asking again and it's calling what I'm doing yak shaving lmao.

I'll give it one more try tomorrow and see if it work. After that I'm going to just upgrade everyone to 24.04.

It's telling me I should use wireguard to connect my droplet to my local cluster.



# agentic knowledge discovery

Use SearXNG, smolagent, open models hosted in a distributed fashion to populate some Knowledge Graph of concepts for molecular biology and synthetic systems biology. Or maybe for dynamic photogrammetry. I want it to connect code to research. Not just reading and summarizing, but connecting the papers with the code and doing novel research by drafting hypotheses and testing them in the codebase for truly synthetic research agent. Put all the results in some kind of knowledge graph-y type of database where these things can be retrieved with cypher queries our system generates on the fly for closer approximation of long term memory.

Just let is sit there and work on moose. Work on sapien and maniskill and dynamic photogrammetry. Work on epiwad and systems biology research. Build on top of what's already understood and what they're doing already with [scBaseCount][scBaseCount].

Get them to do research in mathematics and physics as well as biology and computer science/engineering. Publish their results in beautiful formatted mystmd directly to whtwnd. Have it generate figures from code and use like qwenpali to index the information not just in papers in downloads from the internet, but also from papers it generates itself.


I think this is why I'm so focused on mystmd. I see the cross referencing capabilities as a way of automating citations for LLMs. See I'm very smart.

I miss math. Need to center math more. Love it.


# Whitewind

Wow this codebase really sucks. They don't tell you how to run yourself.

[unitree-r1]: https://www.unitree.com/R1
[hope-jr]: https://github.com/TheRobotStudio/HOPEJr
[msi-spark]: https://ipc.msi.com/product_detail/Industrial-Computer-Box-PC/AI-Supercomputer/EdgeXpert-MS-C931?utm_source=nvidia
[slurm-inference-example]: https://aflah02.substack.com/p/multi-node-llm-inference-with-sglang

[scBaseCount]: https://github.com/ArcInstitute/arc-virtual-cell-atlas/blob/main/scBaseCount/README.md