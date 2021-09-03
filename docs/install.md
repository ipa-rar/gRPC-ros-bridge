# Installation
1.  Run the gRPC server and expose port 8061.
```
https://github.com/ipa-rar/gRPC-servers.git
cd gRPC-servers/demo_simple_communication/server
python3 server.py
```
2. Build the workspace 
    - `colcon build --symlink-install`
    - `source instal/setup.bash`
    
3. Then run the `generator.py` which is the fake data generator to test the client-server function. 
    - ``ros2 run grpc_ros_data_generator generator_node``

4. Now start the grpc client node `grpc_client.py` to initiate the conversion of ROS msgs to proto msgs.
    - ``ros2 run grpc_ros_client grpc_client_node``

