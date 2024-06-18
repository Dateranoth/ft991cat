#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial, time


SerialObj = serial.Serial('/dev/ttyUSB0')   # Port #/dev/ttyUSBx format on Linux
SerialObj.baudrate = 38400                  # Set Baud rate to 38400
SerialObj.bytesize = 8                      # Number of data bits = 8
SerialObj.parity   ='N'                     # No parity
SerialObj.stopbits = 1                      # Number of Stop bits = 1
SerialObj.timeout = 3                       # Set read timeout to 3 seconds

while True:
    cmd = input()
    cmd = cmd.strip().upper()
    if cmd == 'EXIT':
        break
    elif cmd == 'PS1':
        SerialObj.write(b'1;')
        time.sleep(1.1)
        SerialObj.write(b'PS1;')
        time.sleep(1)
        SerialObj.write(b'PS;')
    elif cmd == 'PS0':
        SerialObj.write(b'PS0;')
        time.sleep(1)
        SerialObj.write(b'PS;')
        time.sleep(1.1)
        SerialObj.reset_input_buffer()
        SerialObj.reset_output_buffer()
        SerialObj.write(b'PS;') 
    elif cmd == 'PS':
        SerialObj.write(b'PS;')
        time.sleep(1.1)
        SerialObj.reset_input_buffer()
        SerialObj.reset_output_buffer()
        SerialObj.write(b'PS;')        
    else:
        SerialObj.write((cmd + ';').encode())                           # Encode raw command and send
    EchoedVar    = SerialObj.read_until(b';')                           # Wait for 991 response
    print (EchoedVar.decode())                                          # Print the decoded response.
    SerialObj.reset_input_buffer()
    SerialObj.reset_output_buffer()
SerialObj.close()
