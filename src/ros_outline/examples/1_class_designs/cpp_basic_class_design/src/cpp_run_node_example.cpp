/*--------------------------------------------------------------------
 * node name
 * 
 * description
 * 
 * Subscriptions:
 * 
 * 
 * Publishers:
 * 
 * 
 * Author:  
 *
 * Revisions:
 * - 1.0 file created
 * 
 *------------------------------------------------------------------*/

/* includes */
#include "cpp_class.h"

using std::string;

int main(int argc, char **argv)
{
  ros::init(argc, argv, "node_name");                       // Set up ROS
  ros::NodeHandle n;

  // Declare variables that can be modified by launch file or command line.
  int rate;
  string topic;
  
  std::unique_ptr<ROSClassTemplate> rosclass (new ROSClassTemplate());          //in1) );   filename

  // Tell ROS how fast to run this node.
  ros::Rate r(rate);

  // Main loop.
  while (n.ok())
  {
    ros::spinOnce();
    r.sleep();
  }

  return 0;
} // end main()