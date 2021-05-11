from setuptools import setup

package_name = 'grpc_ros_bridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ragesh',
    maintainer_email='ragesh.ramachandran.ipa.fraunhofer.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bridge = grpc_ros_bridge.grpc_bridge:main',
            'client_app = grpc_ros_bridge.client_node:main'
        ],
    },
)
