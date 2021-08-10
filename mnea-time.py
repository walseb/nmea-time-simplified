#!/usr/bin/env python

import datetime
import sys
import time
import iso8601
import serial

def format_gprmc(dt):
        str= "GPRMC,{}.000,A,5321.6802,N,00630.3372,W,0.02,31.66,{},,,A".format(
                dt.strftime('%H%M%S'),
                dt.strftime('%d%m%y')
        )

        checksum = 0
        for c in str:
                checksum ^= ord(c)
        return ("$%s*%02X\n" % (str, checksum)).encode('ascii')

with serial.Serial('/dev/ttyUSB0', 9600) as ser:
        while True:
                ser.rts = True
                ser.write(format_gprmc(datetime.datetime.now()))
                ser.rts = False
                # Update every 10 minutes
                time.sleep(60*60*10)
