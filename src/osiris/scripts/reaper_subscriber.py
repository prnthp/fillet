#!/usr/bin/env python
# Reaper: Kills rosserial upon Unity shutdown, forcing roslaunch to restart node.
import rospy
import os
from std_msgs.msg import String

def callback(data):
  if data.data == "unityshutdown":
    # Painful way
    # os.system("kill $(ps aux | grep socket_node | grep -v grep | awk '{print $2}')")
    # Correct way
    rospy.logwarn("Hellfire: Executing Rosserial Node")
    os.system("rosnode kill /socket_node")

def listener():
  rospy.init_node('osiris', anonymous=True)
  rospy.Subscriber("control", String, callback)

  rospy.spin()

if __name__ == '__main__':
  listener()
