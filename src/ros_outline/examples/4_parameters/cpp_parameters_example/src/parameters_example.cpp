
#include <ros/ros.h>

int main(int argc, char **argv) {
    ros::init(argc, argv, "param_reader"); // name of this node will be "minimal_publisher"
    ros::NodeHandle nh; // two lines to create a publisher object that can talk to ROS
    double P_gain,D_gain,I_gain;
    
    if (nh.getParam("/joint1_gains/p", P_gain)) {
    ROS_INFO("proportional gain set to %f",P_gain);
    }
}

/*  also add in exmaple of logger */