#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

line_sensor_left = ColorSensor(Port.S3)
line_sensor_right = ColorSensor(Port.S2)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

BLACK = 7
WHITE = 68
threshold = (BLACK + WHITE) / 2

print ("left,right")

speed = 80

deviation = 0

while True:
    if(line_sensor_left.reflection() > threshold and line_sensor_right.reflection() > threshold):
        deviation=0
        speed =60
    else:
        if(line_sensor_left.reflection() < threshold and line_sensor_right.reflection() < threshold):
            deviation=-90
            speed=45
        else:
            if(line_sensor_left.reflection()< threshold):
                deviation-=7
                speed=45
            if(line_sensor_right.reflection()< threshold):
                deviation +=7
                speed=45

    robot.drive(speed, deviation)
    
    print(str(line_sensor_left.reflection()) + "," + str(line_sensor_right.reflection()))

    wait(15)