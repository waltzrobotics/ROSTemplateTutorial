#!/usr/bin/env python

"""
<node name>:


SUBSCRIBE:


PUBLISH:


Revision:
    1.0 Initial Version
    1.1 

TODO:
    - 

References:
    - 
"""

from __future__ import division
from buffer import RingBuffer
import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import Int8
import time
import datetime
import numpy as np

class ClassNameNode():
    
    def __init__(self):                                                                             # constructor
        
        # Class Variables
        self.start_time = time.localtime()
       
        # ROS log
        rospy.loginfo("initializing commander node -- %s", t1)
        
        # ROS Parameters
        rospy.set_param('commander_status', 'init')
        self.num_runs = rospy.get_param('num_runs')
        
        # ROS Publisher / Subscribers
        self.pub1 = rospy.Publisher('robot_command', Point, queue_size=10)                          # create publisher:  <topic_name, message_type, queue_for_subscriber>

        self.sub1 = rospy.Subscriber("execute_command", Int8, self.execute_callback_function)

        # Other
        rate = rospy.Rate(0.2)                                                                      # ROS Loop Rate ==> 0.2 Hz = 5 sec

        # Loop
        while not rospy.is_shutdown():                                                              # check parameters for changes once every 10 sec
        
            # do stuff

            self.pub1.publish(robot_command)                                                        # publish message
        
            rate.sleep()                                                                            # maintain rate.  if no loop, use rospy.spin() to keep node alive
        
    def execute_callback_function(self, msg):                                                       # Callback must contain self and msg
        
        # do stuff

        return


if __name__ == '__main__':                                                                          # Entrance into node and init
    
    rospy.init_node('node_name')                                                                    # initialize the node and name it.
    
    try:
        cn = ClassNameNode()                                                                        # initialize node with object
    except rospy.ROSInterruptException: 
        pass