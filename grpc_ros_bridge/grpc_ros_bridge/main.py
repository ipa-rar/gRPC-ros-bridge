# Subscribes 'BrokerRequest'
# Publishes  'BrokerResponse'
# to Topic 'broker_topic'
# 0.1 sec interval publishing
# QoS is 10 by default
import rclpy
from . import grpc_bridge as GrpcRosBridge

def main(args=None):
    rclpy.init(args=args)
    try:
        grpc_ros_bridge = g.GrpcRosBridge()
        rclpy.spin(grpc_ros_bridge)
    except KeyboardInterrupt:
        grpc_ros_bridge.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()