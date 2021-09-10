import random

import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor
from grpc_ros_interface.msg import BrokerRequest
from grpc_ros_interface.msg import BrokerResponse


class ClientPublisher(Node):
    """""
    Publishes 'BrokerRequest' to Topic 'grpc_request'
    0.1 sec interval publishing and QoS is 10 by default
    """""
    def __init__(self, topic='grpc_request', msg_type=BrokerRequest):
        super().__init__('data_publisher')
        self.pub = self.create_publisher(
            msg_type,
            topic,
            10)
        publish_rate = 0.5
        self.i = 0
        #self.timer = self.create_timer(publish_rate, self.publisher_cb)
        self.timer = self.create_timer(publish_rate, self.publisher_cb)

    def publisher_cb(self):
        msg = BrokerRequest()
        self.i += 1
        msg.id = self.i
        msg.sensor_1 = float(random.uniform(0, 1))
        msg.sensor_2 = float(random.uniform(0, 1))
        msg.sensor_3 = float(random.uniform(0, 1))
        msg.sensor_4 = float(random.uniform(0, 1))
        self.pub.publish(msg)
        #self.get_logger().info('Client streaming :| %d | %g | %g | %g | %g |' %
        #                       (msg.id, msg.sensor_1, msg.sensor_2, msg.sensor_3, msg.sensor_4))


class ClientSubscriber(Node):
    """""
    Subscribes 'BrokerResponse' from Topic 'broker_topic'
    as and when the message is available in the topic
    """""

    def __init__(self, topic='grpc_response', msg_type=BrokerResponse):
        super().__init__('data_subscriber')
        self.client_subsciber = self.create_subscription(
            msg_type,
            topic,
            self.subscriber_cb,
            10
        )

    def subscriber_cb(self, msg):
        self.get_logger().info('Client received:| %d | %r |' % (msg.id, msg.prediction))


def main(args=None):
    rclpy.init(args=args)
    try:
        client_publisher = ClientPublisher()
        client_subscriber = ClientSubscriber()

        executor = SingleThreadedExecutor()
        executor.add_node(client_publisher)
        executor.add_node(client_subscriber)
        try:
            executor.spin()
        finally:
            executor.shutdown()
            client_publisher.destroy_node()
            client_subscriber.destroy_node()

    except KeyboardInterrupt:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
