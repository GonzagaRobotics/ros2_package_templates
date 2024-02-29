from launch import LaunchDescription
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    talker_node = Node(
        package='cpp_pubsub_pkg',
        namespace='publisher_member_function',
        executable='talker',
        name='talker'
    )
    
    return LaunchDescription([
    talker_node
    ])