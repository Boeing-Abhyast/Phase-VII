cmake_minimum_required(VERSION 2.8.3)
project(alpha_description)

find_package(catkin REQUIRED COMPONENTS
  urdf
  xacro
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
