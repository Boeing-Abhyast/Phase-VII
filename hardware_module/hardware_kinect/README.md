# Setting Up Microsoft Kinect XBOX 360

A brief documentation on how to install the drivers for using [Microsoft Kinect XBOX 360](https://en.wikipedia.org/wiki/Kinect) sensor with [ROS Kinetic](http://wiki.ros.org/kinetic).

## Instructions

1. Installing dependencies:
```bash
sudo apt-get install g++ python libusb-1.0-0-dev freeglut3-dev
sudo apt-get install doxygen graphviz mono-complete
sudo apt-get install openjdk-8-jdk
```

2. Intalling OpenNI:
```bash
cd ~/
git clone https://github.com/OpenNI/OpenNI.git
cd OpenNI
cd Platform/Linux/CreateRedist
sudo chmod +x RedistMaker
./RedistMaker
cd ../Redist/OpenNI-Bin-Dev-Linux-[xxx]
sudo ./install.sh
```

3. Installing Kinect driver:
```bash
cd ~/
git clone git://github.com/ph4m/SensorKinect.git
cd SensorKinect/Platform/Linux/CreateRedist
sudo chmod +x RedistMaker
./RedistMaker
cd ../Redist/Sensor-Bin-Linux-x64-v*
sudo ./install.sh
```

__NOTE:__ To test whether the driver is correctly installed or not, run: `~/OpenNI/Platform/Linux/Bin/x64-Release/Sample-NiSimpleViewer`

4. Install [freenect_launch](http://wiki.ros.org/freenect_launch) which includes launch files to open an OpenNI device:
```bash
sudo apt-get install ros-kinetic-freenect-camera ros-kinetic-freenect-launch
```

5. Running Kinect on ROS:
```bash
roslaunch freenect_launch freenect.launch depth_registered:=true
```

6. Setup [tf](http://wiki.ros.org/tf) tree to visualize the point cloud on rviz:
```bash
rosrun tf static_transform_publisher 0 0 0 0 0 0 0 chassis camera_rgb_frame 10
rosrun tf static_transform_publisher 0 0 0 0 0 0 1 camera_rgb_frame camera_rgb_optical_frame 10
rosrun tf static_transform_publisher 0 0 0 0 0 0 1 camera_depth_frame camera_depth_optical_frame 10
```

7. Open [rviz](http://wiki.ros.org/rviz) to visualize the point cloud
```bash
rosrun rviz rviz
```

## Running Kinect with *Alpha*

Run the following command to visualize the kinect data using rviz:
```
roslaunch hardware_kinect kinect360_rviz.launch
```

## Calibrating the Kinect sensor

In order to calibrate the sensor, follow the instructions available [here](http://wiki.ros.org/openni_launch/Tutorials/IntrinsicCalibration).
