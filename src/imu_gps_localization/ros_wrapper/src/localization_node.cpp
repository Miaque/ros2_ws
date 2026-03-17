#include <memory>

#include <glog/logging.h>
#include <rclcpp/rclcpp.hpp>

#include "localization_wrapper.h"

int main(int argc, char** argv)
{
    // Initialize glog.
    FLAGS_colorlogtostderr = true;
    google::InitGoogleLogging(argv[0]);

    // Initialize ROS2.
    rclcpp::init(argc, argv);

    auto node = std::make_shared<LocalizationWrapper>();
    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}
