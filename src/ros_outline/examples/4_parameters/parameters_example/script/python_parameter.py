#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def main_function():
    
    rospy.init_node('python_paramters', anonymous=True)
    
    rospy.set_param('python_param', 1)

    x = rospy.get_param('python_param')

if __name__ == '__main__':
    try:
        main_function()
    except rospy.ROSInterruptException:
        pass