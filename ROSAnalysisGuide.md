# ROS Analysis / Debug Guide

This guide was built as an aid for analysis and uses ROS template as the example platform (only command line).

TODO: outline rqt and plugins

## pub_example1.py

This file initializes a topic_name of a specific type String.
Initializes anonymous node named 'talker.'
Publish at specified rate with specific type String.

## sub_example1.py

Initializes anonymous node 'listener'
Subscribes to topic 'chatter' expecting specific type String.
Set node to continue until shutdown.

## Command line tools

### rosnode


Key tools: list, info, machine

- rosnode list - explore active nodes observed by roscore

```shell
$rosnode list
    /listener_653_1534859081630
    /rosout
    /talker_690_1534859084201
```

- rosnode info - detailed information about a particular node

```shell
$rosnode info /talker_690_1534859084201 

Node [/talker_690_1534859084201]
Publications: 
 * /chatter [std_msgs/String]
 * /rosout [rosgraph_msgs/Log]

Subscriptions: None

Services: 
 * /talker_690_1534859084201/get_loggers
 * /talker_690_1534859084201/set_logger_level


contacting node http://wwaltz:46555/ ...
Pid: 690
Connections:
 * topic: /chatter
    * to: /listener_653_1534859081630
    * direction: outbound
    * tra
 * topic: /rosout
    * to: /rosout
    * direction: outbound
    * transport: TCPROS

```

- rosnode machine - identify nodes operating on particular machine

```shell
$rosnode machine wwaltz
    /listener_653_1534859081630
    /rosout
    /talker_690_1534859084201
```

### rostopic

Key tools:  list, bw, hz, type, pub, find

- rostopic list - comprehensive list of all active topics

```shell
$rostopic list
    /chatter
    /rosout
    /rosout_agg
```

- rostopic bw /chatter - estimated bandwidth consumed by topic /chatter

```shell
$rostopic bw /chatter
    subscribed to [/chatter]
    average: 296.23B/s
        mean: 29.00B min: 29.00B max: 29.00B window: 10
    average: 292.91B/s
        mean: 29.00B min: 29.00B max: 29.00B window: 20
    average: 291.82B/s
        mean: 29.00B min: 29.00B max: 29.00B window: 30
    average: 291.28B/s
```

- rostopic hz /chatter - estimated frequency of topic /chatter

```shell
$rostopic hz /chatter 
    subscribed to [/chatter]
    average rate: 10.002
        min: 0.100s max: 0.100s std dev: 0.00025s window: 10
    average rate: 10.000
        min: 0.100s max: 0.100s std dev: 0.00020s window: 20
    average rate: 10.000
        min: 0.100s max: 0.100s std dev: 0.00018s window: 30
```

- rostopic type - identify the message type of a particular topic

```shell
$rostopic type /chatter
    std_msgs/String
```

- rostopic pub - publish a message on a particular topic.  Can set parameters on number and/or frequency of publish.

```shell
$rostopic pub /chatter std_msgs/String 'testing'
    publishing and latching message. Press ctrl-C to terminate
```

- rostopic find - seek a topic with a particular type

```shell
$rostopic find std_msgs/String 
    /chatter
```

### rosmsg

Key tools: show

```shell
$rosmsg show std_msgs/String
    string data
```

### rosparam

Key tools: list, set, get

- rosparam list - list out all parameters on server

```shell
$rosparam list
    /rosdistro
    /roslaunch/uris/host_wwaltz__45149
    /rosversion
    /run_id
```

- rosparam set - set a parameter on the server

```shell
$rosparam set /new_param "0"
```

Verify parameter using list:

```shell
$rosparam list
    /new_param
    /rosdistro
    /roslaunch/uris/host_wwaltz__45149
    /rosversion
    /run_id
```

- rosparam get - retrieve a parameter from the server

```shell
$rosparam get /new_param
    0
```

### rosdep and rospack

Information regarding packages and dependencies.
Key tools:  check, depends, depends1, 

- rosdep check - checks package for dependencies and if they are installed

```shell
$rosdep check publish_template
```

- rospack depends - lists dependencies of package (depends1 shows only first level)

```shell
$rospack depends publish_template
    cpp_common
    rostime
    roscpp_traits
    roscpp_serialization
    catkin
    genmsg
    genpy
    message_runtime
    gencpp
    geneus
    gennodejs
    genlisp
    message_generation
    rosbuild
    rosconsole
    std_msgs
    rosgraph_msgs
    xmlrpcpp
    roscpp
    rosgraph
    ros_environment
    rospack
    roslib
    rospy
```

### misc tools

TODO: Need to cover roslog and rosbag

## GUI tools

rqt_graph (plots nodes, topics)

rqt_plot (need numerical data -- return to this)
