This repository contains all the source code and design files for the work done by the ground vehicle sub-team in the Phase-VII of The Boeing Company's University Relation Program at IIT Kanpur called [Abhyast](https://www.iitk.ac.in/dord/boeing/public/).

The contents of the repository is available under the [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause).

# How to use the repository?

1. Create a catkin worspace following the guidelines given [here](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
```bash
mkdir -p ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws/
catkin_make
```
2. Clone this repository to your catkin workspace
```bash
cd ~/catkin_ws/src
git clone https://github.com/Boeing-Abhyast/Phase-VII.git
git submodule update --init --recursive
```
3. [Install all dependency packages to run the repository](#additional-ros-packages-required)
```bash
# TODO List
sudo apt-get install ros-kinetic-slam-gmapping     \
                     ros-kinetic-hector-slam       \
                     ros-kinetic-laser-filters     \
                     ros-kinetic-find-object-2d    \
                     ros-kinetic-navigation        \
                     ros-kinetic-node-manager-fkie \
                     -y
```
4. Build the package using [`catkin_make`](http://wiki.ros.org/catkin/commands/catkin_make)
```bash
cd ~/catkin_ws
# To maximize performance, build the workspace in Release mode
catkin_make -DCMAKE_BUILD_TYPE=Release
```
5. Launch the [`node_manager`](https://fkie.github.io/multimaster_fkie/node_manager.html) to use the gui for launching nodes
```bash
rosrun node_manager_fkie node_manager       
```

## <a name="additional-ros-packages-required"></a>Additional ROS Packages required

* [OpenSLAM GMapping](http://wiki.ros.org/gmapping)
* [Laser Filters](http://wiki.ros.org/laser_filters)
* [Find Object 2D](http://wiki.ros.org/find_object_2d)
* [Navigation Stack](http://wiki.ros.org/navigation)
* [Node Manager](https://fkie.github.io/multimaster_fkie/node_manager.html)
* [Darknet YOLOv2](https://github.com/leggedrobotics/darknet_ros)

# Team Members

__Main Repository Maintainer:__ [Mayank Mittal](mayankm96.github.io)

## Ground Vehicle Sub- Team
| Name | Department | Year |
| ------------- |:-------------:| -----:|
| Mayank Mittal | Electrical Engineering | Y14 |
| Ritwik Bera | Mechanical Engineering | Y14 |
| Vikulp Bansal | Electrical Engineering | Y14 |
| Tushar Aggarwal | Mechanical Engineering | Y14 |


## Aerial Vehicle Sub- Team
| Name | Department | Year |
| ------------- |:-------------:| -----:|
| Divyanshu Narayan | Mechanical Engineering | Y13 |
| Krishnraj Singh Gaur | Aerospace Engineering | Y13 |
| Rachit Agarwal | Civil Engineering | Y13 |
