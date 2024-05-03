# Primero imports de librerias standars (orden alfabético)
import time
# Librerias de terceros (3rd party libraaries)
import serial
# local libraries or modules
from locate_ports import find_ports
#import .exampleb

ser = serial.Serial(port = '/dev/ttyACM0', baudrate=115200)

time.sleep(2)

ser.write(b'hola')

time.sleep(1)

for i in range(1, 4):
    to_send = f'prueba {i}'
    ser.write(to_send.encode('utf-8'))
    time.sleep(.5)
    received = ser.readline()
    print("Received: ", received)

ser.close();
    
    
    