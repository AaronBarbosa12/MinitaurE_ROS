#!/usr/bin/env python2

import rospy
import numpy as np
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

import struct
import serial
import math
from time import sleep
import ctypes as ct


def calculateChecksum(bytes, length):
    checksum = ct.c_ushort(0)
    for i in range(length):
        checksum = ct.c_ushort(int(checksum.value) + ord(bytes[i]));
    return checksum.value

def recieved_joycommand_callback(msg):
    # Set values
    id = 0
    mode = 1 # BehaviorMode_RUN
    print(-np.clip(msg.axes[4],a_min=-0.3,a_max=0.3))
    linear['x'] = -np.clip(msg.axes[4],a_min=-0.3,a_max=0.3) # Forwards and backwards
    linear['y'] = 0
    linear['z'] = 0
    angular['x'] = 0
    angular['y'] = 0
    angular['z'] = -2*msg.axes[3] # Yaw
    position['x'] = 0
    position['y'] = 0
    position['z'] = -2*msg.axes[1] # Height
    orientation['x'] = 0
    orientation['y'] = 0
    orientation['z'] = 0
    orientation['w'] = 0

    #print("Sending walking speed:  " + str(linear['x']))

    #print("Sending yaw speed:  " + str(angular['z']))
    #print("Sending height speed:  " + str(position['z']))
    # Pack BehaviorCmd. Definition is at the end of this file in comments.
    # Packet version number, BehaviorCmd: {id, twist.linear, twist.angular, pose.position, pose.orientation, mode}
    behavior_command = struct.pack( '<II3f3f3f4fI', 1, # Version 1 of serial packet format
                                                    id, 
                                                    linear['x'], linear['y'], linear['z'], 
                                                    angular['x'], angular['y'], angular['z'],
                                                    position['x'], position['y'], position['z'],
                                                    orientation['x'], orientation['y'], orientation['z'], orientation['w'],
                                                    mode)

    # Calculate and append checksum, prepend align bytes
    checksum = calculateChecksum(behavior_command, len(behavior_command))
    behavior_command = struct.pack('<cc', b"G", b"R") + behavior_command + struct.pack('<H', checksum)

    # Send BehaviorCmd via USB
    port.write(behavior_command)

if __name__ == '__main__':
    # Open USB port
    portAddress = "/dev/ttyUSB0"
    #portAddress = "/dev/tty.usbserial-DN01QAKV"
    #portAddress = "COM29"
    baud = 115200
    # baud = 230400
    # No timeout so we can keep going with whatever bytes are in waiting
    port = serial.Serial(portAddress, baud, timeout=None)
    print("Sending to: " + port.name)

    #rospy.loginfo("Joystick Command Receieved: " )
    #rospy.loginfo(msg.axes)

    # Init
    linear = {}
    angular = {}
    position = {}
    orientation = {}

    rospy.init_node('xbox_to_twist')

    sub = rospy.Subscriber("/joy",Joy,recieved_joycommand_callback)

    rospy.spin()
