
#include <ros/ros.h>

int main(int argc, char **argv) 
{
    ros::init(argc, argv, "param_reader"); // name of this node will be "minimal_publisher"
    ros::NodeHandle nh; // two lines to create a publisher object that can talk to ROS
    double P_gain,D_gain,I_gain;

    nh.setParam("/joint1_gains/p", 5);
    
    if (nh.getParam("/joint1_gains/p", P_gain)) {
    ROS_INFO("proportional gain set to %f",P_gain);
    }

    if (!nh.hasParam("my_param"))
    {
        ROS_INFO("Paramter Not Found");
    }

    nh.deleteParam("/joint1_gains/p");
}

/*  also add in exmaple of logger */