cmake_minimum_required(VERSION 2.8.3)
project(alpha_gazebo)

find_package(catkin REQUIRED COMPONENTS
  diagnostic_aggregator
  gazebo_ros
  kobuki_gazebo_plugins
  robot_pose_ekf
  robot_state_publisher
  xacro
  yocs_cmd_vel_mux
)

# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)
