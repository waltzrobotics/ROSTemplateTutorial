#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

import rospy 
import actionlib
from sensor_action_server.msg import ArucoDetectAction, ArucoDetectGoal, ArucoDetectResult

rospy.loginfo('start client')
print('start client')
rospy.init_node('sensor_action_client')
client = actionlib.SimpleActionClient('ArucoDetectAction', ArucoDetectAction)
client.wait_for_server()
goal = ArucoDetectGoal()
goal.status = 1

client.send_goal(goal)
client.wait_for_result()
rospy.logdebug("client complete")