# Python3 code to demonstrate working of
from PIL import Image
# Converting String to binary
# Using join() + ord() + format()
 
# initializing string
test_str = "Hello"
 
# printing original string
print("The original string is : " + str(test_str))
 
# using join() + ord() + format()
# Converting String to binary
res = ''.join(format(ord(i), '08b') for i in test_str)
 
# printing result
print("The string after binary conversion : " + str(res))
print(res[0])
img=Image.new('RGB', (640,360))
global xAxis
global yAxis
yAxis=0
xAxis=0
def fill(xAxis,yAxis,c):
    if c==1:
        for a in range(xAxis,xAxis+16+1):
            for b in range(yAxis,yAxis+10):
                img.putpixel((xAxis,yAxis),(255,255,255))
    else:
        for a in range(xAxis,xAxis+16+1):
            
            for b in range(yAxis,yAxis+10):
                img.putpixel((xAxis,yAxis),(0,0,0))
                print('fsfsd')
                print(yAxis,xAxis)
                yAxis=yAxis+1
            xAxis=xAxis+1
    if xAxis>=640 :
        xAxis=0
        yAxis=yAxis+9
def imgPro(a):
    for b in a:
        if b==1:
            fill(xAxis,yAxis,1)
        else:
            fill(xAxis, yAxis, 0)
imgPro(res)
Image._show(img)



