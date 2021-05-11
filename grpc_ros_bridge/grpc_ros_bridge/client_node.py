# Publishes  'BrokerRequest'
# to Topic 'broker_topic'
# 0.1 sec interval publishing
# QoS is 10 by default
import rclpy
from rclpy.node import Node
from grpc_ros_interface.msg import BrokerRequest
import csv
import random


class ClientPublisher(Node):

    def __init__(self):
        super().__init__('client_publisher')
        csv_filename = "src/grpc_ros_bridge/dataset/sensors.csv"
        dataset = open(csv_filename, "r")
        self.row = csv.reader(dataset, delimiter=",")
        self.pub = self.create_publisher(
            BrokerRequest,
            'broker_topic',
            10)
        publish_rate = 0.5
        #self.timer = self.create_timer(publish_rate, self.publisher_cb)
        self.timer = self.create_timer(publish_rate, self.fake_publisher_cb)

    def fake_publisher_cb(self):
        msg = BrokerRequest()
        msg.id = random.randint(0, 9)
        msg.sensor_1 = random.random()
        msg.sensor_2 = random.random()
        msg.sensor_3 = random.random()
        msg.sensor_4 = random.random()
        self.pub.publish(msg)
        self.get_logger().info('Client publishing : %d %g %g %g %g' %
                               (msg.id, msg.sensor_1, msg.sensor_2, msg.sensor_3, msg.sensor_4))

    def publisher_cb(self):
        msg = BrokerRequest()
        for i, data in enumerate(self.row):
            msg.id = int(data[0])
            msg.sensor_1 = float(data[1])
            msg.sensor_2 = float(data[2])
            msg.sensor_3 = float(data[3])
            msg.sensor_4 = float(data[4])
            self.pub.publish(msg)
            self.get_logger().info('Client publishing : %d %g %g %g %g' %
                                   (msg.id, msg.sensor_1, msg.sensor_2, msg.sensor_3, msg.sensor_4))


def main(args=None):
    rclpy.init(args=args)
    try:
        client_publisher = ClientPublisher()
        rclpy.spin(client_publisher)
    except KeyboardInterrupt:
        client_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
