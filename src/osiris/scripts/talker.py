#!/usr/bin/env python
import rospy
from osiris.msg import *
from geometry_msgs import Pose

def talker():
    pub = rospy.Publisher('testlisten', GameObject, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(200) # 200 Hz, faster than Unity
    while not rospy.is_shutdown():
        go = GameObject()
        go.unique_id = 1
        go.frame_count = 2
        go.time = 3.5
        go.parent = '4.0'
        go.num_poses = 5
        go.poses = []
        temp = Pose()
        temp.position.x = 1
        temp.position.y = 2
        temp.position.z = 3
        go.poses.append(temp)
        temp.position.x = 3
        temp.position.y = 2
        temp.position.z = 1
        go.poses.append(temp)
        go.has_event = True
        go.events = ['stop','drop','rooooooool']
        go.has_values = True
        go.values = []
        go.values.append(Values('weight',10.1))
        go.values.append(Values('height',99.9999990))
        
        pub.publish(go)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
