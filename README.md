# How to use the repository?

1. Create a catkin worspace following the guidelines given [here](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```
2. Clone this repository to your catkin workspace
```bash
cd ~/catkin_ws/src
git clone -r https://github.com/Boeing-Abhyast/Phase-VII.git
```
3. Install all dependency packages to run the repository
```bash
# TODO List
sudo apt-get install ros-kinetic-<package-name>
```
4. Build the package using `catkin_make`
```bash
cd ~/catkin_ws
catkin_make
```
5. Launch the [`node_manager`](https://fkie.github.io/multimaster_fkie/node_manager.html) to use the gui for launching nodes
```bash
rosrun node_manager_fkie node_manager       
```


# Team Members

## Ground Vehicle Sub- Team
| Name | Department | Year |
| ------------- |:-------------:| -----:|
| [Mayank Mittal](mayankm96.github.io) | Electrical Engineering | Y14 |
| Ritwik Bera | Mechanical Engineering | Y14 |
| Vikulp Bansal | Electrical Engineering | Y14 |
| Tushar Aggarwal | Mechanical Engineering | Y14 |


## Aerial Vehicle Sub- Team
| Name | Department | Year |
| ------------- |:-------------:| -----:|
| Divyanshu Narayan | Mechanical Engineering | Y13 |
| Krishnraj Singh Gaur | Aerospace Engineering | Y13 |
| Rachit Agarwal | Civil Engineering | Y13 |
