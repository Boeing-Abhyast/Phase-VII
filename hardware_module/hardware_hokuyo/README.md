# Setting Up Hokuyo URG-04LX-UG01

A brief documentation on how to install the drivers for using [Hokuyo URG-04LX-UG01](https://www.hokuyo-aut.jp/search/single.php?serial=166) sensor with [ROS Kinetic](http://wiki.ros.org/kinetic).

## Instructions

1. Installing the [urg_node](http://wiki.ros.org/urg_node):
```bash
sudo apt-get install ros-kinetic-urg-node
```

2. Configuring the Hokuyo sensor:
    1. Check the permissions of the Hokuyo: `ls -l /dev/ttyACM0`. The output would be of form:
        ```bash
        crw-[XX]---- 1 root dialout 166, 0 Oct 28 22:12 /dev/ttyACM0
        ```
    2. If `[XX] = rw`, then the laser is configured properly, else run `sudo chmod a+rw /dev/ttyACM0` to change the permissions.

    3. Checking if device has been setup properly with ROS:
        ```bash
        rosrun urg_node getID /dev/ttyACM0
        ```
        __NOTE:__ The output: `Device at /dev/ttyACM0 has ID H0807228` means that the sensor is configured correctly.

3. Running Hokuyo on ROS:
```
roscore & rosrun urg_node urg_node
```

4. Setup [tf](http://wiki.ros.org/tf) tree to visualize the laser scan on rviz:
```bash
rosrun tf static_transform_publisher 0 0 0 0 0 0 1 chassis laser 10  
```

5. Open [rviz](http://wiki.ros.org/rviz) to visualize the laser scan
```bash
rosrun rviz rviz
```

## Running Hokuyo with *Alpha*

Run the following command to visualize the hokuyo data using rviz:
```
roslaunch hardware_hokuyo urg04lx_rviz.launch
```
