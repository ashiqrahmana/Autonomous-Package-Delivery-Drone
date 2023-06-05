#!/usr/bin/env python3
# ROS python API
import rospy
import cv2
# 3D point & Stamped Pose msgs
from geometry_msgs.msg import Point, PoseStamped
from sensor_msgs.msg import NavSatFix
# import all mavros messages and services
from mavros_msgs.msg import *
from mavros_msgs.srv import *

# GLOBAL VARIABLES
temp_height = 0

# Flight modes class
# Flight modes are activated using ROS services
class fcuModes:
    def __init__(self):
        pass
    def setTakeoff(self):
    	rospy.wait_for_service('mavros/cmd/takeoff')
    	try:
    		takeoffService = rospy.ServiceProxy('mavros/cmd/takeoff', mavros_msgs.srv.CommandTOL)
    		takeoffService(altitude = 10)
    	except rospy.ServiceException:
    		print ("Service takeoff call failed: %s")

    def setArm(self):
        rospy.wait_for_service('mavros/cmd/arming')
        try:
            armService = rospy.ServiceProxy('mavros/cmd/arming', mavros_msgs.srv.CommandBool)
            armService(True)
        except rospy.ServiceException:
            print ("Service arming call failed: %s")

    def setDisarm(self):
        rospy.wait_for_service('mavros/cmd/arming')
        try:
            armService = rospy.ServiceProxy('mavros/cmd/arming', mavros_msgs.srv.CommandBool)
            armService(False)
        except rospy.ServiceException:
            print ("Service disarming call failed: %s")

    def setStabilizedMode(self):
        rospy.wait_for_service('mavros/set_mode')
        try:
            flightModeService = rospy.ServiceProxy('mavros/set_mode', mavros_msgs.srv.SetMode)
            flightModeService(custom_mode='STABILIZED')
        except rospy.ServiceException:
            print ("service set_mode call failed: %s. Stabilized Mode could not be set.")
    def setOffboardMode(self):
        rospy.wait_for_service('mavros/set_mode')
        try:
            flightModeService = rospy.ServiceProxy('mavros/set_mode', mavros_msgs.srv.SetMode)
            flightModeService(custom_mode='OFFBOARD')
        except rospy.ServiceException:
            print ("service set_mode call failed: %s. Offboard Mode could not be set.")

    def setAltitudeMode(self):
        rospy.wait_for_service('mavros/set_mode')
        try:
            flightModeService = rospy.ServiceProxy('mavros/set_mode', mavros_msgs.srv.SetMode)
            flightModeService(custom_mode='ALTCTL')
        except rospy.ServiceException:
            print ("service set_mode call failed: %s. Altitude Mode could not be set.")

    def setPositionMode(self):
        rospy.wait_for_service('mavros/set_mode')
        try:
            flightModeService = rospy.ServiceProxy('mavros/set_mode', mavros_msgs.srv.SetMode)
            flightModeService(custom_mode='POSCTL')
        except rospy.ServiceException:
            print ("service set_mode call failed: %s. Position Mode could not be set.")
    def setAutoLandMode(self):
            rospy.wait_for_service('mavros/set_mode')
            try:
                flightModeService = rospy.ServiceProxy('mavros/set_mode', mavros_msgs.srv.SetMode)
                flightModeService(custom_mode='AUTO.LAND')
            except rospy.ServiceException:
                print("service set_mode call failed: %s. Autoland Mode could not be set.")
                
class Controller:
    global global_pos,temp_height
    # initialization method
    def __init__(self):
       
        # Drone state
        self.state = State()
        self.extended_state = ExtendedState()
        self.sp_glob = GlobalPositionTarget()
        self.sp_glob.type_mask = int('010111111000', 2)
        self.sp_glob.coordinate_frame = 6 #FRAME_GLOBAL_INT

        self.sp_glob.latitude = 13.010699197302143
        self.sp_glob.longitude = 80.2354019880295
        self.sp_glob.altitude = 10
        self.global_pos = Point(0.0, 0.0, 10)
        self.local_pos = Point(0.0, 0.0, 10)
                    
       

        # speed of the drone is set using MPC_XY_CRUISE parameter in MAVLink
        # using QGroundControl. By default it is 5 m/s.

	    # Callbacks

    
    def posCb_glob(self, msg_glob):    #rospy.Subscriber('mavros/global_position/global', NavSatFix, cnt.posCb_glob)
        self.global_pos.x = msg_glob.latitude   # NavSatFix(msg_glob).latitude -> global_pos.x = latitude
        self.global_pos.y = msg_glob.longitude
        self.global_pos.z = msg_glob.altitude
        #print(msg_glob)
    def posCb(self, msg):
        self.local_pos.z = msg.pose.position.z
        print(self.local_pos.z)

    def extended_state_callback(self,msg):
        self.extended_state.landed_state=msg.landed_state
        #print(self.extended_state.landed_state)


    ## Drone State callback
    def stateCb(self, msg):
        self.state = msg
    ## Update setpoint message
    
    def takeOff(self):
        self.sp_glob.latitude = self.global_pos.x
        self.sp_glob.longitude = self.global_pos.y
        self.sp_glob.altitude = 50
    def land(self):
        self.sp_glob.latitude = self.global_pos.x
        self.sp_glob.longitude = self.global_pos.y
        self.sp_glob.altitude = 0
    
    def updateSp_glob(self,lat,long):
        self.sp_glob.latitude =  lat #self.global_pos.x+0.00001
        self.sp_glob.longitude = long #self.global_pos.y +0.00001



