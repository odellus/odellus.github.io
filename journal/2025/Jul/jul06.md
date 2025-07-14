---
date: "2025-07-06"
title: "Real2Sim2Real2Sim2Real2Sim2Real"
---

# Always twirling, twirling upwards

So I spent a lot of time this weekend trying to align the simulation camera with the actual camera, even going so far as to come up with multiple approaches to solve this problem with varying degrees of math and automation. The quick math one worked well enough that I decided to let it rip and see if it can make sense of what it's seeing from camera one in the real world.


:::{figure} ../images/38.mp4
Look out baby 'cause I'm using technology
:::


MAN this is hot shit.



```json
{
  "base_camera_settings": {
      "pos": [0.020, 0.190, 0.505],
      "fov": 0.655,
      "target": [0.151, 0.10, 0.15]
  },
  "greenscreen_overlay_path": "bg.png",
  "spawn_box_pos": [0.3, 0.05],
  "spawn_box_half_size": 0.1,
  "domain_randomization_config": {
    "robot_color": null
  }
}
```


I can't express how grateful I am for the [sim2real][sim2real] project to work on. That's one way to get me to spend more time with Sapien and Maniskill!


I was having tons of fun trying to align the perspective of the camera in simulation with the actual camera on the mount connected to my so100's base. I eventually was like "I'm solving this with quaternions" in my [last post](../jul/jul05) but right after posting it I was like hey these are both cartesian positions above. The rotation about the quaterion isn't really important, just the perspective $\bold{p}$ such that $\bold{p} = (x, y, z)$ that points from the camera to the target, which can be represented as $\bold{p} = \bold{p}_{target} - \bold{p}_{camera}$.

:::{math}
:label:camera-math
\begin{align}
\bold{p}_{camera} &= (x_c,y_c,z_c) \\
\bold{p}_{target} &= (x_t, y_t, z_t) 
\end{align}
:::


:::{math}
:label:more-camera-math
\begin{align}
\bold{p} &= (x_t - x_c, y_t - y_c, z_t - z_c)
\end{align}
:::

So how does this help us align our simulation camera to our real camera?

# Translational motion

Any transformation of the coordinates $\bold{p}_{camera}$ and $\bold{p}_{target}$ where we preserve $\bold{p}$ is going to be translational motion, meaning there will be no rotation of our system of reference. So when we're so close to having them aligned and we just need to give it a kick in some $\bold{r}$ direction, just add or subtract the same quantity from $\bold{p}_{target}$ that you add to $\bold{p}_{camera}$ and the orientation of the direction you're looking will not change, just the position. Then once you get it pretty close you can fiddle with the orientation/target $\bold{p}_{target}$ more alone.


# Happiness

Cannot begin to describe how happy this makes me honestly. This is the future of artificial intelligence. Real2Sim2Real and back again. So I have got to spend a lot more time with maniskill and photogrammetry in general. Need a way to turn videos into URDFs.

Right now I'm training on my gpu laptop. I keep forgetting to talk about slurm. I *really* need to work on distributed inference for robotics. Two GPU laptops! I'm basically gpu middle class but I've got to slurm it so yeah lower middle class hahaha.

Here's the training run in wandb, which I do not really use because I like tracking my own damn metrics but whatever. Need an open source wandb. Is wandb open source? Can you run your own wandb server and issue tokens and whatnot? Well fuck me I guess [you can][wandb-server]. Okay I need to add it to my growing list of things I should put in a bunch of k8s namespaces on my slurm controller. I want to leave the compute intensive nodes for GPU inference and training and run shit like postgres, searxng, wandb (apparently), neo4j, openwebui, deer-flow, some web version of trae-agent, web based climate control and monitoring programs for the automated farm/lab and hell if I know what else eventually. I'm basically a corporation. Fucking odoo. ERPNext. That's what I need an AI for. Project management *shudders*.

I mean I talk about infrastructure on my landing page. I think it's really important.

:::{figure} ../images/so100grasp-wandb-run.png
A bunch of metric of our training showing we're learning to pick up a cube in virtual reality
:::


# Infrastructure

So I'm waiting for the PLA spools I ordered to get here before I start printing again. I bought some cheaper spools. 



[sim2real]: https://github.com/StoneT2000/lerobot-sim2real
[env-config]: https://gist.github.com/odellus/74c10ca972cb70cc133de402466d2878
[wandb-server]: https://github.com/wandb/server