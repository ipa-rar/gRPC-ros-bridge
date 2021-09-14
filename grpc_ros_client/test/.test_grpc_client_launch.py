import launch
import launch_ros
import launch_ros.actions
import launch_testing.actions

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.actions import LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir

import pytest
import unittest

import rclpy

import std_msgs.msg
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory


@pytest.mark.rostest
def generate_test_description():
    """Launch the example.launch.py launch file."""
    return LaunchDescription([
        LogInfo(msg=[
            'Including launch file located at: ', get_package_share_directory('grpc_ros_bringup'), '/bringup_client.py'
        ]),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('grpc_ros_bringup'), '/bringup_client.py']),
            launch_arguments={'node_prefix': 'FOO'}.items(),
        ),
        launch_testing.actions.ReadyToTest(),
    ])

class TestTalkerListenerLink(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        rclpy.init()
       
    @classmethod
    def tearDownClass(cls):
        # Shutdown the ROS context
        rclpy.shutdown()

    def test_talker_talks(self, proc_output):
        proc_output.assertWaitFor(
        process='talker',
        expected_output="Publishing: \"Hello World: 1\"",
        timeout=5.0
    )
 
    def test_listener_hears(self, proc_output):
        proc_output.assertWaitFor(
        process='talker',
        expected_output='I heard: [Hello World: A]',
        # expected_output='I heard: [Hello World: 3]',
        timeout=5.0,
    )
