# Package Level Information


## Creating Packages

This document assumes that the user has installed the catkin-python tools package, and does not make use of the catkin_make commands.

```
usage: catkin create pkg [-h] [-p PATH] --rosdistro ROSDISTRO
                         [-v MAJOR.MINOR.PATCH] [-l LICENSE] [-m NAME EMAIL]
                         [-a NAME EMAIL] [-d DESCRIPTION]
                         [--catkin-deps [DEP [DEP ...]]]
                         [--system-deps [DEP [DEP ...]]]
                         [--boost-components [COMP [COMP ...]]]
                         PKG_NAME [PKG_NAME ...]
```


To create a package complete with dependencies, invoke the following:

```shell script
catkin create pkg pkg_name_here --catkin-deps roscpp rospy
```

## Inspecting Package Dependencies

Dependencies can be checked using the following command using relative or global paths.

```shell script
rosdep install --simulate --from-paths ./ --ignore-src

rosdep install --simulate --from-paths ~/catkin_ws/src/moveit_tuts/moveit_tutorials/ --ignore-src

```

Alternative method, lists even system dependencies:

```shell script
rospack depends moveit_tutorials
```

Alternative visualization:

```shell script
rqt_dep
```

In the search box at the top, enter in the package name of interest.  Make sure the environment is sourced first.  This tool may not pick up on python dependencies.

### Base New Package from Existing

Using the following command, get top level dependencies to use as a template for another package.  Using the following command:
 
```shell script
rospack depends1 moveit_tutorials | xargs echo "catkin create pkg pkg_name --catkin-deps "
```

Will yield:

```shell script
catkin create pkg pkg_name --catkin-deps  panda_moveit_config pluginlib moveit_core moveit_commander moveit_fake_controller_manager moveit_ros_planning_interface moveit_ros_perception interactive_markers moveit_visual_tools joy pcl_ros pcl_conversions rosbag tf2_ros tf2_eigen tf2_geometry_msgs
```

From this result, weed out unnecessary packages such as joy, interactive_markers, etc and execute.

Working example:

```shell script
rospack depends1 ur_incremental | xargs echo "catkin create pkg pkg_name --catkin-deps "
catkin create pkg robot_information --catkin-deps  moveit_core moveit_ros_planning moveit_ros_planning_interface moveit_visual_tools pluginlib roscpp std_msgs tf2_eigen tf2_geometry_msgs tf2_ros

```

## Check Catkin Environment

Make sure to have python-catkin-lint package installed, preferrably through pip.

Navigate to the repository / package in question and execute the following command:

```shell script
catkin_lint
```

A list of warnings and errors will be printed to the screen for the user to review and address.  There are several flags and options to set to analyze the output effectively.

### ROS lint

TBD

Can filter certain errors from linter.  Can pull in some style types, and potentially automatically fix certain issues (such as whitespace).  
Works also with python.

- https://github.com/ros/roslint
- http://wiki.ros.org/roslint


```shell script
Add a build dependency on roslint to your package's package.xml:


<build_depend>roslint</build_depend>
In your package's CMakeLists.txt file, include roslint as one of your catkin component dependencies:


find_package(catkin REQUIRED COMPONENTS roslint ...)
Then, invoke the roslint functions from your CMakeLists.txt, eg:


roslint_cpp()
If you'd like more control over what gets linted, you can specify the exact files:


roslint_cpp(src/foo.cpp src/bar.cpp src/baz.cpp)
```


```shell script
catkin build my_fancy_package --make-args roslint
```

## Debug




## References

- https://catkin-tools.readthedocs.io/en/latest/verbs/catkin_create.html
- http://fkie.github.io/catkin_lint/


Extra notes:

from xacros
- can remove line endings
- search for " \n
- eliminate line endings with [\\]$
- remove " from beginning and end
- format with alt shift I

group specified in semmantic description -> srdf?
