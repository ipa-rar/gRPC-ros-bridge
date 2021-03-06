# Subscribes 'BrokerRequest'
# Publishes  'BrokerResponse'
# to Topic 'broker_topic'
# 0.1 sec interval publishing
# QoS is 10 by default
import grpc
import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor
# proto to ROS msg converted messages
from grpc_ros_interface.msg import BrokerRequest
from grpc_ros_interface.msg import BrokerResponse
# proto autogenerated messages for payload
from . import demo_pb2 as pb2
# # proto autogenerated messages for setting up communciation channel
from . import demo_pb2_grpc as pb2_grpc
PORT = 'simple_server_app:50051'
#PORT = 'localhost:50051'
class GrpcClient(Node):

    def __init__(self, 
                topic_sub='grpc_request', 
                topic_pub='grpc_response', 
                req_msg_type=BrokerRequest,
                res_msg_type=BrokerResponse):
        super().__init__('broker_service_request')
        """
        initializes the grpc communciation channel, 
        subscriber and publisher to/from ROS side
        """
        channel = grpc.insecure_channel(PORT)
        self.stub = pb2_grpc.BrokerServiceStub(channel)
        self.sub = self.create_subscription(
            req_msg_type,
            topic_sub,
            self.grpc_server_request,
            10
        )
        self.pub = self.create_publisher(
            res_msg_type,
            topic_pub,
            10
        )

    def grpc_server_request(self, msg):
        """
        This is a callback from the sub and publishes 
        the subscribed payload directly to the gRPC server.
        demo_pb2 module is used to publish the subscribed ROS msgs to server
        """
        # Send request payload as ROS msg
        request = pb2.BrokerRequest(
            id=int(msg.id),
            sensor1=float(msg.sensor1),
            sensor2=float(msg.sensor2),
            sensor3=float(msg.sensor3),
            sensor4=float(msg.sensor4))
        response = self.stub.SimpleMethod(request)
        # Convert the protobuff response payload to ROS msg
        self.msg = BrokerResponse()
        self.msg.id = response.id
        self.msg.prediction = response.prediction
        self.grpc_server_response(self.msg)

    def grpc_server_response(self, msg):
        """
        Publishes the gRPC server response to the ROS side
        """
        self.pub.publish(msg)

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