cmake_minimum_required(VERSION 3.0.2)
project(grpc_ros_data_generator)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  grpc_ros_interface
)

catkin_package(
  CATKIN_DEPENDS
  roscpp 
  grpc_ros_interface
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

