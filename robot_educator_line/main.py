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

DRIVE_SPEED = 60

deviation = 0

while True:
    if((line_sensor_right.reflection()>7 and line_sensor_right.reflection()<=11)or(line_sensor_left.reflection()>7 and line_sensor_left.reflection()<=11)):
        ev3.speaker.beep()
    else:
        if(line_sensor_right.reflection() <=threshold):
            deviation += 4
        if(line_sensor_left.reflection() <=threshold):
         deviation -= 4
        if(line_sensor_right.reflection() >=threshold and line_sensor_left.reflection() >=threshold):
            deviation=0
    robot.drive(DRIVE_SPEED, deviation)
    wait(15)
