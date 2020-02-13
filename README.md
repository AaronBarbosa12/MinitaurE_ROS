# MinitaurE_ROS
Package for manual and autonomous control of the Minitaur E from Ghost Robotics, using the Robot Operating System (ROS)

## Requirements
## Hardware
* This SDK was written with the assumption that the Minitaur E uses a [SLAMETECH MAPPER M1M1 (Developer Edition)](https://www.slamtec.com/en/Lidar/Mapper) for autonomous navigation. 
* Manual control of the robot is achieved with an [XBOX ONE WIRELESS CONTROLLER](https://www.amazon.com/Xbox-Wireless-Controller-Black-one/dp/B01LPZM7VI?th=1) 

## Software
* Create a machine running Ubuntu 18.04+
* [Install ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu)
* [Install the Ghost Robotics SDK](https://gitlab.com/ghostrobotics/SDK/-/jobs/artifacts/master/download?job=deploy_artifact)
* You'll need TWO wifi capable adapters (One for connecting to the robot's onboard computer, and another for connecting to the LIDAR's wifi network)

## Installation
1. After installing ROS, [create a catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace), if you haven't already.

2. Clone this directory to (YOUR CATKIN_WS LOCATION)/src

```python
git clone https://github.com/AaronBarbosa12/MinitaurE_ROS.git
```

## How To Use This Package
