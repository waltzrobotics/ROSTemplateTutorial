#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
from geometry_msgs.msg import Pose

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def arduinoSetParam(self, msg):
    
    check_theta_ = msg.position.x
    check_theta_ = msg.position.y
    check_theta_ = msg.position.z
    check_theta_ = msg.orientation.x

    #get_theta_launch = rospy.get_param('theta_launch')

    if(check_theta != self.current_theta_launch):
        rospy.set_param('theta_launch', check_theta)
        self.current_theta_launch = check_theta
    
    if(check_theta != self.current_theta_launch):
        rospy.set_param('theta_launch', check_theta)
        self.current_theta_launch = check_theta

    if(check_theta != self.current_theta_launch):
        rospy.set_param('theta_launch', check_theta)
        self.current_theta_launch = check_theta

    if(check_theta != self.current_theta_launch):
        rospy.set_param('theta_launch', check_theta)
        self.current_theta_launch = check_theta
    
def listener():

    # init theta param and variables
    self.current_theta_launch = 0
    rospy.set_param('theta_launch', 0)
    
    # init node and sub
    rospy.init_node('arduino_param_set', anonymous=True)

    rospy.Subscriber("publishLauncherAngle", Pose, arduinoSetParam)

    # keep alive until callback gets fired
    rospy.spin()


if __name__ == '__main__':
    listener()