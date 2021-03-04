from PIL import Image
import pyscreenshot as ImageGrab
from time import sleep
import board
import neopixel
  

def pixelCheck(h, v, sampeSize, sampleBorder):
    # Number of horizontal by vertical Leds
    hLeds = h
    vLeds = v
    pixels = neopixel.NeoPixel(board.D18, (hLeds*2)+(vLeds*2))

    # Create dict to hold LED values
    ledDict = {}
    ledCount = 0
    

    # # load image with PIL
    # im = Image.open('control.jpg')  # Can be many different formats.
    # pix = im.load()

    #Grab screen
    try:
        screenshot = ImageGrab.grab()
        im = screenshot
        pix = im.load()
    except:
        print('\nFail Imag Load\n')
        pass

    # Get the width and hight
    imWidth, imHeight = im.size

    # Calculate sample box size based on image size and number of Leds
    xBoxSize = int(imWidth/hLeds)
    yBoxSize = int(imHeight/vLeds)
    # print(xBoxSize, yBoxSize)

    # Calculate row sample boxes
    row = []
    xRange = 0
    for i in range(hLeds+1):
        row.append(xRange)
        xRange += xBoxSize
    # print(row)

    # Calculate column sample boxes
    column = []
    yRange = 0
    for i in range(vLeds+1):
        column.append(yRange)
        yRange += yBoxSize
    # print(column)

    # Value for top row samples
    for i in row[1:]:
        rAv, gAv, bAv, rSum, gSum, bSum = 0, 0, 0, 0, 0, 0
        count = 0
        for x in range(i-xBoxSize, i, sampeSize):
            for y in range(0, int(yBoxSize/sampleBorder), sampeSize):
                r, g, b = pix[x, y]
                # print(f'{count} {pix[x, y]}')
                rSum += r
                gSum += g
                bSum += b
                # print(count)
                count += 1
        # print(f" Top Row box {i}: ", int(rSum/count),
        #       int(gSum/count), int(bSum/count))
        ledDict[ledCount] = (int(rSum/count), int(gSum/count), int(bSum/count))
        ledCount = ledCount + 1
        # print(count)

    # Value for right column samples
    for i in column[1:]:
        rAv, gAv, bAv, rSum, gSum, bSum = 0, 0, 0, 0, 0, 0
        count = 0
        for x in range(imWidth-int(xBoxSize/sampleBorder), imWidth, sampeSize):
            for y in range(i-yBoxSize, i, sampeSize):
                r, g, b = pix[x, y]
                # print(f'{count} {pix[x, y]}')
                rSum += r
                gSum += g
                bSum += b
                # print(count)
                count += 1
        # print(f" Bottom Row box {i}: ", int(rSum/count),
        #       int(gSum/count), int(bSum/count))
        ledDict[ledCount] = (int(rSum/count), int(gSum/count), int(bSum/count))
        ledCount = ledCount + 1
        # print(count)
    
    
    # Value for bottom row samples
    for i in reversed(row[1:]):
        rAv, gAv, bAv, rSum, gSum, bSum = 0, 0, 0, 0, 0, 0
        count = 0
        for x in range(i-xBoxSize, i, sampeSize):
            for y in range(imHeight-int(yBoxSize/sampleBorder), imHeight, sampeSize):
                r, g, b = pix[x, y]
                # print(f'{count} {pix[x, y]}')
                rSum += r
                gSum += g
                bSum += b
                # print(count)
                count += 1
        # print(f" Bottom Row box {i}: ", int(rSum/count),
        #       int(gSum/count), int(bSum/count))
        ledDict[ledCount] = (int(rSum/count), int(gSum/count), int(bSum/count))
        ledCount = ledCount + 1
        # print(count)

    # Value for left column samples
    for i in reversed(column[1:]):
        rAv, gAv, bAv, rSum, gSum, bSum = 0, 0, 0, 0, 0, 0
        count = 0
        for x in range(0, int(xBoxSize/sampleBorder), sampeSize):
            for y in range(i-yBoxSize, i, sampeSize):
                r, g, b = pix[x, y]
                # print(f'{count} {pix[x, y]}')
                rSum += r
                gSum += g
                bSum += b
                # print(count)
                count += 1
        # print(f"Left Column box {i}: ", int(rSum/count),
        #       int(gSum/count), int(bSum/count), count)
        ledDict[ledCount] = (int(rSum/count), int(gSum/count), int(bSum/count))
        ledCount = ledCount + 1
        # print(count)
    for i in ledDict:
        pixels[i]=(ledDict[i])

        
# pixelCheck(16,9)
# while True:
#     sleep(.03)
#     pixelCheck(45, 30, 12, 1)
    
pixelCheck(45, 30, 12, 1)