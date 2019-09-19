# ROS Overview


This repository is to be a comprehensive collection of examples and templates to best understand the tools available provided by ROS.  


Files that directly support a particular node design are found in the src folder of a repository.  Python files that are supplementary are found in the scripts folder (ie do not directly contribute to the node or primary intent) as per ROS development guidelines.

## Outline



## Docker

The examples are intended to also be compatible with docker containers for repeatability and to introduce the concept of docker containers into the ROS ecosystem. 

### Examples

1. cpp_basic_class_design
2. messages
3. pub sub
4. parameters
5. services
6. actions
7. packages (building, installing) => cmake

potential upcoming

- moveit (separate ? investigative?)
- unit testing
- dynamic reconfigure & advanced roslaunch?
- debugging, logging, roswtf
- example simple package combining stuff
- distributed ros? ros master?
- rosserial
- behavior / framework?
- advanced?
- ros_control
- navigation?
- hardware_interface



### Templates

TBD


consider example commands for building a new package

test


## Sections

### 1 cpp_basic_class_design

This section covers the basics over developing a class design for the execution of a ros node and the essentials surrounding ROS operation.  This first package contains many elements that are reviewed in greater detail in that respositories readme file.

The repository contains two primary files, the first containing the design of the node.  The second file instantiates the node object and executes it per ROS directives.

Compiles with include folder.

Need to discuss the different types of nodes that can be created (anonymous, named,etc.).  

### 2 messages

Compiles with message folder.

### 3 pub_sub

Cpp and python versions.  Can execute either.
Need to investigate if python version needs execute bit to work.

#### Topics


#### Launch File Basics

- TODO (add to readme in the repo)

#### Excluded

- Setting up environment (provide reference?)
- topics



### 4 parameters

different ways to set/get parameters

### 5 services


### 6 actions




#### TODO

- Develop python class design version
- 




2. messages
3. pub sub
4. parameters
5. services
6. actions
7. packages


how to separate out executables
CMAKE


## References

- http://wiki.ros.org/ROS/Tutorials
- https://industrial-training-master.readthedocs.io/en/melodic/
- http://www.clearpathrobotics.com/assets/guides/ros/
- 

ROS books

### Unverified 

- https://github.com/ros/ros_tutorials
- https://github.com/ros-planning/navigation_tutorials
- https://github.com/osrf/rosbook
- https://github.com/qboticslabs/ros_robotics_projects
- https://github.com/mjshiggins/ros-examples
- https://github.com/ros-simulation/gazebo_ros_demos
- https://github.com/ATLFlight/ros-examples
- https://github.com/AaronMR/Learning_ROS_for_Robotics_Programming_2nd_edition
- https://github.com/fairlight1337/ros_service_examples
