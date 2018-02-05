#!/usr/bin/env python
import rospy
from osiris.msg import *
from std_msgs.msg import *

pub = rospy.Publisher('shimmer_gsr_con', Shimmer, queue_size=10)

def callback(shimmer_data):
    new_data = Shimmer()
    new_data.index = shimmer_data.index
    new_data.time = shimmer_data.time
    new_data.data = 1000.0 / shimmer_data.data
    pub.publish(new_data)

def shimmer_republish():
    rospy.init_node('shimmer_republisher')
    rospy.Subscriber('shimmer_gsr_cal', Shimmer, callback)
    rospy.Spin()

if __name__ == '__main__'
    try:
        shimmer_republish()
    except rospy.ROSInterruptException:
        pass

