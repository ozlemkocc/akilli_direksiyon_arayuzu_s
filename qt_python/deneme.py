import serial
import struct
import time
ser = serial.Serial('/dev/ttyUSB0', 115200)
while True:
    data = ser.read(9)
    print(data)
    unpacked = list(struct.unpack('<ffB', data))
    print(unpacked)

