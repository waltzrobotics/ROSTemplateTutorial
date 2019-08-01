

- set/get through launch file
- set/get through command line
- code

- search strings? maps?


many ways to load parameters 

get references

by application 

get exmaples of monitoring (or services that set / get parameters)

cover remapping here

<launch>
<rosparam command="load" file="$(find example_parameter_server)/launch/jnt1_gains.yaml" />
</launch>


  
joint1_gains: {p: 7.0, i: 8.0, d: 9.0}



Command line entries:

```
rosparam list

rosparam get /parameter_name

rosparam set /parameter_name <type> <value>

rosparam set /parameter_name /std_msgs <value>
```

Use within node:


### TODO / Issues

- what is standard operation for changing parameters at run-time?
- how are arguments handled during reconfigure / launch
- 



## Reference 