#!/usr/bin/env pybricks-micropython

from pybricks.messaging import BluetoothMailboxClient, BluetoothMailboxServer, TextMailbox
from pybricks.hubs import EV3Brick

ev3 = EV3Brick()

def server():
    ev3.screen.print("[@] Server")
    srv = BluetoothMailboxServer()
    mbox  = TextMailbox('AutoBus-Project', server)
    ev3.screen.print("[!] Waiting")
    srv.wait_for_connection()
    ev3.screen.print("[!] Connected")
    mbox.wait()
    ev3.screen.print(mbox.read)
    mbox.send("Prova-WRI - Server")

def client(MacAddress):
    ev3.screen.print("[@] Client")
    cli = BluetoothMailboxClient()
    mbox = TextMailbox('AutoBus-Project', client)
    ev3.screen.print("[!] Waiting for connection")
    cli.connect(MacAddress)
    ev3.screen.print("[!] Connected")
    mbox.send("Prova-WRI - Client", MacAddress)
    mbox.wait()
    ev3.screen.print(mbox.read())