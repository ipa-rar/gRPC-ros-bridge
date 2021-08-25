# Subscribes 'BrokerRequest'
# Publishes  'BrokerResponse'
# to Topic 'broker_topic'
# 0.1 sec interval publishing
# QoS is 10 by default
# py /home/edge/workspace/gRPC-ws/insecure_bidirection_databroker/server/server.py

import grpc
import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor

from grpc_ros_interface.msg import BrokerRequest
from grpc_ros_interface.msg import BrokerResponse

from . import databroker_pb2 as pb2
from . import databroker_pb2_grpc as pb2_grpc
port = 'localhost:8061'

# Demo using this class
class GrpcRequestPublisher(Node):

    def __init__(self, topic= 'request_topic', msg_type=BrokerRequest):
        super().__init__('request_topic')
        channel = grpc.insecure_channel(port)
        self.stub = pb2_grpc.BrokerServiceStub(channel)
        self.client_subsciber = self.create_subscription(
            msg_type,
            topic,
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

        """ 
        This introduces an error
        - On every new msg arrived in the /request_topic this callback function gets called. 
        - At the same time the request is send to the server 
        - But this will not produce the desired results
        - We want the subscription call back fun to be called by the request sending function that sends each msg arrived
        - Instead of calling the request sending function on every callback 
        """    
        response_iterator = self.stub.BidirectionalStreaming(request)
        self.msg = BrokerResponse()
        for response in response_iterator:
            self.msg.id = response.id
            self.msg.prediction = response.prediction
            print("Server response: ", int(msg.id),
                 bool(msg.prediction))


# This is not implemented yet
class GrpcResponseSubscriber(Node):
    def __init__(self):
        super().__init__('response_topic')
        self.client_publisher = self.create_publisher(
            BrokerResponse,
            'broker_topic',
            10
        )

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
        grpc_request_publisher = GrpcRequestPublisher()
        #grpc_response_subscriber = GrpcResponseSubscriber()
        executor = SingleThreadedExecutor()
        executor.add_node(grpc_request_publisher)
        #executor.add_node(grpc_response_subscriber)
        try:
            executor.spin()
        finally:
            executor.shutdown()
            grpc_request_publisher.destroy_node()
           # grpc_response_subscriber.destroy_node()
    
    except KeyboardInterrupt:
        rclpy.shutdown()

if __name__ == '__main__':
    main()

