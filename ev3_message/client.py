#!/usr/bin/env pybricks-micropython
from LocalLib import messages
from pybricks.hubs import EV3Brick


def main():
    ev3 = EV3Brick()
    mex = messages
    ev3.screen.clear()
    ev3.screen.print("[!] Message lib test")
    ev3.screen.print("[!] Insert the mode\n1 - Master\n2 - Client\n")

    mex.client('00:17:E9:B5:77:B0')

if __name__ == '__main__':
    main()