# ROS Class Design


- can be executed by launch file or rosrun

```shell script 
rosrun 
```

```shell script
roslaunch 
```

- class design layout of each
- discuss messages and types (briefly)
- python interpreted --> do not need explicit node start example file

This file is to outline the essential components for getting a ROS node setup that has been defined in a developed node object.  

Add more later.



- Make sure to mark python files as executable, otherwise ROS will not able to locate and execute them.

```shell script
sudo chmod +x python_file_name
```

```shell script
find . -name '*.cfg' | xargs chmod +x
```



- it is possible to target file extensions and update all files of that type recursively.
- configuration files, python files

