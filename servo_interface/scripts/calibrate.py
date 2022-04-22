#!/usr/bin/python3
import os
import rospy
import yaml
import io
import pigpio

key_list = [\
'rf1_initial_angle','rf2_initial_angle','rf3_initial_angle',\
'lf1_initial_angle','lf2_initial_angle','lf3_initial_angle',\
'rb1_initial_angle','rb2_initial_angle','rb3_initial_angle',\
'lb1_initial_angle','lb2_initial_angle','lb3_initial_angle']
calibration_dict = {}

servo_configs = [95,137,145, 90,50,45, 93,107,140, 93,52,25] #calibrated list
servo_pins = [2,3,4,   14,15,17,   18,27,22,   23,24,25] #rf lf br bl
pi_value =3.14
pi = pigpio.pi()

#initialize pigpio
for pin in servo_pins:
        pi.set_PWM_frequency(pin,50)
        pi.set_PWM_range(pin,2000)

def set_servo_angle(pin,angle):
        dutycycle = angle*1.1111111+50
        pi.set_PWM_dutycycle(pin,dutycycle)

if __name__=='__main__':
    rospy.init_node('servo_calibration',anonymous=True)
    calibrated_angles = []
    flag = ""
    i = 0
    for pin in servo_pins:
        print("you are calibrating is servo "+str(i+1))
        while(1):
            angle = input("input an angle: ")
            set_servo_angle(pin,float(angle))
            flag = input("is this angle ok?(y/n)")
            print(flag)
            if(flag == "y" or flag == "Y" or flag == "yes"):
                break
            elif(flag == "n" or flag == "N" or flag == "no"):
                pass
            else:
                print("wrong input, please do it again")
        calibrated_angles.append(float(angle))
        current_key = key_list[i]
        calibration_dict[current_key] = angle
        i = i + 1
        print(calibration_dict)
    print("calibration done!")
    current_path = os.path.dirname(os.path.abspath(__file__))
    current_path = os.path.join(current_path,os.path.pardir)
    calibration_yaml_path = os.path.join(current_path,'config/calibration/calibration.yaml')
    with open(calibration_yaml_path, 'w') as f:
        yaml.dump(calibration_dict,f,default_flow_style=False)
