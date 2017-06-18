#!/usr/bin/env python
# Comms Test: Recieves string and spits out md5 hash of string
import rospy
import md5
from osiris.srv import *

def handle_comms_test(req):
    rospy.loginfo("Comms Test: Got something")
    rospy.loginfo(md5.new(req.input).hexdigest())
    return comms_test_srvResponse(md5.new(req.input).hexdigest())

def comms_test_server():
    rospy.init_node('comms_test_server', anonymous=True)
    s = rospy.Service('comms_test', comms_test_srv, handle_comms_test)
    rospy.loginfo("Comms Test: Service started")

    rospy.spin()

if __name__ == '__main__':
    comms_test_server()
