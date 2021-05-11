# Subscribes 'BrokerRequest'
# Publishes  'BrokerResponse'
# to Topic 'broker_topic'
# 0.1 sec interval publishing
# QoS is 10 by default
import grpc
import rclpy
from rclpy.node import Node

from grpc_ros_interface.msg import BrokerRequest
from grpc_ros_interface.msg import BrokerResponse

from . import broker_pb2 as pb2
from . import broker_pb2_grpc as pb2_grpc
port = 'localhost:8061'


class GrpcRosBridge(Node):

    def __init__(self):
        super().__init__('grpc_ros_bridge')

        channel = grpc.insecure_channel(port)
        self.stub = pb2_grpc.BrokerServiceStub(channel)
        self.client_subsciber = self.create_subscription(
            BrokerRequest,
            'broker_topic',
            self.subscribe_to_client,
            10
        )
        self.client_publisher = self.create_publisher(
            BrokerResponse,
            'broker_topic',
            10
        )

    def subscribe_to_client(self, msg):
        self.get_logger().info('Bridge listenes to : %d %g %g %g %g' %
                               (msg.id, msg.sensor_1, msg.sensor_2, msg.sensor_3, msg.sensor_4))
        request = pb2.BrokerRequest(
            id=int(msg.id),
            sensor1=float(msg.sensor_1),
            sensor2=float(msg.sensor_2),
            sensor3=float(msg.sensor_3),
            sensor4=float(msg.sensor_4))
        self.send_grpc_request(request)

    def send_grpc_request(self, request):
        response_iterator = self.stub.BidirectionalStreaming(request)
        self.get_grpc_response(response_iterator)

    def get_grpc_response(self, response_iterator):
        self.msg = BrokerResponse()
        for response in response_iterator:
            self.msg.id = response.id
            self.msg.prediction = response.prediction
            self.publish_to_client(self.msg)

    def publish_to_client(self, msg):
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    try:
        grpc_ros_bridge = GrpcRosBridge()
        rclpy.spin(grpc_ros_bridge)
    except KeyboardInterrupt:
        grpc_ros_bridge.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
