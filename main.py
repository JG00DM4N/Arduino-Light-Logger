import serial
import time

arduino = serial.Serial(port='COM8', baudrate=115200, timeout=1)

def write_read():
    data = arduino.readline().decode('utf-8').rstrip()
    return data

try:
    while True:
        arduino.write(str.encode("s"))
        value = write_read()
        if value != "":
            with open("SVGA_light_Sensor.txt", "a") as f:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                f.write(current_time + " -> " + value + "\n")

except KeyboardInterrupt:
    print("Bye!")
    exit()