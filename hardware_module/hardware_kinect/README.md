# Kinect XBOX 360

A brief documentation on how to install the drivers for using [Microsoft Kinect XBOX 360](https://en.wikipedia.org/wiki/Kinect) camera with [ROS Kinetic](http://wiki.ros.org/kinetic).

## Instructions

1. Installing dependencies:
```bash
sudo apt-get install g++ python libusb-1.0-0-dev freeglut3-dev
sudo apt-get install doxygen graphviz mono-complete
sudo apt-get install openjdk-7-jdk
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

3. Installing Kinect driver
```bash
cd ~/
git clone git://github.com/ph4m/SensorKinect.git
cd SensorKinect/Platform/Linux/CreateRedist
sudo chmod +x RedistMaker
./RedistMaker
cd ../Redist/Sensor-Bin-Linux-x64-v*
sudo ./install.sh
```

4. Install [freenect_launch](http://wiki.ros.org/freenect_launch) which includes launch files to open an OpenNI device
```bash
sudo apt-get install ros-kinetic-freenect-camera ros-kinetic-freenect-launch
```
5. To run Kinect on ROS:
```bash
roslaunch freenect_launch freenect.launch
```

## Running Kinect with *Alpha*

Run the following command to visualize the kinect data using rviz:
```
roslaunch hardware_kinect kinect360_rviz.launch
```
