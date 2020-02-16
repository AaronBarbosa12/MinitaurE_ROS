# MinitaurE_ROS
Package for manual and autonomous control of the Minitaur E from Ghost Robotics, using the Robot Operating System (ROS)

![Robot Image](images/minitaur.jpeg)

## Requirements
## Hardware
* This SDK was written with the assumption that the Minitaur E uses a [SLAMETECH MAPPER M1M1 (Developer Edition)](https://www.slamtec.com/en/Lidar/Mapper) for autonomous navigation. 

![Mapper Image](images/mapper.png)

* MinitaurE_ROS assumes that there are two computers connected to the same network: one directly mounted to the Minitaur itself (which sends movement commands over USB), and a MAIN_COMPUTER, which is used to remotely control the robot. 

![Network Image](images/comp_network.png)

* Manual control of the robot is achieved with an [XBOX ONE WIRELESS CONTROLLER](https://www.amazon.com/Xbox-Wireless-Controller-Black-one/dp/B01LPZM7VI?th=1), connected to the MAIN_COMPUTER.

## Software
* Create a machine running Ubuntu 18.04+
* [Install ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu)
* [Install the Ghost Robotics SDK](https://gitlab.com/ghostrobotics/SDK/-/jobs/artifacts/master/download?job=deploy_artifact)
* You'll need TWO wifi capable adapters (One for connecting to the robot's onboard computer, and another for connecting to the LIDAR's wifi network)

## Installation
1. After installing ROS, [create a catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace), if you haven't already.

2. Clone the contents of this directory to (YOUR CATKIN_WS LOCATION)/src

3. Build the workspace 
```python
cd (YOUR CATKIN_WS LOCATION)
catkin_make
```

## How To Use This Package
3. Open a terminal and start the ROS Master
```python
roscore
```

4. Open another terminal and open start the local ROS nodes 
```python
roslaunch minitaur_ros minitaur_client_nodes.launch
```

4. Open another terminal and open start the ROS nodes on the onboard computer (MAKE SURE THAT THE ROBOT IS SUPPORTED BENEATH - THE LEGS WILL GO LIMP BRIEFLY) 
```python
ssh odroid@10.42.0.1
roslaunch minitaur_ros minitaur_seraunch
```
