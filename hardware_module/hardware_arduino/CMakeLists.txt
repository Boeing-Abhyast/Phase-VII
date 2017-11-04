cmake_minimum_required(VERSION 2.8.3)
project(hardware_arduino)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  rospy
  rosserial_arduino
  rosserial_client
  std_msgs
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES hardware_arduino
#  CATKIN_DEPENDS message_generation roscpp rospy rosserial_arduino rosserial_client std_msgs
#  DEPENDS system_lib
)

## Create a target called <package-name>_ros_lib, which will generate the rosserial client library
rosserial_generate_ros_lib(
  PACKAGE rosserial_arduino
  SCRIPT make_libraries.py
)

###########
## Build ##
###########

## Specify additional locations of header files
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

## Create target which will configure the CMake project in the specified subdirectory
rosserial_configure_client(
  DIRECTORY firmware
  TOOLCHAIN_FILE ${ROSSERIAL_ARDUINO_TOOLCHAIN}
)

## Configure the firmware directory and build the hello target therein
rosserial_add_client_target(firmware hello ALL)
rosserial_add_client_target(firmware hello-upload)
