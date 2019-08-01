
// #ifndef EXAMPLE_ROS_NODE_CLASS_H_
// #define EXAMPLE_ROS_NODE_CLASS_H_


// #include <ros/ros.h>                                        // Essential for all ROS nodes

// /* ROS Specific includes for a specific node */
// #include <std_msgs/Bool.h> 
// #include <std_msgs/Float32.h>

// /* other includes non-ROS specific */
// #include <math.h>                                           // Includes to consider
// #include <stdlib.h>
// #include <string>
// #include <vector>


// class ROSClassTemplate
// {
//     public:
//         /* constructors and deconstructors */
//         ROSClassTemplate();
//         ROSClassTemplate(ros::NodeHandle* nodehandle);       
//         ~ROSClassTemplate();

//     private:
//         ros::NodeHandle _nodeHandle;                        // only needed if maintaining a passed node
        
//         /* include only as needed ;; consider instantiation in constructor */
//         ros::Subscriber _sub;
//         ros::Publisher  _pub;
        
//         /* internal member variables / properties */
//         double _classVariable;
        
//         /* helper members */
//         /* ALTERNATIVE INITIALIZATION MEMBERS IF NEEDED */
//         /*
//         void initializeSubscribers();
//         void initializePublishers();
//         void initializePublishers();
//         */
// };

// #endif  // EXAMPLE_ROS_NODE_CLASS_H_

/* END HEADER -----------------------------------------------------------------------------*/

#include "rosclasstemplate.h"


ROSClassTemplate::ROSClassTemplate()
{
    //ros::init(argc, argv, "template_node");                       // Set up ROS
    //ros::NodeHandle n;
}



ROSClassTemplate::ROSClassTemplate(ros::NodeHandle* nodehandle)
{
    //ros::init(argc, argv, "template_node");                       // Set up ROS
    //ros::NodeHandle n;
    _nodeHandle = *nodehandle;
}