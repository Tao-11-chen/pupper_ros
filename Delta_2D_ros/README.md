# How to build 3iRobotics lidar ros package:
1. select correct serial in “src\node.cpp”：/dev/ttyUSB0(default)
2. sudo chmod 777 /dev/ttyUSB0


# How to run 3iRobotics lidar ros package:

## run publish_node:
    rosrun delta_lidar delta_lidar_node 
    or 
    roslaunch  delta_lidar delta_lidar.launch
## run subscribe_node:
    Open new Termial: 
    source devel/setup.bash
    rosrun delta_lidar delta_lidar_node_client
## How to run 3iRobotics lidar rviz:
    roslaunch  delta_lidar view_delta_lidar.launch


