# -- Encontrar los puertos seriales disponibles -- #
# Importamos 
import serial.tools.list_ports

# Declaramos la funcion
def find_serial_ports():
    ports = serial.tools.list_ports.comports()
    serial_ports = []
    for port in ports:
        serial_ports.append(port.device)
    return serial_ports

if __name__ == "__main__":
    print("Puertos seriales disponibles:")
    ports = find_serial_ports()
    for port in ports:
        print(port)
