from launch import LaunchDescription
from launch_ros.actions import Node
    
def generate_launch_description():
    ld = LaunchDescription()

    data_generator_node = Node(
        package="grpc_ros_data_generator",
        executable="generator_node"
    )
    
    grpc_client_node = Node(
        package="grpc_ros_client",
        executable="grpc_client_node"
    )
    
    ld.add_action(data_generator_node)
    ld.add_action(grpc_client_node)

    return ld
