from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    listener_node = Node(
        package='python_pubsub_pkg',
        namespace='subscriber_member_function',
        executable='listener',
        name='listener'
    )
    
    return LaunchDescription([
    listener_node
    ])
    
    