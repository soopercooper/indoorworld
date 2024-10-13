How to run package: <br/>
source /opt/ros/humble/setup.bash<br/>
export WEBOTS_HOME=/usr/local/webots<br/>
source install/local_setup.bash<br/>
colcon build<br/>
ros2 launch finalproject f23_robotics_1_launch.py<br/>
<br/>
Doors can be opened/closed by changing position value in proto from 0 to 1.5
