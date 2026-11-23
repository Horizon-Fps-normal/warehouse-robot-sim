#!/usr/bin/env python3

import rclpy
from nav_msgs.msg import Odometry
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Imu


class MeasurementCovariance(Node):
    def __init__(self):
        super().__init__('measurement_covariance')
        self.wheel_pub = self.create_publisher(Odometry, '/wheel/odom_ekf', 10)
        self.imu_pub = self.create_publisher(Imu, '/imu/data_ekf', 10)
        self.create_subscription(
            Odometry, '/wheel/odom', self.forward_wheel, qos_profile_sensor_data
        )
        self.create_subscription(
            Imu, '/imu/data', self.forward_imu, qos_profile_sensor_data
        )

    def forward_wheel(self, msg):
        msg.twist.covariance[0] = 0.02 ** 2
        self.wheel_pub.publish(msg)

    def forward_imu(self, msg):
        if msg.angular_velocity_covariance[8] <= 0.0:
            msg.angular_velocity_covariance[8] = 0.01 ** 2
        self.imu_pub.publish(msg)


def main():
    rclpy.init()
    node = MeasurementCovariance()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()