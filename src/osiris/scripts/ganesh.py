#!/usr/bin/env python
# Ganesh: Launches rosbag using roslaunch API
import rospy
import os
import subprocess
from std_msgs.msg import String
from osiris.srv import *

def handle_ganesh(req):

  global name

  if req.command == "recordbegin":
    rospy.loginfo("Ganesh: Starting rosbag")
    # TODO: Add try-catch
    # TODO: Add information to bag filename

    name = req.filename

    topics = req.topics.split()
    for topic in topics:
        topics += topic + " "

    command = "rosbag record -o " + name + " " + topics
    dir_save_bagfile = os.path.expanduser("~") + "/Record/"
    rosbag_proc = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, cwd=dir_save_bagfile)
    return ganesh_srvResponse(1,name)

  elif req.command == "recordend":
    # TODO: Add try-catch
    # HACK: http://answers.ros.org/question/10714/start-and-stop-rosbag-within-a-python-script/
    list_cmd = subprocess.Popen("rosnode list", shell=True, stdout=subprocess.PIPE)
    list_output = list_cmd.stdout.read()
    retcode = list_cmd.wait()
    assert retcode == 0, "List command returned %d" % retcode

    for str in list_output.split("\n"):
        if (str.startswith("/record")):
            os.system("rosnode kill " + str)
            rospy.loginfo("Ganesh: Killed rosbag node: " + str)

    rospy.logwarn("Ganesh: Recording ended")
    return ganesh_srvResponse(1,name)

  else:
    return ganesh_srvResponse(0,"Unknown Command")

def ganesh_server():
  rospy.init_node('ganesh_server', anonymous=True)
  s = rospy.Service('ganesh', ganesh_srv, handle_ganesh)
  rospy.loginfo("Ganesh: Service started")

  rospy.spin()

if __name__ == '__main__':
  ganesh_server()
