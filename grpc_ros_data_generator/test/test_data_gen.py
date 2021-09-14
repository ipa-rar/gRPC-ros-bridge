from grpc_ros_data_generator.grpc_ros_data_generator.generator import ClientPublisher, ClientSubscriber
import pytest
import rclpy

from grpc_ros_interface.msg import BrokerRequest
from grpc_ros_interface.msg import BrokerResponse

# fixture: helper code that should run before any tests are executed
@pytest.fixture(scope='session', autouse=True)
def setup_ros():
    rclpy.init()

def setup_publisher():
    pub = ClientPublisher()
    return sub

def setup_subscriber():
    sub  = ClientSubscriber()
    return sub

def test_data_gen():
    pub = setup_publisher()
    assert pub.client_pub.topic_name == "/grpc_request"
    assert sub.client_sub.topic_name == "/grpc_response"
    assert pub.client_pub.msg_type == BrokerRequest
    assert sub.client_sub.msg_type == BrokerResponse
