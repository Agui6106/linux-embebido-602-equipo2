# Nativas
import time
# Terceras
import serial
# Por nosotros
from locate_ports import find_serial_ports

ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200)

time.sleep(2)

# Escribimos al Arduino
ser.write(b'Hola tonotos')

time.sleep(1)

for i in range(3):
    to_send = f'prueba {i}'
    ser.write(to_send.encode('utf-8'))
    time.sleep(.5)
    received = ser.readline()
    print("Received: ", received)

# Cerramos comunicacion 
ser.close()