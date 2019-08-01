

1. Upload Arduino sketch containing ROS components.

2. Make sure to have roscore running:

```shell
roscore
```

3. Launch ROS serial node using

```shell
rosrun rosserial_python serial_node.py /dev/ttyACM0 _baud:=115200
```

References:

- http://wiki.ros.org/rosserial
- http://wiki.ros.org/rosserial_arduino
- https://github.com/ros-drivers/rosserial