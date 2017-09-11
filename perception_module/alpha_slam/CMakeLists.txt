cmake_minimum_required(VERSION 2.8.3)
project(alpha_slam)

find_package(catkin REQUIRED COMPONENTS
  nav_msgs
  openslam_gmapping
  roscpp
  rospy
  tf
)


###################################
## catkin specific configuration ##
###################################
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES alpha_slam
#  CATKIN_DEPENDS nav_msgs openslam_gmapping roscpp rospy tf
#  DEPENDS system_lib
)

# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)
