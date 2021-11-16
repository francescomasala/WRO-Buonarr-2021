#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks import ev3brick as brick
from time import time

#class LightSensor(EvrdevSensor):
#    _ev3dev_driver_name='lego-nxt-light'
#
#    def ambient(self):
#        self._mode('AMBIENT')
#        return self._model(0)/10
#
#    def reflection(self):
#        self._mode('REFLECTION'
#)
#        return self._value(0)/10

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

line_sensor_left = ColorSensor(Port.S3)
line_sensor_right = ColorSensor(Port.S2)
color_sensor = ColorSensor(Port.S1)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

WHITE = 68
BLACK = 7
threshold = (BLACK+WHITE)/2

print ("left,right")

speed = 60

deviation = 0

while True:
    if(color_sensor.color()==Color.BLUE):
        speed = 0
        deviation=0
    else: 
        if(line_sensor_right.reflection() > threshold and line_sensor_left.reflection() > threshold):
            deviation=0
            speed=60
        else:
            if(line_sensor_right.reflection() < threshold and line_sensor_left.reflection() < threshold):
                deviation=0
                speed=60
            else:
                if(line_sensor_right.color()==RED):
                    while(speed>=0):
                        if(line_sensor_right.reflection()< threshold):
                            deviation+=3
                        if(line_sensor_left.reflection()<threshold):
                            deviation-=3
                        speed-=6
                        robot.drive(speed, deviation)
                        wait(15)
                    wait(150)
                    while(speed>=60):
                        if(line_sensor_right.reflection()< threshold):
                            deviation+=6
                        if(line_sensor_left.reflection()<threshold):
                            deviation-=6
                        speed+=6
                        wait(15)
                        robot.drive(speed, deviation)
                else:
                    if(line_sensor_right.reflection()< threshold):
                        deviation+=6
                    if(line_sensor_left.reflection()<threshold):
                        deviation-=6
        
    robot.drive(speed, deviation)
    print(str(line_sensor_left.reflection()) + "," + str(line_sensor_right.reflection())+ ","+ str(color_sensor.color()))

    wait(15)
