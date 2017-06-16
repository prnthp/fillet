#!/usr/bin/env python
# Ganesh: Launches rosbag using roslaunch API
import rospy
import os
import subprocess
from std_msgs.msg import String

def callback(data):
  if data.data == "recordbegin":
    rospy.loginfo("Ganesh: Starting rosbag")
    # TODO: Add information to bag filename
    name = "oculus"
    topics = "/noface_pose"
    command = "rosbag record -o " + name + " " + topics
    dir_save_bagfile = "/home/viki/Record/"
    robag_proc = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True, cwd=dir_save_bagfile)
  elif data.data == "recordend":
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

def listener():
  rospy.init_node('osiris', anonymous=True)
  rospy.Subscriber("control", String, callback)

  rospy.spin()

if __name__ == '__main__':
  listener()