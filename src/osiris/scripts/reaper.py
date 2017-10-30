#!/usr/bin/env python
# Reaper: Kills rosserial upon Unity shutdown, forcing roslaunch to restart node.
import rospy
import os
from std_msgs.msg import String
from osiris.srv import *

pub = rospy.Publisher('/control', String, latch=False, queue_size=10)

def handle_reaper(req):
    ## Using another subscriber to shutdown due to racing from service blocking call
    ## (otherwise rosserial will die and publisher/Unity will hang until timeout ~ 10 secs)
    if req.input == "unityshutdown":
        rospy.logwarn("Reaper: Recieved request to murder rosserial node")
        pub.publish("unityshutdown");
        return reaper_srvResponse(1)
    elif req.input == "shimmershutdown":
        rospy.logwarn("Reaper: Recieved request to murder rosserial node")
        pub.publish("shimmershutdown");
        return reaper_srvResponse(1)
    else:
        return reaper_srvResponse(0)

def reaper_server():
    rospy.init_node('reaper_server')
    rospy.on_shutdown(death_blossom)
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

def death_blossom():
    # Kills all rosserial nodes
    rospy.logwarn("Reaper: Clearing the area (killing all rosserial nodes)")
    os.system("kill $(rosnode info /unity_node | grep 'Pid: ' | grep -Eo '[0-9]{1,}')")
    os.system("kill $(rosnode info /shimmer_node | grep 'Pid: ' | grep -Eo '[0-9]{1,}')")

if __name__ == '__main__':
  reaper_server()
