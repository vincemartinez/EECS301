#!/usr/bin/env python
import roslib
import rospy
from fw_wrapper.srv import *

# -----------SERVICE DEFINITION-----------
# allcmd REQUEST DATA
# ---------
# string command_type
# int8 device_id
# int16 target_val
# int8 n_dev
# int8[] dev_ids
# int16[] target_vals

# allcmd RESPONSE DATA
# ---------
# int16 val
# --------END SERVICE DEFINITION----------

# ----------COMMAND TYPE LIST-------------
# GetMotorTargetPosition
# GetMotorCurrentPosition
# GetIsMotorMoving
# GetSensorValue
# GetMotorWheelSpeed
# SetMotorTargetPosition
# SetMotorTargetSpeed
# SetMotorTargetPositionsSync
# SetMotorMode
# SetMotorWheelSpeed

# wrapper function to call service to get sensor value
def getSensorValue(port):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('GetSensorValue', port, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to set a motor target position
def setMotorTargetPositionCommand(motor_id, target_val):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
	resp1 = send_command('SetMotorTargetPosition', motor_id, target_val, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to get a motor's current position
def getMotorPositionCommand(motor_id):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
	resp1 = send_command('GetMotorCurrentPosition', motor_id, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to check if a motor is currently moving
def getIsMotorMovingCommand(motor_id):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
	resp1 = send_command('GetIsMotorMoving', motor_id, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e




# Main function
if __name__ == "__main__":
    rospy.init_node('example_node', anonymous=True)
    rospy.loginfo("Starting Group X Control Node...")
    
    # control loop running at 10hz
    r = rospy.Rate(1) # 1hz

    response = setMotorTargetPositionCommand(1,512)
    response = setMotorTargetPositionCommand(2,512)
    response = setMotorTargetPositionCommand(4, 510)
    response = setMotorTargetPositionCommand(3,501)
    rospy.sleep(1.0)

    while not rospy.is_shutdown():
        # call function to get sensor value
        #port = 5
        #sensor_reading = getSensorValue(port)
        #rospy.loginfo("Sensor value at port %d: %f", 5, sensor_reading)

        # call function to set motor position
        #motor_id = 1
        #target_val = 450
        # response = setMotorTargetPositionCommand(motor_id, target_val)

	#call function to get motor position
	#motor_1_reading=getMotorPositionCommand(1)
	#motor_2_reading=getMotorPositionCommand(2)
	#motor_3_reading=getMotorPositionCommand(3)
	#motor_4_reading=getMotorPositionCommand(4)
	#rospy.loginfo("Motor 1 position: %d\nMotor 2 position: %d\nMotor 3 position: %d\nMotor 4 position: %d",motor_1_reading,motor_2_reading,motor_3_reading,motor_4_reading)




	#walking block

	

	#response = setMotorTargetPositionCommand(4,400)
	#response = setMotorTargetPositionCommand(3,440)
	#rospy.sleep(0.1)
	#response = setMotorTargetPositionCommand(4,417)
	#rospy.sleep(0.1)

	#response = setMotorTargetPositionCommand(1,422)
	#rospy.sleep(0.1)
	#response = setMotorTargetPositionCommand(2,422)
	#rospy.sleep(0.1)

	#response = setMotorTargetPositionCommand(4,510)
	#response = setMotorTargetPositionCommand(3,501)
	#rospy.sleep(0.1)

	#response = setMotorTargetPositionCommand(3,616)
	#response = setMotorTargetPositionCommand(4,571)
	#rospy.sleep(0.1)
	#response = setMotorTargetPositionCommand(3,594)
	#rospy.sleep(0.1)

	#response = setMotorTargetPositionCommand(2,602)
	#rospy.sleep(0.1)
	#response = setMotorTargetPositionCommand(1,602)
	#rospy.sleep(0.1)

	#response = setMotorTargetPositionCommand(3,501)
	#response = setMotorTargetPositionCommand(4,510)
	#rospy.sleep(0.1)

	#while sensor_reading != 0:

	#turning right 90 degrees

	
	#####
	#response = setMotorTargetPositionCommand(4,375)
	#response = setMotorTargetPositionCommand(3,425)
	#rospy.sleep(0.1)
	#response = setMotorTargetPositionCommand(4,417)
	#rospy.sleep(0.1)

	#response = setMotorTargetPositionCommand(1,500)
	#rospy.sleep(0.05)
	#response = setMotorTargetPositionCommand(1,475)
	#rospy.sleep(0.05)
	#response = setMotorTargetPositionCommand(1,450)
	#rospy.sleep(0.05)
	#response = setMotorTargetPositionCommand(1,425)
	#rospy.sleep(0.05)
	#response = setMotorTargetPositionCommand(1,400)
	#rospy.sleep(0.05)

	#response = setMotorTargetPositionCommand(4,510)
	#response = setMotorTargetPositionCommand(3,501)
	#rospy.sleep(0.1)
	
	#response = setMotorTargetPositionCommand(1,512)
	#rospy.sleep(0.1)
	#####

	#####
	#response = setMotorTargetPositionCommand(3,616)
	#response = setMotorTargetPositionCommand(4,605)
	#rospy.sleep(0.1)

	#response = setMotorTargetPositionCommand(2,500)
	#rospy.sleep(.05)
	#response = setMotorTargetPositionCommand(2,475)
	#rospy.sleep(.05)
	#response = setMotorTargetPositionCommand(2,450)
	#rospy.sleep(.05)
	#response = setMotorTargetPositionCommand(2,425)
	#rospy.sleep(.05)
	#response = setMotorTargetPositionCommand(2,400)
	#rospy.sleep(.05)

	#response = setMotorTargetPositionCommand(4,510)
	#response = setMotorTargetPositionCommand(3,501)
	#rospy.sleep(0.1)

	#response = setMotorTargetPositionCommand(2,512)
	#rospy.sleep(0.1)
	#####

	#sensor_reading = getSensorValue(port)

	#turning left 90 degrees

	
	#####
	response = setMotorTargetPositionCommand(3,649)
	response = setMotorTargetPositionCommand(4,599)
	rospy.sleep(0.1)
	response = setMotorTargetPositionCommand(3,607)
	rospy.sleep(0.1)

	response = setMotorTargetPositionCommand(2,524)
	rospy.sleep(0.05)
	response = setMotorTargetPositionCommand(2,549)
	rospy.sleep(0.05)
	response = setMotorTargetPositionCommand(2,574)
	rospy.sleep(0.05)
	response = setMotorTargetPositionCommand(2,599)
	rospy.sleep(0.05)
	response = setMotorTargetPositionCommand(2,624)
	rospy.sleep(0.05)

	response = setMotorTargetPositionCommand(4,510)
	response = setMotorTargetPositionCommand(3,501)
	rospy.sleep(0.1)
	
	response = setMotorTargetPositionCommand(2,512)
	rospy.sleep(0.1)
	#####

	#####
	response = setMotorTargetPositionCommand(4,408)
	response = setMotorTargetPositionCommand(3,419)
	rospy.sleep(0.1)

	response = setMotorTargetPositionCommand(1,524)
	rospy.sleep(.05)
	response = setMotorTargetPositionCommand(1,549)
	rospy.sleep(.05)
	response = setMotorTargetPositionCommand(1,574)
	rospy.sleep(.05)
	response = setMotorTargetPositionCommand(1,599)
	rospy.sleep(.05)
	response = setMotorTargetPositionCommand(1,624)
	rospy.sleep(.05)

	response = setMotorTargetPositionCommand(4,510)
	response = setMotorTargetPositionCommand(3,501)
	rospy.sleep(0.1)

	response = setMotorTargetPositionCommand(1,512)
	rospy.sleep(0.1)
	#####



        # sleep to enforce loop rate
        r.sleep()

