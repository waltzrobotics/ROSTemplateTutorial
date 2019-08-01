couple of examples

1. building of messages
2.  generation?
3.  consumption of messages in pub/sub


- something about needing message generation and runtime (builds and compiles the message types and stores them in devel?)
- best practices often suggest that the message types are stored in separate repository
- convention to use msg folder in src with extension .msg
- can use primative types and also make use of other existing message types (aggregate)

Make sure to source the environment after a build.
Using the below commands:

```
roscd message_example

rosmsg info basic_message
```

Should receive the following:

```
[message_example/basic_message]:
string basic_message_1
std_msgs/String basic_message_2
  string data
```


## Command Line Usage



### Other

```
rosmsg package message_example
```

```
message_example/basic_message
```

```
$ rosmsg --help

rosmsg is a command-line tool for displaying information about ROS Message types.

Commands:
        rosmsg show     Show message description
        rosmsg info     Alias for rosmsg show
        rosmsg list     List all messages
        rosmsg md5      Display message md5sum
        rosmsg package  List messages in a package
        rosmsg packages List packages that contain messages

Type rosmsg <command> -h for more detailed usage
```


## TODO / Issues

- Clean up documentation
- Message use example?
- Command line use example?