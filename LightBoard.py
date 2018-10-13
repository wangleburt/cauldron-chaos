import serial
import threading
from time import sleep

PIXELS_PER_STRIP = 72

ser = serial.Serial('/dev/ttyACM0',1000000)
lock = threading.Lock()

STRIPS = ["l%d,72,0,0,0\n"%(i) for i in range(8)]

def setStrip(stripNumber, percent, red, green, blue):
    pixels = int(percent * PIXELS_PER_STRIP)
    #lock.acquire()
    #STRIPS[stripNumber] = "l%d,%d,%d,%d,%d\n"%(stripNumber,pixels,red,green,blue)
    #lock.release()
    line = "l%d,%d,%d,%d,%d\n"%(stripNumber,pixels,red,green,blue)
    ser.write(line)
    print(line)
    return

def clearBoard():
    #lock.acquire()
    for i in range(8):
        #STRIPS[i] = "l%d,%d,0,0,0\n"%(i, PIXELS_PER_STRIP)
        ser.write("l%d,%d,0,0,0\n"%(i, PIXELS_PER_STRIP))
    #lock.release()
    return

thread = None

def workerLoop():
    while True:
        for i in range(8):
            lock.acquire()
            line = STRIPS[i]
            lock.release()
            print("writing " + line)
            ser.write(line)
        ser.write("c\n")
        sleep(0.1)
    return

def init():
    thread = threading.Thread(target=workerLoop)
    thread.daemon = True
    thread.start()
    return

#init()
while True:
    for i in range(8):
        setStrip(i, 1, 255, 0, 0)
        sleep(0.05)
    ser.write("c\n")
    sleep(1)
    for i in range(8):
        setStrip(i, 1, 0, 255, 0)
        sleep(0.05)
    ser.write("c\n")
    sleep(1)
    for i in range(8):
        setStrip(i, 1, 0, 0, 255)
        sleep(0.05)
    ser.write("c\n")
    sleep(1)
    #clearBoard()
    #ser.write("c\n")
    #sleep(1)