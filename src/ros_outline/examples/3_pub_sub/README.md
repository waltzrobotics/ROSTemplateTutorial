# ROS Pub / Sub

Can be done inside of a node design / class or in "script" fashion.

Python version is stock ros tutorial version without elaboration.
##



## Command Line

Start roscore and rosrun appropriate executables.

```
roscore
```


### Publish

```
rosrun pub_example pub_example 

rostopic list 

rostopic echo /simple_pub
```

```
linear: 
  x: 1.05935077884
  y: 0.0
  z: 0.0
angular: 
  x: 0.0
  y: 0.0
  z: -2.52867580276
---
```

#### Manual Publish

FIX : 

```
rostopic pub -1 /simple_pub geometry_msgs/Twist -- 0.0 0.0 0.0 
```

### Subscribe

```
rosrun sub_example sub_example 
```



## TODO / Issues

- Everything

## References
