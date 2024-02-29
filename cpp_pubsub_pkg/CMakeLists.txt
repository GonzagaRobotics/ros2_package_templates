cmake_minimum_required(VERSION 3.5)
project(cpp_pubsub_pkg)

# Set build type if not specified
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Debug")
endif()

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

# Include custom cmake scripts for code coverage
include(CodeCoverage.cmake)
APPEND_COVERAGE_COMPILER_FLAGS()

# Set the coverage exclusions
set(COVERAGE_LCOV_EXCLUDES 'launch/*' 'inputs/*' 'src/injector.cpp')
SETUP_TARGET_FOR_COVERAGE_LCOV(NAME coverage_report EXECUTABLE ctest --output-on-failure)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Compiler-specific options
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find package dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(pcl_conversions REQUIRED)


# Declare executables for publisher and subscriber member functions
add_executable(talker src/publisher_member_function.cpp)
ament_target_dependencies(talker  rclcpp std_msgs)

add_executable(listener src/subscriber_member_function.cpp)
ament_target_dependencies(listener rclcpp std_msgs)


# Installation commands for executables
install(TARGETS
  talker
  listener
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch inputs
  DESTINATION share/${PROJECT_NAME}/
)


# Ensure ament package is correctly set up
ament_package()
