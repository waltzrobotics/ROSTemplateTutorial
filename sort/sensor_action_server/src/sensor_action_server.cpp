#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <sensor_action_server/ArucoDetectAction.h>


/* need to
 * need to determine how to best consume this action server
 * aruco detect when operational needs to continuously provide aruco poses on tf
 * what is goal?  what is feedback?  how to cancel action when complete?
 * two separate actions?
 *
 */

class ArucoDetectAction
{
protected:

  ros::NodeHandle _nodeHandle;
  actionlib::SimpleActionServer<sensor_action_server::ArucoDetectAction> _actionServer; // NodeHandle instance must be created before this line. Otherwise strange error occurs.
  std::string _actionName;
  // create messages that are used to published feedback/result
  sensor_action_server::ArucoDetectFeedback _feedback;
  sensor_action_server::ArucoDetectResult _result;

public:
    ArucoDetectAction(std::string name) :
    _actionServer(_nodeHandle, name, boost::bind(&ArucoDetectAction::executeCB, this, _1), false),
    _actionName(name)
  {
    _actionServer.start();
  }

  ~ArucoDetectAction(void)
  {
  }

  void executeCB(const sensor_action_server::ArucoDetectGoalConstPtr &goal)
  {
    // helper variables
    ros::Rate r(1);
    bool success = true;


  }
};


int main(int argc, char** argv)
{
  ros::init(argc, argv, "ArucoDetect");

    ArucoDetectAction arucoDetect("ArucoDetect");
  ros::spin();

  return 0;
}