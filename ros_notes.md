# Additional ROS Notes




## Checking Dependencies and Installs for ROS Packages

The --from-paths option indicates we want to install the dependencies for an entire directory of packages, in this case src. The --ignore-src option indicates to rosdep that it shouldn't try to install any ROS packages in the src folder from the package manager, we don't need it to since we are building them ourselves. The --rosdistro option is required because we don't have a ROS environment setup yet, so we have to indicate to rosdep what version of ROS we are building for. The -y option indicates to rosdep that we don't want to be bothered by too many prompts from the package manager. After a while (and maybe some prompts for your password) rosdep will finish installing system dependencies and you can continue. The -r flag causes rosdep to ignore minor errors. This is necessary to get the base dependencies installed. After the packages following this section have been installed it would be a good idea to run this command again without the -r to see if there are any dependencies that you forgot or didn't have in your base system (i.e. packages different from what the author of this tutorial had installed). The --os flag was necessary for the author because of differences in the way that the wheezy version of debian stores version information and what rosdep is expecting. If you are having trouble with any of the dependencies rosdep is supposed to get, make sure that you have the package name right by getting the rosdep base.yaml from this http://docs.ros.org/independent/api/rosdep/html/contributing_rules.html

Rosdep verbs and options can be found in [2].

### Checking Through Simulation

```
rosdep install --simulate --from-paths ~/workspaces/project/src --ignore-src
```

## Creating Packages with Catkin

Using references [4], [5], and [6] combine to provide instrution on creating ros catkin packages with prior identified dependencies.

[5] has practical information regarding development and is applied to actual hardware.
[6] is an excellent overall resource for ros development.

## Chaining Ros Launches

Using the include tag, link to another launch file to simplify.  

Example:

```
  <include file="$(find ur_gazebo)/launch/controller_utils.launch"/>
```

### Attributes for Reference

```
file="$(find pkg-name)/path/filename.xml"

Name of file to include.
ns="foo" (optional)

Import the file relative to the 'foo' namespace.
clear_params="true|false" (optional Default: false)

Delete all parameters in the <include>'s namespace before launch. This feature is very dangerous and should be used with caution. ns must be specified. Default: false.

pass_all_args="true|false" (optional Default: false) (New in Indigo and Jade as of roslaunch version 1.11.17)

If true, then all args set in the current context are added to the child context that is created for processing the included file. You can do this instead of explicitly listing each argument that you want to pass down.
```

## Kinematics

ur_

## Supressing Error from MoveIT

Edit planning scene monitor to suppress warnings about complete state of an object.

```
/home/wwaltz/workspaces_catkin/moveit_ws/src/moveit/moveit_ros/planning/planning_scene_monitor/src
```

## Misc

Add rviz to launch file:

```
<node type="rviz" name="rviz" pkg="rviz" args="-d $(find package_name)/rviz/config_file.rviz" />
```

Extending catkin workspace (must be in workspace).  Can chain several workspaces together.

```
catkin config --extend <<devel folder location of desired workspace>>
```

## References

- [1] http://answers.ros.org/question/251732/how-can-generate-a-list-of-dependencies-from-the-src-folder-of-a-workspace/
- [2] https://docs.ros.org/independent/api/rosdep/html/commands.html
- [3] https://erlerobotics.gitbooks.io/erle-robotics-erle-brain-a-linux-brain-for-drones/en/ros/tutorials/rosinstall.html
- [4] https://catkin-tools.readthedocs.io/en/latest/verbs/catkin_create.html
- [5] https://erlerobot.github.io/erle_gitbook/en/ros/tutorials/creating_a_ros_package.html
- [6] https://industrial-training-master.readthedocs.io/en/melodic/_source/session1/Creating-a-ROS-Package-and-Node.html
- [7] https://industrial-training-master.readthedocs.io/en/melodic/_source/session1/Creating-a-ROS-Package-and-Node.html
- [8] http://wiki.ros.org/roslaunch/XML/include