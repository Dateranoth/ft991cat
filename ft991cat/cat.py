#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial, time, logging

class CAT:
    """Send Message to FT991 using serial"""
    def __init__(self, port = "/dev/ttyUSB0", baudrate = 38400,
                 bytesize = 8, parity = "N", stopbits = 1, timeout = 3):
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)

    def send_command(self, command, waitreply = True):
        """Send command to FT-991A. Return reply from server if waitreply True.
           ; Terminator and byte conversion will be done automatically.
           Example send_message("FA") - Returns FA014250000 (; terminator removed)
           """
        command = command.strip().upper() + ";"
        byteCommand = command.encode()        
        #self.logger.debug("Sending message: " + command)
        ft991SerialPort = serial.Serial(self.port, self.baudrate,self.bytesize,
                                        self.parity, self.stopbits, self.timeout)
        ft991SerialPort.write(byteCommand)
        if waitreply:
            ft991Response = ft991SerialPort.read_until(b";")
        else:
            ft991Response = b""
        return ft991Response.decode().replace(";", "")
    
    def power_switch(self, command = -1):
        """Power Switch Command for FT991. 
           0 = Power Off FT-991
           1 = Power On FT-991
           -1 or any other value = Check Power Status
           Returns True for power on and False for power off.
           """
        if command == 0:
            self.send_command("PS0", False)
        elif command == 1:
            #This command requires dummy data be initially sent. Then after one second and before two seconds the command is sent
            self.send_command("1", False) #dummy data
            time.sleep(1.1) #wait
            self.send_command("PS1", False) #send power on command
            time.sleep(1) #wait for power up
        ft991Response = self.send_command("PS")
        if ft991Response == "PS1":
            return True
        else:
            return False
    