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
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # call function to get sensor value
        port = 1
        sensor_reading = getSensorValue(port)
	#rospy.loginfo("Current time %i ", current_time.secs)
        rospy.loginfo("Sensor value at port %d: %f", 5, sensor_reading)
	while sensor_reading != 0:
		current_time = rospy.get_time()
		running_time = rospy.get_time()
		while (running_time - current_time) < 3:
			#behavior 1
			#right arm motion
			motor_id = 6
			target_val = 200
			response = setMotorTargetPositionCommand(motor_id, target_val)
			rospy.sleep(.1) 
			motor_id = 8
			target_val = 550
			response = setMotorTargetPositionCommand(motor_id, target_val)
			rospy.sleep(.2)
			#motor_id = 8
			target_val = 256
			response = setMotorTargetPositionCommand(motor_id, target_val)
			rospy.sleep(.3)
			motor_id = 6
        		target_val = 512
        		response = setMotorTargetPositionCommand(motor_id, target_val)
			motor_id = 8
			target_val = 475
			response = setMotorTargetPositionCommand(motor_id, target_val)
			
			#check time duration threshold
			running_time = rospy.get_time()
			if (running_time - current_time) > 3:
				break
			#check sensor value and break appropriately
			sensor_reading = getSensorValue(port)
			if sensor_reading == 0:
				break

			#left arm motion
			motor_id = 5
			target_val = 824
			response = setMotorTargetPositionCommand(motor_id, target_val)
			rospy.sleep(.1) 
			motor_id = 7
			target_val = 474
			response = setMotorTargetPositionCommand(motor_id, target_val)
			rospy.sleep(.2)
			#motor_id = 7
			target_val = 768
			response = setMotorTargetPositionCommand(motor_id, target_val)
			rospy.sleep(.3)
			motor_id = 5
        		target_val = 512
        		response = setMotorTargetPositionCommand(motor_id, target_val)
			motor_id = 7
			target_val = 549
			response = setMotorTargetPositionCommand(motor_id, target_val)
			
			running_time = rospy.get_time()
			#check sensor value and break appropriately
			sensor_reading = getSensorValue(port)			
			if sensor_reading == 0:
				break
		
		sensor_reading = getSensorValue(port)
		if sensor_reading == 0:
			break
		rospy.sleep(.5)
		while sensor_reading != 0:
			#threshold action aka, behavior 2
			motor_id = 6
			target_val = 75
			response = setMotorTargetPositionCommand(motor_id, target_val)
			motor_id = 5
			target_val = 949
			response = setMotorTargetPositionCommand(motor_id, target_val)
			#rospy.sleep(.25)
			motor_id = 8
			target_val = 550
			response = setMotorTargetPositionCommand(motor_id, target_val)
			motor_id = 7
			target_val = 474
			response = setMotorTargetPositionCommand(motor_id, target_val)
			rospy.sleep(.25)
			motor_id = 8			
			target_val = 350
			response = setMotorTargetPositionCommand(motor_id, target_val)
			motor_id = 7
			target_val = 674
			response = setMotorTargetPositionCommand(motor_id, target_val)
			sensor_reading = getSensorValue(port)
		rospy.sleep(1)

        # call function to set motor position
	else:        
		motor_id = 6
        	target_val = 512
        	response = setMotorTargetPositionCommand(motor_id, target_val)
		motor_id = 8
		target_val = 475
		response = setMotorTargetPositionCommand(motor_id, target_val)
		motor_id = 5
		target_val = 512
		response = setMotorTargetPositionCommand(motor_id, target_val)
		motor_id = 7
		target_val = 549
		response = setMotorTargetPositionCommand(motor_id, target_val)


        # sleep to enforce loop rate
        r.sleep()