# Main function
def main():
    #export PX4_HOME_LAT=13.009972684533134
    #export PX4_HOME_LON=80.23523569107057
    #export PX4_HOME_ALT=0

    # initiate node
    rospy.init_node('setpoint_node', anonymous=True)

    # flight mode object
    modes = fcuModes()

    # controller object
    cnt = Controller()
# ROS loop rate
    rate = rospy.Rate(20.0)

    # Subscribe to drone state
    rospy.Subscriber('mavros/state', State, cnt.stateCb)
    rospy.Subscriber('mavros/extended_state',ExtendedState,cnt.extended_state_callback)
                                              
                                              

 
    rospy.Subscriber('mavros/global_position/global', NavSatFix, cnt.posCb_glob) # cnt.global_pos = Drone's GPS position(lat, long, alt)

    # Subscribe to drone's local position
    rospy.Subscriber('mavros/local_position/pose', PoseStamped, cnt.posCb)


    # Setpoint publisher    
    sp_glob_pub = rospy.Publisher('mavros/setpoint_raw/global', GlobalPositionTarget, queue_size=1)

    #Get pickup and drop location from user
    with open('location.txt','r') as fread:
        temp = fread.readline()
        pick_up_lat = float(temp[:len(temp)-1])
        temp = fread.readline()
        pick_up_long = float(temp[:len(temp)-1])
        temp = fread.readline()
        drop_lat = float(temp[:len(temp)-1])
        temp = fread.readline()
        drop_long = float(temp[:len(temp)-1])
    

# Make sure the drone is armed
    while not cnt.state.armed:
        modes.setArm()
        rate.sleep()
    rospy.loginfo("Flight Armed!!")

    # set in takeoff mode and takeoff to default altitude (10 m)
    # modes.setTakeoff()
    # rate.sleep()


    delay_rate=rospy.Rate(0.2)
    

    # We need to send few setpoint messages, then activate OFFBOARD mode, to take effect
    k=0
    while k<10:
        sp_glob_pub.publish(cnt.sp_glob)
        rate.sleep()
        k = k + 1
        # activate OFFBOARD mode
    modes.setOffboardMode()
    rospy.loginfo("OFFBOARD mode set!! Ready to Takeoff!!")
    #13.0107253
    #80.2358043
    # ROS main loop
    while not rospy.is_shutdown():
        while(cnt.local_pos.z<9.5):
            cnt.takeOff()
            sp_glob_pub.publish(cnt.sp_glob)
            rate.sleep()
        rospy.loginfo("Takeoff successful!!")

        rospy.loginfo("Travelling to pickup point!!")
        while(not ((pick_up_lat-0.000005 <cnt.global_pos.x<pick_up_lat+0.000005) and (pick_up_long-0.000005 <cnt.global_pos.y<pick_up_long+0.000005))):
            cnt.updateSp_glob(pick_up_lat,pick_up_long)
            sp_glob_pub.publish(cnt.sp_glob)
            rate.sleep()
        rospy.loginfo("Reached Pickup Point!!")
        rospy.loginfo("Landing at Pickup Point!!")

        modes.setAutoLandMode()
        while(cnt.extended_state.landed_state!=1):
            pass
            # cnt.land()
            # sp_glob_pub.publish(cnt.sp_glob)
            # rate.sleep()
        
        

        rospy.loginfo("Landing Successful at Pickup Point!!")
        # modes.setDisarm()
        # rospy.loginfo("Flight Disarmed!! Package can be loaded now!!")
        delay_rate.sleep()

        # while not cnt.state.armed:
        #     modes.setArm()
        #     rate.sleep()
        # rospy.loginfo("Flight Armed!!")

        k=0
        while k<10:
            sp_glob_pub.publish(cnt.sp_glob)
            rate.sleep()
            k = k + 1
            # activate OFFBOARD mode
        modes.setOffboardMode()
        rospy.loginfo("OFFBOARD mode set!! Ready to Takeoff!!")

        while(cnt.local_pos.z<9.5):
            cnt.takeOff()
            sp_glob_pub.publish(cnt.sp_glob)
            rate.sleep()
        rospy.loginfo("Takeoff successful!!")

        rospy.loginfo("Travelling to destination point!!")
        while(not ((drop_lat-0.000005 <cnt.global_pos.x<drop_lat+0.000005) and (drop_long-0.000005 <cnt.global_pos.y<drop_long+0.000005))):
            cnt.updateSp_glob(drop_lat,drop_long)
            sp_glob_pub.publish(cnt.sp_glob)
            rate.sleep()
        rospy.loginfo("Reached Destination Point!!")
        rospy.loginfo("Landing at Destination Point!!")
        modes.setAutoLandMode()
        while(cnt.extended_state.landed_state!=1):
            pass
            # cnt.land()
            # sp_glob_pub.publish(cnt.sp_glob)
            # rate.sleep()

        rospy.loginfo("Landing Successful at Destination Point!!")
        modes.setDisarm()
        rospy.loginfo("Flight Disarmed!! Package can be unloaded now!!")
        delay_rate.sleep()
        rospy.loginfo("Flight Successful!!")
        break





if __name__ == '__main__':

    try:
        main()
    except rospy.ROSInterruptException:
	    pass