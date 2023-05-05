# LEGO type:standard slot:4

from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math

#define "my blocks"
def init():
    global hub, gyro, motor_arm_L, motor_arm_R, motors, motor_l, motor_r
    # Initialize the hub.
    hub = MSHub()
    #Initialize the gyro
    gyro = hub.motion_sensor
    #Initialize the motors arms.
    motor_arm_L = Motor('A')
    motor_arm_R = Motor('D')

    # Initialize the motors wheels.
    motors = MotorPair('B', 'C')
    motor_r = Motor('B')
    motor_l = Motor('C')
    motor_l.set_degrees_counted(0)
    motor_r.set_degrees_counted(0)

    #Initialize the gyro
    gyro.reset_yaw_angle()

def curr_angle():
    curr_angle_var = int(gyro.get_yaw_angle())
    return curr_angle_var


def update_diff_angle_left(dest_angle):
    if curr_angle() < 0 and dest_angle > 0:
        diff_angle = 300 + curr_angle() - dest_angle
    else:
        diff_angle = curr_angle() - dest_angle
    return diff_angle

def turn_l(dest_angle,max_v,min_v,pivot):
    motors.stop()
    curr_angle = gyro.get_yaw_angle()
