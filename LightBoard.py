import serial
import threading
from time import sleep

PIXELS_PER_STRIP = 72

ser = serial.Serial(port='/dev/ttyACM0', baudrate=1000000)
lock = threading.Lock()

STRIPS = ["l%d,72,0,0,0\n"%(i) for i in range(8)]

def write(line):
    ser.write(line)
    #print("wrote: " + line)
    response = ser.read(1)
    #print("read: " + response)
    return

def setStrip(stripNumber, percent, red, green, blue):
    pixels = int(percent * PIXELS_PER_STRIP)
    
    lock.acquire()
    STRIPS[stripNumber] = "l%d,%d,%d,%d,%d\n"%(stripNumber,pixels,red,green,blue)
    lock.release()
    '''
    line = "l%d,%d,%d,%d,%d\n"%(stripNumber,pixels,red,green,blue)
    write(line)
    '''
    return

def clearBoard():
    lock.acquire()
    for i in range(8):
        STRIPS[i] = "l%d,%d,0,0,0\n"%(i, PIXELS_PER_STRIP)
        #ser.write("l%d,%d,0,0,0\n"%(i, PIXELS_PER_STRIP))
    lock.release()
    return

thread = None

def workerLoop():
    sleep(1)
    while True:
        for i in range(8):
            lock.acquire()
            line = STRIPS[i]
            lock.release()
            write(line)
        write("c\n")
        #sleep(0.1)
    return

def init():
    thread = threading.Thread(target=workerLoop)
    thread.daemon = True
    thread.start()
    return

def lightTest():
    init()
    #sleep(1)
    while True:
        for i in range(256):
            for s in range(8):
                setStrip(s, 1, 255-i, 0, i)
            sleep(0.001)
        
        for i in range(256):
            for s in range(8):
                setStrip(s, 1, i, 255-i, 0)
            sleep(0.001)
        
        for i in range(256):
            for s in range(8):
                setStrip(s, 1, 0, i, 255-i)
            sleep(0.001)
        
    return

lightTest()