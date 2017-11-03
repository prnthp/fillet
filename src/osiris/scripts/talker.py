#!/usr/bin/env python
import rospy
from osiris.msg import *

def talker():
    pub = rospy.Publisher('testlisten', GameObject, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(200) # 200 Hz, faster than Unity
    while not rospy.is_shutdown():
        go = GameObject()
        go.time = 1.0
        pub.publish(go)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
