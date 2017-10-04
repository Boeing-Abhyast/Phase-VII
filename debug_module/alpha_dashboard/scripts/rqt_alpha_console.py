#!/usr/bin/env python
import roslib; roslib.load_manifest('alpha_dashboard')
import sys
import subprocess
import rospy

if __name__=="__main__":
    if len(sys.argv) >2:
        print("Usage: rqt_alpha_console.py file")
    else
        command = "rqt --perspective-file" + sys.argv[1]
        sys.exit(subprocess.call(command)
