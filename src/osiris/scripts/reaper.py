#!/usr/bin/env python
# Reaper: Kills rosserial upon Unity shutdown, forcing roslaunch to restart node.
import rospy
import os
from std_msgs.msg import String
from osiris.srv import *

def handle_reaper(req):
    if req.input == "unityshutdown":
        rospy.logwarn("Reaper: Recieved request to murder rosserial node")
        os.system("rosnode kill /socket_node")
        return reaper_srvRespose(1)
    else:
        return reaper_srvRespose(0)

def reaper_server():
    rospy.init_node('reaper_server')
    s = rospy.Service('reaper', reaper_srv, handle_reaper)
    rospy.loginfo("Reaper: Service started")
    rospy.spin()

# def callback(data):
#   if data.data == "unityshutdown":
#     # Painful way
#     # os.system("kill $(ps aux | grep socket_node | grep -v grep | awk '{print $2}')")
#     # Correct way
#     rospy.logwarn("Reaper: Recieved request to murder rosserial node")
#     os.system("rosnode kill /socket_node")

# def listener():
#   rospy.init_node('osiris', anonymous=True)
#   rospy.Subscriber("control", String, callback)
#
#   rospy.spin()

if __name__ == '__main__':
  reaper_server()
