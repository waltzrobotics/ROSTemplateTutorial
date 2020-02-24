# ROS Tutorial

This project is created to serve as yet another ROS starting point.  This tutorial has the following requirements:

1. Ubuntu 16.04
2. ROS Kinetic

```shell script
docker run -it --rm -v /media/wwaltz/ISA-Work/_external_only/personal/repositories/ROSTemplateTutorial:/home/wwaltz/work --net=host --name waltz1 waltz:base
docker run -it --rm -v /home/wwaltz/hdd/projections/ros_development/ROSTemplateTutorial_copied:/home/wwaltz/work --net=host --name waltz1 waltz:base


```

## Preparation

1. Clone repository
2. Build
3. a. Put //project_root/devel/setup.bash into .bashrc OR (where //project_root/ is the location of the project)
    b. source //project_root/devel/setup.bash each time

## Steps

1. Open terminal and run: roscore
2. Open terminal and run: rosrun publish_template pub_example1

## Recall

rosrun <package_name> <script>


## Development Environment

```shell
ln -s /home/wwaltz/hdd/projects/ros_development/ROSTemplateTutorial/src/ros_outline/examples/8_dynamic_reconfigure /home/wwaltz/test_ws/src/
ln -s /home/wwaltz/hdd/projects/ros_development/ROSTemplateTutorial/src/ros_outline/examples/dynamic_reconfigure_8 /home/wwaltz/test_ws/src/
```


## References

## TODO

- [ ] Symlink arduino nodes to project
- [ ] Update readme
