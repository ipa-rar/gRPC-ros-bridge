cmake_minimum_required(VERSION 3.0.2)
project(grpc_ros_client)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_package(
 rospy
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
