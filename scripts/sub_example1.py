#!/usr/bin/env python
#refer to pub_example1.py to review first, similar comments excluded

import rospy
from std_msgs.msg import String

#create delegate function that gets executed on the event of message_received
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
#primary function call that assigns subscription delegate method
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    #assignment of subscription delegate function
    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()