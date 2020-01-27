#include "cpp_class.h"


ROSClassTemplate::ROSClassTemplate()
{
    ros::init(argc, argv, "template_node");                       // Set up ROS
    ros::NodeHandle n;
    _nodeHandle = *nodehandle;
}

ROSClassTemplate::ROSClassTemplate(ros::NodeHandle* nodehandle)
{
    ros::init(argc, argv, "template_node");                       // Set up ROS
    _nodeHandle = *nodehandle;
}

