#!/usr/bin/evn python
import rospy
from osiris.msg import *

def talker():
    pub = rospy.Publisher('testlisten', GameObject, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.rate(200) # 200 Hz, faster than Unity
    while not rospy.is_shutdown():
        go = GameObject()
        
