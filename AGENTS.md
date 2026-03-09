# 仓库指南

## 项目结构与模块组织
本仓库是一个以 `ros2_ws` 为根目录的 ROS 2 工作区。
- `src/cpp_pubsub/`：C++ 包（`ament_cmake`），节点源码在 `src/`，构建规则在 `CMakeLists.txt`。
- `src/my_package/`：Python 包（`ament_python`），模块代码在 `my_package/`，测试在 `test/`。
- `build/`、`install/`、`log/`：由 `colcon` 生成，请勿提交。
- `.vscode/tasks.json`：本地构建任务的规范参考。

新增包请放在 `src/` 下，并遵循现有 ROS 2 包布局（`package.xml`、构建元数据、源码、测试）。

## 构建、测试与开发命令
在工作区根目录执行：
- `source /opt/ros/jazzy/setup.bash`：加载 ROS 2 Jazzy 环境。
- `colcon build --symlink-install`：构建全部包。
- `colcon test`：运行包测试（包含以测试形式配置的 linter）。
- `colcon test-result --verbose`：查看失败测试详情。
- `source install/setup.bash`：运行节点前叠加当前工作区环境。
- `ros2 run my_package my_node` 与 `ros2 run cpp_pubsub talker`：运行示例节点。

为了保证本地构建可复现，优先使用 `.vscode/tasks.json` 中的参数（Clang 与 compile commands 导出）。

## 代码风格与命名规范
- Python：遵循 PEP 8，4 空格缩进；模块与函数使用 snake_case；测试文件命名为 `test_*.py`。
- C++：使用 C++17（由 `CMakeLists.txt` 约束）；沿用现有文件的 2 空格缩进；类名使用 PascalCase（如 `MinimalPublisher`）。
- 包名与 ROS 可执行名：使用小写加下划线（如 `my_package`、`my_node`）。
- 新增源码文件请添加 Apache-2.0 许可证头，以满足 lint 要求。

## 测试指南
- Python 测试使用 `pytest`，并结合 ament linters（`ament_flake8`、`ament_pep257`）。
- C++ 包在 `BUILD_TESTING` 下使用 `ament_lint_auto` / `ament_lint_common`。
- 测试放在各包的 `test/` 目录，文件命名为 `test_<topic>.py`。
- 提交 PR 前运行 `colcon test`，并确认 `colcon test-result --verbose` 无失败项。

## 提交与 Pull Request 规范
当前提交历史较少（仅 `first commit`），建议采用清晰的祈使句风格：
- 提交格式：`type(scope): 简短摘要`（示例：`feat(my_package): add timer-based publisher`）。
- 每次提交应聚焦且可构建。
- PR 需包含：变更目的、影响包列表、测试证据（`colcon test` 输出），以及行为变更的运行证明（日志片段或截图）。
- 关联相关 issue，并注明后续待办事项。
