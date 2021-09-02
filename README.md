# gRPC-ros-client 
- This is a ROS2 package which can subscribe to ROS2 topic and send gRPC request to gRPC servers, receive gRPC response and then publish back to the ROS2 node. 
<br/>
[![Docker GRPC server image](https://github.com/ipa-rar/gRPC-ros-bridge/actions/workflows/docker-server.yml/badge.svg)](https://github.com/ipa-rar/gRPC-ros-bridge/actions/workflows/docker-server.yml)
[![Docker GRPC-ROS image](https://github.com/ipa-rar/gRPC-ros-bridge/actions/workflows/docker-image.yml/badge.svg)](https://github.com/ipa-rar/gRPC-ros-bridge/actions/workflows/docker-image.yml)
<br/>
## Installation
- First, run the gRPC server and expose port 8061.
```
https://github.com/ipa-rar/gRPC-servers.git
cd gRPC-servers/demo_simple_communication/server
python3 server.py
```
- Build the workspace 
    - `colcon build --symlink-install`
    - `source instal/setup.bash`
- Then run the `generator.py` which is the fake data generator to test the client-server function. 
    - ``ros2 run grpc_ros_data_generator generator_node``
- Now start the grpc client node `grpc_client.py` to initiate the conversion of ROS msgs to proto msgs.
    - ``ros2 run grpc_ros_client grpc_client_node``


## To Do
- Write [unit tests](https://answers.ros.org/question/356180/ros2-creating-integration-tests-for-python-nodes/) for the nodes
- Fix communication issues in docker
- generalize the client 
