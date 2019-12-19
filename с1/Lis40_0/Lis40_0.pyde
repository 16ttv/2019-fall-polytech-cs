def setup():
    size(500,500)
    smooth()
    background(50)
    strokeWeight(1)
    noLoop()

cx = 250
cy = 250
cRadius = 200
mcolor = float(0)
counter = float(0)

def draw():
    global cx,cy, cRadius, mcolor, counter
    y1 = cos(counter)*cRadius + cy
    x1 = sin(counter)*cRadius + cx
    mcolor = mcolor + 1
    stroke(mcolor)
    line(cx,cy,x1,y1)
    counter = counter + 2*PI/255
    while counter > 2*PI:
        counter = 0
        mcolor = 0
        background(50)
    
def keyPressed():
    if key =="s":
        saveFrame("wawa")
