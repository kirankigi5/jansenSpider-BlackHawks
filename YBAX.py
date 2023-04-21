#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
import math

def joy_callback(data):
    # Print the data.buttons array
    print('Y: up:', data.buttons[4])
    print('X: left:', data.buttons[3])
    print('A: down:', data.buttons[0])
    print('B: right:', data.buttons[1])

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('joy_buttons')

    # Subscribe to the joystick topic
    rospy.Subscriber('joy', Joy, joy_callback)

    # Spin the ROS node to receive callbacks
    rospy.spin()
#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
import math

def joy_callback(data):
    # Print the data.buttons array
    print('Button values:', data.buttons[4])

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('joy_buttons')

    # Subscribe to the joystick topic
    rospy.Subscriber('joy', Joy, joy_callback)

    # Spin the ROS node to receive callbacks
    rospy.spin()
