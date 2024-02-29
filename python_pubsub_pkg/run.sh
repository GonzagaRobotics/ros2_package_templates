colcon build --packages-select python_pubsub_pkg
source install/setup.bash
ros2 launch python_pubsub_pkg both.launch.py
