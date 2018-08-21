#!/usr/bin/env python

#make sure script is executed as python

#imports from other packages
import rospy
from std_msgs.msg import String

#functions
def talker():
    
    #create publisher:  <topic_name, message_type, queue_for_subscriber>
    pub = rospy.Publisher('chatter', String, queue_size=10)

    #start node:  <name_of_node, determine_if_unique>
    rospy.init_node('talker', anonymous=True)
    
    #establish loop rate (publish rate) frequency
    rate = rospy.Rate(10) # 10hz

    #<param_name> , <param_value>
    rospy.set_param('/pub_value','2')

    #execute loop -> while roscore is active
    while not rospy.is_shutdown():
        
        #pub_value = rospy.get_param('/pub_value')

        #prepare message
        hello_str = "hello world!  Time: {} pub_value: {}".format(rospy.get_time(),  rospy.get_param('/pub_value'))
        #hello_str = "hello world!  Time: %s PubValue: " % (rospy.get_time(),  rospy.get_param('/pub_value'))
        #hello_str = "hello world!  Time: %s PubValue: " % (unicode(rospy.get_time(),  unicode(rospy.get_param('/pub_value')))
        
        #for display purposes
        rospy.loginfo(hello_str)
        
        #publish message
        pub.publish(hello_str)
        
        #execute only on desired rate
        rate.sleep()

#conditional for where script is called from
#also capture any errors from unintended publishes
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass