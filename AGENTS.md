# Repository Guidelines

## 项目结构与模块组织
本仓库是一个 **ROS 2 Jazzy** 工作区，所有功能包统一放在 `src/` 下。仓库同时包含 `ament_cmake` 的 C++ 包（如 `cpp_pubsub`、`custom_action_cpp`、`imu_gps_localization`）和 `ament_python` 的 Python 包（如 `py_pubsub`、`py_srvcli`、`nmea_navsat_driver`），另有接口包 `custom_action_interfaces`、`tutorial_interfaces`、`nmea_msgs`。C++ 头文件放在 `include/<package>/`，实现放在 `src/`，启动文件放在 `launch/`，RViz 配置放在 `rviz/`，Python 测试放在各包自己的 `test/` 目录。

## 构建、测试与开发命令
在工作区根目录执行构建：
`colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release`
迭代单个包时用：
`colcon build --packages-select imu_gps_localization`
构建后先加载环境：Linux 使用 `source install/setup.bash`，Windows 参考 `README.win.md` 中的 `local_setup.bat` 和 VS 环境变量设置。运行节点示例：
`ros2 run py_pubsub talker`
`ros2 run cpp_pubsub listener`
测试使用：
`colcon test`
`colcon test-result --verbose`

## 代码风格与命名约定
C++ 代码以 **C++17 + ROS 2 Jazzy** 为基线，保持现有 `-Wall -Wextra -Wpedantic` 警告级别可通过。沿用 ROS 2 常见风格：`CMakeLists.txt` 使用 2 空格缩进，文件名使用 snake_case，如 `fibonacci_action_server.cpp`。Python 遵循 PEP 8，使用 4 空格缩进，模块名、入口函数名与脚本名保持 snake_case，如 `publisher_member_function.py`、`talker`。

## 测试要求
Python 包使用 `pytest`，并集成 `ament_flake8` 与 `ament_pep257`；测试文件命名保持 `test_*.py`。多数 C++ 包当前主要依赖 `ament_lint_auto`。修改某个包后，至少执行：
`colcon test --packages-select <package_name>`
提交前确认对应包的测试结果无失败。

## 提交与合并请求规范
现有提交历史采用 Conventional Commits，例如 `feat(gps_goal): ...`、`fix(readme): ...`。继续沿用 `type(scope): subject`，其中 `scope` 应对应实际修改的包或目录。PR 需说明影响的包、列出验证命令；如果改动了 launch、RViz 或可视化行为，附上截图或运行结果说明。

## 环境与配置说明
`pyproject.toml` 中包含本地 Pyrefly 和 Windows ROS 2 环境配置。不要把机器私有路径硬编码进源码；与环境相关的路径应放在本地配置或说明文档中。
