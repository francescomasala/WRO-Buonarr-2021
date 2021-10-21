#!/usr/bin/env pybricks-micropython

from pybricks.messaging import BluetoothMailboxClient, BluetoothMailboxServer, TextMailbox
from pybricks.hubs import EV3Brick
import logging

from ev3_message.LocalLib.messages import server

class Ev3Message:
        def __init__(self, macAddress):
            self.macAddress = macAddress
            logging.info("[!] Initiating Client constructor")
        
        def __init__(self, clientCount):
            self.clientCount = clientCount
            ev3 = EV3Brick()
            logging.info("[!] Initiating Server constructor")
        
        def initServer(self,mailbox):
            mbox = TextMailbox(mailbox, server)
            srv = BluetoothMailboxServer()
            ev3 = EV3Brick()

            logging.info("[!] Initiating mailbox: " + mailbox)
            srv.wait_for_connection(self.clientCount)
            ev3.speaker.beep()
            ev3.screen.print("[!] Cli. Conn.")

            mbox.send("")
            print()

        def initClient():
            print()

        
            