import serial
import time
from threading import Thread

        
def readLine(ser):
    cmd = ''
    while True:
        c = ser.read()
        if c == "\n":
            break
        cmd += c
        
    return cmd

    
def wait(ser, keyword):
    while True:
        line = readLine(ser).rstrip()
        print line
        if line == keyword:
            break
            
        time.sleep(0.1)
    
    
def main():       
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(1)
    wait(ser, 'READY')
    time.sleep(1)
    ser.write('LED_ON\n')
    time.sleep(1)


    
if __name__ == '__main__':
    main()
    