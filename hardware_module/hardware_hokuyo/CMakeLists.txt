cmake_minimum_required(VERSION 2.8.3)
project(hardware_hokuyo)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  tf2
  tf2_ros
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES hardware_kinect
#  CATKIN_DEPENDS roscpp tf2 tf2_ros
#  DEPENDS system_lib
)

###########
## Build ##
###########
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
