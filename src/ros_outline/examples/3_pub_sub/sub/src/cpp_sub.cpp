#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <stdlib.h>
#include <string>
#include <ros/console.h>

/*--------------------------------------------------------------------
 * 
 * 
 * 
 * 
 * Subscriptions:
 * 
 * 
 * Publishers:
 * n/a
 * 
 * Revisions:
 * - 1.0 Initial version.
 * - 1.1 
 * - 1.2 
 * 
 *------------------------------------------------------------------*/

using std::string;

void sub_callback(const geometry_msgs::Twist::ConstPtr &msg)
{  
  ROS_INFO("Pub message received");
  // manipulate msg and more elaborate print statement using data
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "cpp_sub_example");                       // Set up ROS
  ros::NodeHandle n;

  ROS_INFO("initializing sub node");

  // Declare variables and params that can be modified by launch file or command line.
  int rate;
  string topic;
  //n.setParam("/some_param", "0" );       

    // establish subscriber and link callback function
  ros::Subscriber primary_log_data = n.subscribe("/simple_pub", 1000, &sub_callback);
  
  // Tell ROS how fast to run this node.
  ros::Rate r(10);

  // Main loop.
  while (n.ok())
  {
    ros::spinOnce();
    r.sleep();
  }

  return 0;
} // end main()


