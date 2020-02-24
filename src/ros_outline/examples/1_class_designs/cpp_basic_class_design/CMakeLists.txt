cmake_minimum_required(VERSION 2.8.3)
project(basic_class_design)

add_compile_options(-std=c++14)

find_package(catkin REQUIRED)

find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs geometry_msgs)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES class_design
    CATKIN_DEPENDS roscpp std_msgs geometry_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
    include
    ${catkin_INCLUDE_DIRS}
)


add_executable(basic_class_design   src/cpp_class_design_full.cpp
                                    src/cpp_run_node_example.cpp
                                    include/cpp_class.h)

add_dependencies(basic_class_design ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(basic_class_design
  ${catkin_LIBRARIES}
)

