cmake_minimum_required(VERSION 2.8.3)
project(raw_scan_filter)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  sensor_msgs
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES raw_scan_filter
#  CATKIN_DEPENDS roscpp sensor_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a C++ library
# add_library(${PROJECT_NAME}
#   src/${PROJECT_NAME}/raw_scan_filter.cpp
# )
