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
    rospy.logwarn("Hellfire: Executing Unity Rosserial Node")
    os.system("rosnode kill /rosserial_message_info")

    # Escalating to force SIGTERM on rosserial socket_node(s)
    os.system("kill $(rosnode info /unity_node | grep 'Pid: ' | grep -Eo '[0-9]{1,}')")
  elif data.data == "shimmershutdown":
    rospy.logwarn("Hellfire: Executing Shimmer Rosserial Node")
    os.system("rosnode kill /rosserial_message_info")
    # os.system("rosnode kill /shimmer_node")

    # Escalating to force SIGTERM on rosserial socket_node(s)
    os.system("kill $(rosnode info /shimmer_node | grep 'Pid: ' | grep -Eo '[0-9]{1,}')")

def listener():
  rospy.init_node('osiris', anonymous=True)
  rospy.Subscriber("control", String, callback)

  rospy.spin()

if __name__ == '__main__':
  listener()
