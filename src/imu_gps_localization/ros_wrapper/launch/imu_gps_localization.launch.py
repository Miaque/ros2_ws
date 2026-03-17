from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg_share = FindPackageShare("imu_gps_localization")

    log_folder_arg = DeclareLaunchArgument(
        "log_folder",
        default_value="/tmp",
        description="Directory for state.csv and gps.csv output files",
    )

    localization_node = Node(
        package="imu_gps_localization",
        executable="imu_gps_localization_node",
        name="imu_gps_localization_node",
        output="screen",
        parameters=[
            {
                "acc_noise":       1e-2,
                "gyro_noise":      1e-4,
                "acc_bias_noise":  1e-6,
                "gyro_bias_noise": 1e-8,
                "I_p_Gps_x":       0.0,
                "I_p_Gps_y":       0.0,
                "I_p_Gps_z":       0.0,
                "log_folder":      LaunchConfiguration("log_folder"),
            }
        ],
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=[
            "-d",
            PathJoinSubstitution([pkg_share, "rviz", "default.rviz"]),
        ],
    )

    return LaunchDescription([
        log_folder_arg,
        localization_node,
        rviz_node,
    ])
