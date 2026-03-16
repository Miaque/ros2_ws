# 开发环境准备

创建系统变量

```bash
set VSINSTALLDIR=H:\\software\\Microsoft Visual Studio\\2022\\Professional\\
set ROS2_PY=C:\\pixi_ws\\.pixi\\envs\\default
set ROS2_ROOT=C:\\pixi_ws\\ros2-windows
```

测试是否生效

```bash
echo %VSINSTALLDIR%
echo %ROS2_PY%
echo %ROS2_ROOT%
```

以管理员的方式打开"Developer Command Prompt for VS 2022", 
终端路径 `%VSINSTALLDIR%Common7\\Tools\\VsDevCmd.bat`

```bash
cd C:\\pixi_ws
pixi shell
cd H:\\workspace\\ROS2\\ros2_ws
H:
call C:\\pixi_ws\\ros2-windows\\local_setup.bat
set PYTHONUTF8=1
"%VSINSTALLDIR%VC\Auxiliary\Build\vcvars64.bat"
colcon build --packages-select cpp_pubsub --symlink-install --event-handlers console_direct+ --cmake-args -G Ninja -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```

为了方便vscode开发，创建软连接
```bash
mklink compile_commands.json build\\compile_commands.json
```