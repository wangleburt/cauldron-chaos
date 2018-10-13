import serial

PIXELS_PER_STRIP = 72

#ser = serial.Serial('/dev/ttyACM0',1000000)

def update():
    #ser.write("c\n")
    pass

def setStrip(stripNumber, percent, red, green, blue):
    pixels = int(percent * PIXELS_PER_STRIP)
    serialWrite = "l%d,%d,%d,%d,%d\n"%(stripNumber,pixels,red,green,blue)
    #ser.write(serialWrite)
    #print(serialWrite)
    pass

def clearBoard():
    for i in range(8):
        setStrip(i, 0, 0, 0, 0);
    update()
    return
    