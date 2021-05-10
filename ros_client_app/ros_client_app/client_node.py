# Publishes  'BrokerRequest'
# to Topic 'broker_topic'
# 0.1 sec interval publishing
# QoS is 10 by default
import rclpy
from rclpy.node import Node 
from grpc_ros_interface.msg import BrokerRequest

class ClientPublisher(Node):
    def __init__(self):
        super().__init__('client_publisher')
        self.pub = self.create_publisher(
            BrokerRequest, 
            'broker_topic', 
            10)
        publish_rate = 0.05
        self.timer = self.create_timer(publish_rate, self.publisher_cb)

    def publisher_cb(self):
        msg = BrokerRequest()
        csv_filename = "../dataset/sensors.csv"
        with open(csv_filename, "r") as dataset:
            row = csv.reader(dataset, delimiter=",")
            for i, data in enumerate(row):
                msg.id=data[0]
                msg.sensor_1=data[1]
                msg.sensor_2=data[2]
                msg.sensor_3=data[3]
                msg.sensor_4=data[4]
                self.get_logger().info('publishing: "%d"'% msg.id)
                yield msg

def main(args=None):
    rclpy.init(args=args)
    try:
        client_publisher = ClientPublisher()
        rclpy.spin(client_publisher)
    except KeyboardInterrupt:
        client_publisher.destroy_node()
        rclpy.shutdown()

if __name__=='__main__':
    main()