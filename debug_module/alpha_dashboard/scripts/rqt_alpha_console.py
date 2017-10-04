#!/usr/bin/env python
import roslib; roslib.load_manifest('alpha_dashboard')
import sys
import subprocess
import rospy

## Alternate approach by using roslaunchAPIs for python
# See here: http://wiki.ros.org/roslaunch/API%20Usage

# Approach stated here: https://answers.ros.org/question/272267/is-it-possible-to-launch-non-ros-applications-with-roslaunch/
if __name__=="__main__":
    if len(sys.argv) > 2:
        print("Usage: rqt_alpha_console.py file")
    else
        command = "rqt --perspective-file" + (rospy.myargv(argv=sys.argv)[1])
        sys.exit(subprocess.call(command))
