#!/usr/bin/env pybricks-micropython

# Lib import
import os
from pybricks.messaging import BluetoothMailboxServer, TextMailbox, LogicMailbox, NumericMailbox
import logging

# Code General Setup
Debug = False

# General information for Logger
logger = logging.getLogger(' Lego Mailbox Server')

# Obtaining MAC Address for the server
BluetoothMAC = os.popen("hcitool dev | cut -sf3").read()
logger.info(' Obtaining MAC Address: %s', BluetoothMAC)

# Max. number of clients
MaxClients = 1
logger.info(' Setting the maximum number of clients to: %s', MaxClients)

# Mailboxes declaration
MailServer = BluetoothMailboxServer()
logger.info(' Initiating the mail server')

MailCli0 = LogicMailbox("Client-0", MailServer)
logger.warning(' Creating a Boolean Mailbox with name: %s', 'Client-0')

MailCli1 = LogicMailbox("Client-1", MailServer)
logger.warning(' Creating a Boolean Mailbox with name: %s', 'Client-1')

BlueIntersection = TextMailbox("Blue-Intersection", MailServer)
logger.warning(' Creating a Textual Mailbox with name: %s', 'Blue-Intersection')

GreenIntersection = TextMailbox("Green-Intersection", MailServer)
logger.warning(' Creating a Textual Mailbox with name: %s', 'Green-Intersection')

# Waiting for clients connection
logging.info(' Start listening to potential EV3 clients')
MailServer.wait_for_connection(MaxClients)
logging.info(' Clients connected!')

# Beginning Loop
while True:
    MailCli0.wait()