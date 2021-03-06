__author__ = 'Amal G Jose'

import time
import string
from pynmea import nmea
try:
    import serial
except:
    print 'Missing package dependency for pySerial'
    raise

ser = serial.Serial()
ser.port = "/dev/tty.usbmodem1411"
ser.baudrate = 9600
ser.timeout = 1
ser.open()
gpgga = nmea.GPGGA()
while True:
    data = ser.readline()
    if data[0:6] == '$GPRMC':
        print(data)
        if data.split(',')[2] ==  'V':
            working = 0
            print('still searching...')
        else:
            working = 1
    if data[0:6] == '$GPGGA' and working == 1:
        # method for parsing the sentence
        gpgga.parse(data)
        print(data)
        lats = gpgga.latitude
        print("Latitude values : " + str(lats))

        lat_dir = gpgga.lat_direction
        print("Latitude direction : "+str(lat_dir))

        longitude = gpgga.longitude
        print "Longitude values : " + str(longitude)

        long_dir = gpgga.lon_direction
        print "Longitude direction : " + str(long_dir)

        time_stamp = gpgga.timestamp
        print "GPS time stamp : " + str(time_stamp)

        alt = gpgga.antenna_altitude
        print "Antenna altitude : " + str(alt)

        lat_deg = lats[0:2]
        lat_mins = lats[2:4]
        lat_secs = round(float(lats[5:])*60/10000, 2)

        latitude_string = lat_deg + '*' + lat_mins + string.printable[68] + str(lat_secs) + string.printable[63]
        print "Latitude : " + str(latitude_string)

        lon_deg = longitude[0:3]
        lon_mins = longitude[3:5]
        lon_secs = round(float(longitude[6:])*60/10000, 2)
        lon_str = lon_deg + '*' + lon_mins + string.printable[68]+ str(lon_secs) + string.printable[63]
        print "Longitude : " + str(lon_str)
