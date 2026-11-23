cmake_minimum_required(VERSION 3.8)
project(warehouse_robot_sim)

find_package(ament_cmake REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install(
  DIRECTORY launch urdf worlds config
  DESTINATION share/${PROJECT_NAME}
)

install(
  PROGRAMS scripts/measurement_covariance.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()