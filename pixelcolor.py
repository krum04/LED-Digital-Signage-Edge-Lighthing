from PIL import Image

# Number of horizontal by vertical Leds
hLeds = 16
vLeds = 9

# load image with PIL
im = Image.open('test.jpg')  # Can be many different formats.
pix = im.load()

# Get the width and hight
imWidth, imHeight = im.size

# Calculate sample box size based on image size and number of Leds
xBoxSize = int(imWidth/hLeds)
yBoxSize = int(imHeight/vLeds)
# print(xBoxSize, yBoxSize)

# Calculate top row sample boxes
topRow = []
xRange = 0
for i in range(hLeds+1):
    topRow.append(xRange)
    xRange += xBoxSize
print(topRow)


bottomRow = []

for i in topRow[1:]:
    rAv, gAv, bAv, rSum, gSum, bSum = 0, 0, 0, 0, 0, 0
    count = 0
    for x in range(i-xBoxSize, i, 3):
        for y in range(0, yBoxSize, 3):
            r, g, b = pix[x, y]
            # print(f'{count} {pix[x, y]}')
            rSum += r
            gSum += g
            bSum += b
            # print(count)
            count += 1
    print(f"Xbox {i}: ", int(rSum/count), int(gSum/count), int(bSum/count))
