cmake_minimum_required(VERSION 3.8)
project(imu_gps_localizer)

find_package(Eigen3 REQUIRED)

# 第三方：GeographicLib
add_subdirectory(third_party/GeographicLib)

add_library(imu_gps_localizer_lib
  src/imu_gps_localizer.cpp
  src/initializer.cpp
  src/imu_processor.cpp
  src/gps_processor.cpp
)

target_include_directories(imu_gps_localizer_lib PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/third_party/GeographicLib/include>
  ${EIGEN3_INCLUDE_DIR}
)

target_compile_features(imu_gps_localizer_lib PUBLIC cxx_std_17)

target_link_libraries(imu_gps_localizer_lib
  Eigen3::Eigen
  libGeographiccc
)
