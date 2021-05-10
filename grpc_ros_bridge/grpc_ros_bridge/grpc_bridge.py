import grpc
import rclpy
from rclpy.node import Node 

from grpc_ros_interface.msg import BrokerRequest
from grpc_ros_interface.msg import BrokerResponse

from .generated import broker_pb2 as pb2
from .generated import broker_pb2_grpc as pb2_grpc
port = 'localhost:8061'

class GrpcRosBridge(Node):
    def __init__(self):
        super().__init__('grpc_ros_bridge')

        self.channel = grpc.insecure_channel(port)
        self.stub = Client.BrokerServiceStub(channel)
        self.client_subsciber  = self.create_subscription(
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
        self.publish_rate = 0.1
        self.timer = self.create_timer(self.publish_rate, self.publish_to_client)

  
    
    def subscribe_to_client(self, msg):
        self.get_logger().info(msg.id, msg.sensor_1, msg.sensor_2, msg.sensor_3, msg.sensor_4)
        request = pb2.BrokerRequest()
        request.id = msg.id
        request.sensor1 = msg.sensor_1
        request.sensor2 = msg.sensor_2
        request.sensor3 = msg.sensor_3
        request.sensor4 = msg.sensor_4
        self.send_grpc_request(request)


    def send_grpc_request(self, request):
        request_iterator = self.stub.BidirectionalStreaming(request)
            

    def get_grpc_response(self):
        response = pb2.BrokerResponse()
        msg = BrokerResponse()
        msg.id = response.id
        msg.prediction = response.prediction
        return msg

    def publish_to_client(self, msg):
        msg = self.get_grpc_response()
        self.pub.publish(msg)