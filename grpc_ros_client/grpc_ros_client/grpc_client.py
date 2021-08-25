# Subscribes 'BrokerRequest'
# Publishes  'BrokerResponse'
# to Topic 'broker_topic'
# 0.1 sec interval publishing
# QoS is 10 by default

import grpc
import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor

from grpc_ros_interface.msg import BrokerRequest
from grpc_ros_interface.msg import BrokerResponse

from . import demo_pb2 as pb2
from . import demo_pb2_grpc as pb2_grpc
port = 'localhost:8061'


class GrpcClient(Node):

    def __init__(self, topic='request_topic', msg_type=BrokerRequest):
        super().__init__('broker_service_request')
        channel = grpc.insecure_channel(port)
        self.stub = pb2_grpc.BrokerServiceStub(channel)
        self.data_subscriber = self.create_subscription(
            msg_type,
            topic,
            self.publish_to_grpc_server,
            10
        )
        self.data_publisher = self.create_publisher(
            BrokerResponse,
            'response_topic',
            10
        )

    def publish_to_grpc_server(self, msg):
        self.get_logger().info('gRPC client publishes : %d %g %g %g %g' %
                               (msg.id, msg.sensor_1, msg.sensor_2, msg.sensor_3, msg.sensor_4))
        # Send request payload as ROS msg
        request = pb2.BrokerRequest(
            id=int(msg.id),
            sensor1=float(msg.sensor_1),
            sensor2=float(msg.sensor_2),
            sensor3=float(msg.sensor_3),
            sensor4=float(msg.sensor_4))
        response = self.stub.SimpleMethod(request)

        # Convert the protobuff response payload to ROS msg
        self.msg = BrokerResponse()
        self.msg.id = response.id
        self.msg.prediction = response.prediction
        self.subscribe_grpc_server(self.msg)

    def subscribe_grpc_server(self, msg):
        self.data_publisher.publish(msg)
        self.get_logger().info('Server response payload: %d, %r' %
                               (self.msg.id, self.msg.prediction))


def main(args=None):
    rclpy.init(args=args)
    try:
        grpc_client = GrpcClient()
        executor = SingleThreadedExecutor()
        executor.add_node(grpc_client)
        try:
            executor.spin()
        finally:
            executor.shutdown()
            grpc_client.destroy_node()

    except KeyboardInterrupt:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
