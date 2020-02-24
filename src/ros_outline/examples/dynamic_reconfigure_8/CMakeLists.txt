cmake_minimum_required(VERSION 2.8.3)
project(dynamic_reconfigure_8)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++14)

find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  roscpp
  rospy
)

#generate_dynamic_reconfigure_options(
#  cfg/example.cfg
#)

generate_dynamic_reconfigure_options(
  cfg/nodeExample.cfg
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES dynamic_reconfigure_8
  CATKIN_DEPENDS dynamic_reconfigure roscpp rospy
#  DEPENDS system_lib
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  # ${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake
)

add_executable( dyn_cfg_node   src/dyn_cfg_node.cpp )
target_link_libraries( dyn_cfg_node ${catkin_LIBRARIES} )
add_dependencies( dyn_cfg_node ${PROJECT_NAME}_gencfg )

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h"
)

install(TARGETS dyn_cfg_node
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

###################################
###################################
###################################


###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need

## Specify additional locations of header files
## Your package locations should be listed before other locations
#include_directories(
#    include
##    ${catkin_INCLUDE_DIRS}
#)

#add_dependencies(dyn_cfg_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

#target_link_libraries(dyn_cfg_node
#  ${catkin_LIBRARIES}
#)

# add dynamic reconfigure api
#rosbuild_find_ros_package(dynamic_reconfigure)
#include(${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake)
#gencfg()
#rosbuild_add_executable(dyn_cfg_node src/dyn_cfg_node.cpp)

#or if your ROS distribution is Groovy or higher use this:
#X . find_package(catkin REQUIRED COMPONENTS dynamic_reconfigure ) 
#X . generate_dynamic_reconfigure_options( cfg/MyStuff.cfg)  
#X . include_directories(${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake) 
#X . add_executable(dynamic_reconfigure_node src/dynamic_reconfigure_node.cpp)
#X . add_dependencies(dynamic_reconfigure_node ${PROJECT_NAME}_gencfg)
#X . target_link_libraries(dynamic_reconfigure_node ${catkin_LIBRARIES})

#add_dependencies(dyn_cfg_node dynamic_reconfigure_8_gencfg ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})