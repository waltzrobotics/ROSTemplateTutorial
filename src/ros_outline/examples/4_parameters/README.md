

many ways to load parameters 

get references

by application 

get exmaples of monitoring (or services that set / get parameters)

cover remapping here

<launch>
<rosparam command="load" file="$(find example_parameter_server)/launch/jnt1_gains.yaml" />
</launch>


  
joint1_gains: {p: 7.0, i: 8.0, d: 9.0}