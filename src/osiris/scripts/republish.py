#!/usr/bin/env python
import rospy
from osiris.msg import *
from geometry_msgs.msg import Pose
from std_msgs.msg import *

pub = rospy.Publisher('republished_float', GameObject, queue_size=10)

def callback(input_float):
    go = GameObject()
    go.unique_id = 0
    go.has_values = True
    go.values = []
    go.values.append(Values('length',input_float.data))
    pub.publish(go)

def republish():
    rospy.init_node('republisher')
    rospy.Subscriber('pressure0', Float64, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        republish()
    except rospy.ROSInterruptException:
        pass
