from grpc_ros_client.grpc_client import GrpcClient
import pytest
import rclpy
from grpc_ros_interface.msg import BrokerRequest
from grpc_ros_interface.msg import BrokerResponse


# fixture: helper code that should run before any tests are executed
@pytest.fixture(scope='session', autouse=True)
def setup_ros():
    rclpy.init()

def setup_grpc_client():
    client = GrpcClient()
    return client

def test_grpc_client():
    client = setup_grpc_client()
    assert client.pub.topic_name == "/grpc_response"
    assert client.sub.topic_name == "/grpc_request"
    assert client.pub.msg_type == BrokerResponse
    assert client.sub.msg_type == BrokerRequest
