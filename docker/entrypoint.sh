#!/bin/bash
#!/bin/bash
set -e

source /opt/ros/foxy/setup.bash
source /home/ros2_ws/install/setup.bash

ros2 launch grpc_ros_bringup bringup.py