#!/usr/bin/python3
import rospy
#from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory
import pigpio

servo_configs = [86,138,80, 75,52,83, 68,155,60, 73,50,75] #rf lf rb lb
servo_pins = [2,3,4,   14,15,17,   18,27,22,   23,24,25] #rf lf rb lb
pi_value =3.14
pi = pigpio.pi()

#initialize pigpio
for pin in servo_pins:
	pi.set_PWM_frequency(pin,50)
	pi.set_PWM_range(pin,2000)

def set_servo_angle(pin,angle):
	dutycycle = angle*1.1111111+50
	pi.set_PWM_dutycycle(pin,dutycycle)

def get_param():
    global servo_configs
    servo_configs.append(float(rospy.get_param('rf1_initial_angle')))
    servo_configs.append(float(rospy.get_param('rf2_initial_angle')))
    servo_configs.append(float(rospy.get_param('rf3_initial_angle')))

    servo_configs.append(float(rospy.get_param('lf1_initial_angle')))
    servo_configs.append(float(rospy.get_param('lf2_initial_angle')))
    servo_configs.append(float(rospy.get_param('lf3_initial_angle')))

    servo_configs.append(float(rospy.get_param('rb1_initial_angle')))
    servo_configs.append(float(rospy.get_param('rb2_initial_angle')))
    servo_configs.append(float(rospy.get_param('rb3_initial_angle')))

    servo_configs.append(float(rospy.get_param('lb1_initial_angle')))
    servo_configs.append(float(rospy.get_param('lb2_initial_angle')))
    servo_configs.append(float(rospy.get_param('lb3_initial_angle')))

def callback(data):
    points = data.points[0]
    joint_positions = points.positions

    lf1_position = (180/pi_value)*joint_positions[0]
    lf2_position = (180/pi_value)*joint_positions[1]
    lf3_position = (180/pi_value)*joint_positions[2]
    rf1_position = (180/pi_value)*joint_positions[3]
    rf2_position = (180/pi_value)*joint_positions[4]
    rf3_position = (180/pi_value)*joint_positions[5]
    lb1_position = (180/pi_value)*joint_positions[6]
    lb2_position = (180/pi_value)*joint_positions[7]
    lb3_position = (180/pi_value)*joint_positions[8]
    rb1_position = (180/pi_value)*joint_positions[9]
    rb2_position = (180/pi_value)*joint_positions[10]
    rb3_position = (180/pi_value)*joint_positions[11]

    set_servo_angle(14,servo_configs[3]+lf1_position)
    set_servo_angle(15,servo_configs[4]+lf2_position)
    set_servo_angle(17,servo_configs[5]-90-lf2_position-lf3_position)

    set_servo_angle(2,servo_configs[0]+rf1_position)
    set_servo_angle(3,servo_configs[1]-rf2_position)
    set_servo_angle(4,servo_configs[2]+90+rf2_position+rf3_position)

    set_servo_angle(23,servo_configs[9]+lb1_position)
    set_servo_angle(24,servo_configs[10]+lb2_position)
    set_servo_angle(25,servo_configs[11]-90-lb2_position-lb3_position)

    set_servo_angle(18,servo_configs[6]+rb1_position)
    set_servo_angle(27,servo_configs[7]-rb2_position)
    set_servo_angle(22,servo_configs[8]+90+rb2_position+rb3_position)
    #rospy.loginfo(lf2_position)

def listener():
    rospy.init_node('pupper_ros',anonymous=True)
    #get_param()
    rospy.Subscriber("/joint_group_position_controller/command",JointTrajectory 
,callback,queue_size=1)
    rospy.spin()

if __name__=='__main__':
    listener()
