from setuptools import find_packages, setup

package_name = 'finalproject'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/f23_robotics_1_launch.py']))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/indoorworld.wbt', 
]))
data_files.append(('share/' + package_name + '/worlds', [
    'worlds/indoorworld.wbt', 
]))
data_files.append(('share/' + package_name + '/worlds', [
    'worlds/65ffe8d19b24fc7543c0d16db27253c6.jpg', 
]))
data_files.append(('share/' + package_name + '/worlds', [
    'worlds/others_0019_plane_600.png', 
]))
data_files.append(('share/' + package_name + '/worlds', [
    'worlds/Untitled.jpeg', 
]))
data_files.append(('share/' + package_name + '/protos', [
    'protos/Wall.proto', 
]))
data_files.append(('share/' + package_name + '/protos', [
    'protos/Roughcast.proto', 
]))
data_files.append(('share/' + package_name + '/protos', [
    'protos/OfficeChair.proto', 
]))
data_files.append(('share/' + package_name, ['package.xml']))
# data_files.append(('share/' + package_name + '/resource', [
#     'resource/turtlebot_webots.urdf',
#     'resource/ros2control.yml',
# ]))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='crolson1',
    maintainer_email='cooper@olsonville.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
