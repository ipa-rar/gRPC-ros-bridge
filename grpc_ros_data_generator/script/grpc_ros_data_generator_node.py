#!/usr/bin/env python3

import rospy
import random
from grpc_ros_interface.msg import BrokerRequest
from grpc_ros_interface.msg import BrokerResponse


class ClientPubSub(object):
 
    def __init__(self, pub_topic='grpc_request', 
                    sub_topic='grpc_response', 
                    pub_msg_type=BrokerRequest, 
                    sub_msg_type=BrokerResponse):

        self.client_pub = rospy.Publisher(pub_topic, pub_msg_type, queue_size=10)
        self.client_sub = rospy.Subscriber(sub_topic, sub_msg_type, self.subscriber_cb)
        self.i = 0
        
    def publisher_cb(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            msg = BrokerRequest()
            self.i += 1
            msg.id = self.i
            msg.sensor1 = float(random.uniform(0, 1))
            msg.sensor2 = float(random.uniform(0, 1))
            msg.sensor3 = float(random.uniform(0, 1))
            msg.sensor4 = float(random.uniform(0, 1))
            #rospy.loginfo("Payload: {0} ,{1}, {2}, {3}, {4}" .format(msg.id, msg.sensor1, msg.sensor2, msg.sensor3, msg.sensor4))
            self.client_pub.publish(msg)
            rate.sleep()

    def subscriber_cb(self, msg):
        rospy.loginfo("Reponse {0}, {1}".format(msg.id, msg.prediction))


def main():
    rospy.init_node('data_publisher')
    client_pub_sub = ClientPubSub()
    try:
        client_pub_sub.publisher_cb()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.logerr("ROS Interrupt Exception! Just ignore the exception!")




if __name__ == '__main__':
    main()