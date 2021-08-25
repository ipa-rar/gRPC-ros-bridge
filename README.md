# gRPC-ros-bridge 
- This is a ROS2 package which can subscribe to ROS2 topic and send gRPC request to gRPC servers, receive gRPC response and then publish back to the ROS2 node.

## Starting up
- First, run the gRPC server and expose port 8061.
- Build the workspace 
    - `colcon build`
    - `source instal/setup.bash`
- Then run the `client_node.py` which is the client that sends request to the server using the ROS-gRPC bridge.
    - ``ros2 run grpc_ros_bridge client_node``
- Now start the bridge node `broker_bridge.py` to initiate the conversion of ROS msgs to proto msgs.
    - ``ros2 run grpc_ros_bridge broker_bridge``

## To dos

- sending req from subscribed ROS topic
- Reciving the response and publishing back to the ROS topic

## Troubleshooting
Check all open ports to see the connection status
```
netstat -atun  | grep '8061
```
```
tcp6       0      0 127.0.0.1:8061          :::*                    LISTEN     
tcp6       0      0 127.0.0.1:42186         127.0.0.1:8061          ESTABLISHED
tcp6       0      0 127.0.0.1:8061          127.0.0.1:42186         ESTABLISHED
```