#!/usr/bin/env python
# Ganesh: Launches rosbag using roslaunch API
import rospy
import os
import subprocess
from std_msgs.msg import String
from osiris.srv import *

def handle_ganesh(req):
  if req.command == "recordbegin":
    rospy.loginfo("Ganesh: Starting rosbag")
    # TODO: Add information to bag filename
    name = req.filename
    topics = ""
    for topic in req.topics:
        topics += topic + " "
    command = "rosbag record -o " + name + " " + topics
    dir_save_bagfile = os.path.expanduser("~") + "/Record/"
    rosbag_proc = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, cwd=dir_save_bagfile)
    return ganesh_srvResponse(1,name)
  elif req.command == "recordend":
    # http://answers.ros.org/question/10714/start-and-stop-rosbag-within-a-python-script/
    # Holy mother of hacks
    list_cmd = subprocess.Popen("rosnode list", shell=True, stdout=subprocess.PIPE)
    list_output = list_cmd.stdout.read()
    retcode = list_cmd.wait()
    assert retcode == 0, "List command returned %d" % retcode
    for str in list_output.split("\n"):
        if (str.startswith("/record")):
            os.system("rosnode kill " + str)
            rospy.loginfo("Ganesh: Killed rosbag node: " + str)
    rospy.logwarn("Ganesh: Recording ended")
    name = ""
    # TODO: FIX RETURN NAME
    return ganesh_srvResponse(1,name)

def ganesh_server():
  rospy.init_node('ganesh_server', anonymous=True)
  s = rospy.Service('ganesh', ganesh_srv, handle_ganesh)
  rospy.loginfo("Ganesh: Service started")

  rospy.spin()

if __name__ == '__main__':
  ganesh_server()
