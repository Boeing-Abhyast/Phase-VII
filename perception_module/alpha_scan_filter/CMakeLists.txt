cmake_minimum_required(VERSION 2.8.3)
project(alpha_scan_filter)

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

## add the C++ raw_scan_filter
add_executable(raw_scan_filter src/raw_scan_filter.cpp)
target_link_libraries(raw_scan_filter
  ${catkin_LIBRARIES}
)
