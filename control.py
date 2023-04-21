#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
import math

def joy_callback(data):
    # Get the value of the left joystick's horizontal and vertical axes
    joy_x = data.axes[0]
    joy_y = data.axes[1]

    # Calculate the angle from the joystick values
    angle = math.atan2(joy_y, joy_x) * 180.0 / math.pi

    # Convert the angle to the range of -180 to +180 degrees
    if angle > 180.0:
        angle -= 360.0
    elif angle < -180.0:
        angle += 360.0

    # Print the angle to the terminal
    print('Angle: %f' % angle)

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('joy_to_angle')

    # Subscribe to the joystick topic
    rospy.Subscriber('joy', Joy, joy_callback)

    # Spin the ROS node to receive callbacks
    rospy.spin()
