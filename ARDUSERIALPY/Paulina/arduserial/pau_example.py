# standard python libraries (alphabetical order)
import time
# 3rd party libraries
import serial
# Local libraries or modules
from locate_ports import find_ports

# Inicializar objeto serial
ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200)

time.sleep(2)

# Se tienen que mandar en bytes, al agregarle la b automaticamente manda el string en bytes
ser.write(b'hola')

time.sleep(1)

for i in range(1,4):
    to_send =  f'prueba {i}'
    ser.write(to_send.encode('utf-8'))
    time.sleep(.5)
    recieved = ser.readline()
    print("Recieved: ", recieved)
    
ser.close()
