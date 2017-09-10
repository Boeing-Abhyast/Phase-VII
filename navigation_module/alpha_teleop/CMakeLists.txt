cmake_minimum_required(VERSION 2.8.3)
project(alpha_teleop)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  tf
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES alpha_teleop
   CATKIN_DEPENDS geometry_msgs roscpp rospy tf
#   DEPENDS system_lib
)

###########
## Build ##
###########

# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)
## add the C++ keyboard_teleop
add_executable(keyboard_teleop src/keyboard_teleop.cpp)
add_dependencies(keyboard_teleop
	${catkin_EXPORTED_TARGETS}
	${${PROJECT_NAME}_EXPORTED_TARGETS}
)
target_link_libraries(keyboard_teleop
	${catkin_LIBRARIES}
)
