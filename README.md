How to run package:
source /opt/ros/humble/setup.bash
export WEBOTS_HOME=/usr/local/webots
source install/local_setup.bash
colcon build
ros2 launch finalproject f23_robotics_1_launch.py
