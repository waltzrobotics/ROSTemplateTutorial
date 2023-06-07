#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

import copy
import threading
import PyKDL

import rospy
import tf2_ros
import tf2_geometry_msgs
import tf_conversions
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Pose, PoseStamped, Transform, TransformStamped
from fiducial_msgs.msg import FiducialTransformArray, FiducialTransform

import time
import actionlib
from sensor_action_server.msg import ArucoDetectAction, ArucoDetectGoal, ArucoDetectResult

class ArucoRebroadcaster:
    """
    Attributes:
        markers (list): A list for maintaining data about
            any markers currently observed.
        tf_buffer: A buffer for maintaining transform data.
        tf_listener: To get data from the tf_buffer.

    """
    def __init__(self):
        #rospy.init_node('aruco_rebroadcaster')
        print('broadcaster created')
        self.tf_buffer = tf2_ros.Buffer(rospy.Duration(600))
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)
        self.tf_broadcaster = tf2_ros.TransformBroadcaster()

        self.markers = []
        self.marker_lock = threading.Lock()
        #rospy.Service('reset_aruco_rebroadcaster', Empty, self.reset_service_callback)
        rospy.Subscriber('/fiducial_transforms', FiducialTransformArray, self.fiducial_callback, queue_size=100)

    
    # def reset_service_callback(self, msg):
    #     with self.marker_lock:
    #         self.markers = []

    #     return EmptyResponse()
        
    
    def fiducial_callback(self, msg):
        """Publish the transform as ar_marker_{marker_num} to be consumed later

        Args:
            msg (fiducial_msgs/FiducialTransformArray)
        """
        #print("entered callback")
        # Look up the transform from world to the camera
        # if not self.tf_buffer.can_transform_full(
        #     'world', msg.header.stamp, msg.header.frame_id, msg.header.stamp, fixed_frame='world'):
        if not self.tf_buffer.can_transform_full(
            'world', msg.header.stamp, msg.header.frame_id, msg.header.stamp, fixed_frame='world'):
            #print(msg.header.frame_id)
            print(msg)
            print("not full transform")
            return

        world_to_cam_transform_stamped = self.tf_buffer.lookup_transform_full(
            'world', msg.header.stamp, msg.header.frame_id, msg.header.stamp, fixed_frame='world')
        #print("checkpoint1")
        for fiducial_transform in msg.transforms:
            world_to_fid_transform_stamped = self.compose_transforms(
                world_to_cam_transform_stamped, fiducial_transform.transform)

            marker_id = fiducial_transform.fiducial_id
            marker_frame = "ar_marker_{}".format(marker_id)
            world_to_fid_transform_stamped.child_frame_id = marker_frame
            #print("checkpoint2")
            with self.marker_lock:
                existing_marker = filter(lambda marker: marker['id'] == marker_id, self.markers)
                if existing_marker:
                    existing_marker[0]['transform_stamped'] = world_to_fid_transform_stamped
                else:
                    self.markers.append({'id': marker_id, 'transform_stamped': world_to_fid_transform_stamped})


    def compose_transforms(self, tf_ab_stamped, tf_bc):
        tf_bc_stamped = TransformStamped()
        tf_bc_stamped.transform = tf_bc
        ac_frame = (tf2_geometry_msgs.transform_to_kdl(tf_ab_stamped) * 
                 tf2_geometry_msgs.transform_to_kdl(tf_bc_stamped))
        
        tf_ac_stamped = TransformStamped()
        tf_ac_stamped.header = tf_ab_stamped.header
        tf_ac_stamped.transform.translation.x = ac_frame.p[0]
        tf_ac_stamped.transform.translation.y = ac_frame.p[1]
        tf_ac_stamped.transform.translation.z = ac_frame.p[2]

        (tf_ac_stamped.transform.rotation.x,
         tf_ac_stamped.transform.rotation.y,
         tf_ac_stamped.transform.rotation.z,
         tf_ac_stamped.transform.rotation.w) = ac_frame.M.GetQuaternion()
        
        return tf_ac_stamped
            

    def run_rebroadcaster(self):
        # while not rospy.is_shutdown():
        #     with self.marker_lock:
        #         for marker in self.markers:
        #             stamped_transform = marker['transform_stamped']
        #             stamped_transform.header.stamp = rospy.Time.now()
        #             self.tf_broadcaster.sendTransform(stamped_transform)
            
        #     rospy.sleep(1)\
        start_time = time.time()
        timeout = 0
        print("before loop")
        while(timeout < 10):
            x = 1
            timeout = time.time() - start_time
            print(timeout)
            with self.marker_lock:
                for marker in self.markers:
                    stamped_transform = marker['transform_stamped']
                    print(stamped_transform)
                    stamped_transform.header.stamp = rospy.Time.now()
                    self.tf_broadcaster.sendTransform(stamped_transform)
                
            rospy.sleep(1)

        result = ArucoDetectResult()
        result.success = 0
        server.set_succeeded(result, "timedout")
        print("end -- need to terminate node")
        rospy.signal_shutdown("end condition")


def do_aruco_broadcast(goal):
    rospy.logdebug("starting broadcast")
    print('start broadcast')
    aruco_rebroadcaster = ArucoRebroadcaster()
    stop = 0
    
    print('start broadcast')
    broadcast_thread = threading.Thread(target=aruco_rebroadcaster.run_rebroadcaster)
    broadcast_thread.start()
    rospy.spin()
    broadcast_thread.join()
    # while(timeout < 30):
    #     x = 1
    #     timeout = time.time() - start_time
    #     print(timeout)
    #     with self.marker_lock:
    #         for marker in self.markers:
    #             stamped_transform = marker['transform_stamped']
    #             stamped_transform.header.stamp = rospy.Time.now()
    #             self.tf_broadcaster.sendTransform(stamped_transform)
            
    #     rospy.sleep(1)

    # result = ArucoDetectResult()
    # result.success = 0
    # server.set_succeeded(result, "timedout")
        # need some terminating action
        # don't need feedback topic if publish occurs in expected topic

        # loop here






# server 
rospy.init_node('aruco_action_node')
print('server started')
server = actionlib.SimpleActionServer('ArucoDetectAction', ArucoDetectAction, do_aruco_broadcast, False)
#server = actionlib.SimpleActionServer('ArucoDetectAction', ArucoDetectAction, do_aruco_broadcast, False)
server.start()
rospy.spin()

