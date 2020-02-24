#include <ros/ros.h>

#include <dynamic_reconfigure/server.h>
//#include <dynamic_reconfigure_8/dconfig.h>
#include <dynamic_reconfigure_8/nodeExampleConfig.h>

void callback(dynamic_reconfigure_8::nodeExampleConfig &config, uint32_t level) {
  ROS_INFO("Reconfigure Request: %d %d %s %d ", 
            config.a, config.b, 
            config.message.c_str(), 
            config.enable?"True":"False");
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "dynamic_tutorials");

  dynamic_reconfigure::Server<dynamic_reconfigure_8::nodeExampleConfig> server;
  dynamic_reconfigure::Server<dynamic_reconfigure_8::nodeExampleConfig>::CallbackType f;

  f = boost::bind(&callback, _1, _2);
  server.setCallback(f);

  ROS_INFO("Spinning node");
  ros::spin();
  return 0;
}