---
date: "2025-06-24"
title: "New lerobot environment, who dis?"
---

# Read The Docs
So I was scrolling deer.social and reading some scifi book after work and I was like:

> "You know what I need to be reading? The specs for the LeRobot SDK is what."  


So I did some reading on my phone and started digging into the [docs on huggingface.co][so100-setup]. 


## Just Do It!

Eventually got around to running this on my laptop and following along the [calibration video][calibration-vid] instead of trying to figure out how to move my old calibration json into the new environment. This was well and truly decided when I found out that the new calibration system, indeed even the whole origin for datasets with this new way of doing this is not [backward compatible][backward-comp] with the previous version of LeRobot I was using before tonight.

## Calibration and Teloperation

I could run this inside a jupyter notebook cell but I had to `uv run ipython` for the calibration sequence. After the first Enter key press it shorted out so I just calibrated from the command line.

```python
from lerobot.common.cameras.opencv.configuration_opencv import OpenCVCameraConfig
from lerobot.common.teleoperators.so100_leader import SO100LeaderConfig, SO100Leader
from lerobot.common.robots.so100_follower import SO100FollowerConfig, SO100Follower

camera_config = dict(
    camera_one=OpenCVCameraConfig(index_or_path=2, width=640, height=480, fps=30),
    camera_two=OpenCVCameraConfig(index_or_path=4, width=640, height=480, fps=30),
)

robot_config = SO100FollowerConfig(
    port="/dev/ttyACM2",
    id="my_so100_follower",
    cameras=camera_config,
)

teleop_config = SO100LeaderConfig(
    port="/dev/ttyACM0",
    id="my_so100_leader",
)

teleop_device = SO100Leader(teleop_config)
robot = SO100Follower(robot_config)


robot.connect()
teleop_device.connect()

while True:
    action = teleop_device.get_action()
    robot.send_action(action)
```

So yeah we're in freaking business!!! This was the big block in the road towards setting up [lerobot-sim2real][lerobot-sim2real]. Pretty much just have to follow along with the steps in the [tutorial][sim2real-tutorial].

## Lot of work to do

Right now I am [here][i-am-here]. Still a good bit of work to do. Wish I hadn't taken so long to just barrel forward but at least today I was aware enough to start doing some reading so I could get a good idea of what I needed to do. Turns out it's all reading! LOL

I also need to figure out how to include bibtex in myst.






[backward-comp]: https://huggingface.co/docs/lerobot/backwardcomp
[calibration-vid]: https://huggingface.co/docs/lerobot/en/so101#calibration-video
[so100-setup]: https://huggingface.co/docs/lerobot/en/so100
[lerobot-sim2real]: https://github.com/StoneT2000/lerobot-sim2real
[sim2real-tutorial]: https://github.com/StoneT2000/lerobot-sim2real/blob/main/docs/zero_shot_rgb_sim2real.md
[i-am-here]: https://github.com/StoneT2000/lerobot-sim2real/blob/main/docs/zero_shot_rgb_sim2real.md#1-setup-your-simulation-and-real-world-environment