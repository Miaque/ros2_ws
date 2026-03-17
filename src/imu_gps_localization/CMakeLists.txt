cmake_minimum_required(VERSION 3.8)
project(imu_gps_localization)

# C++17
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# ament_cmake
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(Eigen3 REQUIRED)

# ---- imu_gps_localizer (算法库，内联构建) ----
add_subdirectory(imu_gps_localizer)

# ---- ros_wrapper 库 ----
add_library(ros_wrapper_lib
  ros_wrapper/src/localization_wrapper.cpp
)
target_include_directories(ros_wrapper_lib PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/ros_wrapper/include>
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/imu_gps_localizer/include>
  $<INSTALL_INTERFACE:include>
  ${EIGEN3_INCLUDE_DIR}
)
target_link_libraries(ros_wrapper_lib
  imu_gps_localizer_lib
  glog
)
ament_target_dependencies(ros_wrapper_lib
  rclcpp
  nav_msgs
  sensor_msgs
  geometry_msgs
)

# ---- 节点可执行文件 ----
add_executable(${PROJECT_NAME}_node
  ros_wrapper/src/localization_node.cpp
)
target_link_libraries(${PROJECT_NAME}_node
  ros_wrapper_lib
)
ament_target_dependencies(${PROJECT_NAME}_node
  rclcpp
)

# ---- 安装 ----
install(TARGETS ${PROJECT_NAME}_node
  DESTINATION lib/${PROJECT_NAME}
)
install(DIRECTORY ros_wrapper/launch/
  DESTINATION share/${PROJECT_NAME}/launch
)
install(DIRECTORY ros_wrapper/rviz/
  DESTINATION share/${PROJECT_NAME}/rviz
)

ament_package()
