cmake_minimum_required(VERSION 3.0.2)
project(grpc_ros_interface)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  std_msgs
)
## Generate messages in the 'msg' folder
add_message_files(
   FILES
   BrokerRequest.msg
   BrokerResponse.msg
 )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )

## CATKIN_DEPENDS: catkin_packages dependent projects also need
catkin_package(
  CATKIN_DEPENDS 
  message_generation 
  roscpp 
  rospy 
  std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)