cmake_minimum_required(VERSION 2.8.3)
project(cpp_service_example)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++14)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

add_service_files(
  FILES
  AddTwoInts.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES class_design
    CATKIN_DEPENDS roscpp std_msgs message_runtime
#  DEPENDS system_lib
)

###########
## Build ##
###########
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
    #include
    ${catkin_INCLUDE_DIRS}
)


# add_executable(cpp_service_example   src/cpp_class_design_full.cpp
#                                     src/cpp_run_node_example.cpp)

# add_dependencies(cpp_service_example ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

# target_link_libraries(cpp_service_example
#   ${catkin_LIBRARIES}
# )

add_executable(cpp_service_server_example src/add_two_ints_server.cpp)
target_link_libraries(cpp_service_server_example ${catkin_LIBRARIES})
# add_dependencies(cpp_service_example beginner_tutorials_gencpp)

add_executable(cpp_service_client_example src/add_two_ints_client.cpp)
target_link_libraries(cpp_service_client_example ${catkin_LIBRARIES})
# add_dependencies(cpp_service_example beginner_tutorials_gencpp)