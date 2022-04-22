# How to build 3iRobotics lidar ros package:
1. Clone this project to your catkin's workspace src folder
2. Please select correct serial in “src\node.cpp”：/dev/ttyUSB0(default)
3. cd catkin
4. catkin_make (to build delta_lidar_node and delta_lidar_node_client)
5. source devel/setup.bash
6. sudo chmod 777 /dev/ttyUSB0
7. Open new Termial: roscore

# How to run 3iRobotics lidar ros package:

## run publish_node:
    rosrun delta_lidar delta_lidar_node or roslaunch  delta_lidar delta_lidar.launch(NOTE:please select correct serial in “launch\delta_lidar.launch”)
## run subscribe_node:
    1.Open new Termial: source devel/setup.bash
    2.rosrun delta_lidar delta_lidar_node_client
## How to run 3iRobotics lidar rviz:
    roslaunch  delta_lidar view_delta_lidar.launch


