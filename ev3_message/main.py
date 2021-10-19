from lib import messages
from pybricks.messaging import screen

screen.clear()
screen.print("[!] Message lib test")
screen.print("[!] Insert the mode\n1 - Master\n2 - Client\n")

#mode = input()

#if(mode == 1):
messages.server()
#elif(mode == 2):
#    messages.client
