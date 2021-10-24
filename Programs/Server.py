#!/usr/bin/env pybricks-micropython

# Lib import
import os
from pybricks.messaging import BluetoothMailboxServer, TextMailbox, LogicMailbox, NumericMailbox
import logging
import uasyncio as asyncio

# Code General Setup
Debug = True

# General information for Logger
logger = logging.getLogger(' Lego Mailbox Server')
if(Debug == True):
    logging.basicConfig(level=logging.DEBUG)

# Obtaining MAC Address for the server
BluetoothMAC = os.popen("hcitool dev | cut -sf3").read()
logger.info(' Obtaining MAC Address: ', BluetoothMAC)

# Max. number of clients
MaxClients = 1
logger.debug(' Setting the maximum number of clients to: ' + MaxClients)

# Mailboxes declaration
MailServer = BluetoothMailboxServer()
logger.info(' Initiating the mail server')

MailCli0 = LogicMailbox("Client-0", MailServer)
logger.debug(' Creating a Boolean Mailbox with name: ' + 'Client-0')
#MailCli0Message = ""

MailCli1 = LogicMailbox("Client-1", MailServer)
logger.debug(' Creating a Boolean Mailbox with name: ' + 'Client-1')

BlueIntersection = TextMailbox("Blue-Intersection", MailServer)
logger.debug(' Creating a Textual Mailbox with name: ' + 'Blue-Intersection')

GreenIntersection = TextMailbox("Green-Intersection", MailServer)
logger.debug(' Creating a Textual Mailbox with name: ' + 'Green-Intersection')

# Waiting for clients connection
logger.info(' Start listening to potential EV3 clients')
MailServer.wait_for_connection(MaxClients)
logger.info(' Clients connected!')

def CloseServer():
    MailServer.close
    logger.critical( ' MailServer stopped')

async def GetUpdateMailCli0():
    while True:
        logger.info(' Start listening to the Mailbox: ' + 'Client-0')
        MailCli0.wait()  
        data = MailCli0.read()
        if (data != None):
            logger.info(' New message in mailbox: ' + 'Client-0 : ' + str(data))
            return str(data)

async def GetUpdateMailCli1():
    while True:
        logger.info(' Start listening to the Mailbox: ' + 'Client-1')
        MailCli1.wait()  
        data = MailCli1.read()
        if (data != None):
            logger.info(' New message in mailbox: ' + 'Client-1 : ' + str(data))
            return str(data)

async def GetUpdateBlueIntersection():
    while True:
        logger.info(' Start listening to the Mailbox: ' + 'BlueIntersection')
        BlueIntersection.wait()
        data = BlueIntersection.read()
        if (data != None):
            logger.info(' New message in mailbox: ' + 'Blue-Intersection : ' + str(data))
            return str(data)

async def GetUpdateGreenIntersection():
    while True:
        logger.info(' Start listening to the Mailbox: ' + 'Green-Intersection')
        GreenIntersection.wait()
        data = GreenIntersection.read()
        if (data != None):
            logger.info(' New message in mailbox: ' + 'Green-Intersection : ' + str(data))
            return str(data)

async def main():
    loop = asyncio.get_event_loop()
    loop.create_task(GetUpdateBlueIntersection())
    loop.run_forever()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()




