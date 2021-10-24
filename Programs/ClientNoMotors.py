#!/usr/bin/env pybricks-micropython

# Lib import
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
import os

# Code General Setup
Debug = False

# Obtaining MAC Address for the server
BluetoothMAC = os.popen("hcitool dev | cut -sf3").read()

# MailBox Declaration
SERVER = '00:17:E9:B5:77:B0'
MailClient = BluetoothMailboxClient()
BlueIntersection = TextMailbox("Blue-Intersection", MailClient)
MailClient.connect(SERVER)


BlueIntersection.send("Prova da " + BluetoothMAC)
print("Messaggio Inviato")
    