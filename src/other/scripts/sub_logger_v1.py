#!/usr/bin/env python
#refer to pub_example1.py to review first, similar comments excluded

import rospy
# from std_msgs.msg import String
#import msgs/controlLoop.msg
from publish_template.msg import controlLoop
#create delegate function that gets executed on the event of message_received

#f = file

def callback(data):
    
    #msg1 = data.inputCmd
    msg = data

    print (data)

    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    outputString = "{}, {}, {}\n".format(msg.outputValue, msg.inputCmd, msg.setPoint)
    f = open("/home/waltzrobotics/demofile.txt", "a")
    f.write(outputString)
    f.close()
    
    
#primary function call that assigns subscription delegate method
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('logger', anonymous=True)

    #f = open("/home/waltzrobotics/demofile.txt", "a")
    

    #assignment of subscription delegate function
    rospy.Subscriber("controlOut", controlLoop, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()


