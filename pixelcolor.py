from PIL import Image, ImageGrab
from time import sleep


def pixelCheck(h, v):
    # Number of horizontal by vertical Leds
    hLeds = h
    vLeds = v

    # load image with PIL
    # im = Image.open('control.jpg')  # Can be many different formats.
    # pix = im.load()

    # Grab screen
    try:
        screenshot = ImageGrab.grab()
        # im = Image.open(screenshot)
        # pix = im.load()
        im = screenshot
        pix = im.load()
    except:
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
    print(row)

    # Calculate column sample boxes
    column = []
    yRange = 0
    for i in range(vLeds+1):
        column.append(yRange)
        yRange += yBoxSize
    print(column)

    # Value for top row samples
    for i in row[1:]:
        rAv, gAv, bAv, rSum, gSum, bSum = 0, 0, 0, 0, 0, 0
        count = 0
        for x in range(i-xBoxSize, i, 7):
            for y in range(0, yBoxSize, 7):
                r, g, b = pix[x, y]
                # print(f'{count} {pix[x, y]}')
                rSum += r
                gSum += g
                bSum += b
                # print(count)
                count += 1
        print(f" Top Row box {i}: ", int(rSum/count),
              int(gSum/count), int(bSum/count))
        # print(count)

    # Value for bottom row samples
    for i in row[1:]:
        rAv, gAv, bAv, rSum, gSum, bSum = 0, 0, 0, 0, 0, 0
        count = 0
        for x in range(i-xBoxSize, i, 7):
            for y in range(imHeight-yBoxSize, imHeight, 7):
                r, g, b = pix[x, y]
                # print(f'{count} {pix[x, y]}')
                rSum += r
                gSum += g
                bSum += b
                # print(count)
                count += 1
        print(f" Bottom Row box {i}: ", int(rSum/count),
              int(gSum/count), int(bSum/count))
        # print(count)

    # Value for left column samples
    for i in column[1:]:
        rAv, gAv, bAv, rSum, gSum, bSum = 0, 0, 0, 0, 0, 0
        count = 0
        for x in range(i-yBoxSize, i, 7):
            for y in range(0, xBoxSize, 7):
                r, g, b = pix[x, y]
                # print(f'{count} {pix[x, y]}')
                rSum += r
                gSum += g
                bSum += b
                # print(count)
                count += 1
        print(f"Left Column box {i}: ", int(rSum/count),
              int(gSum/count), int(bSum/count), count)


        # print(count)
while True:
    sleep(.03)
    pixelCheck(16, 9)
