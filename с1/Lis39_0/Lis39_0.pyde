def setup():
    size(500, 500)
    smooth()
    background(50)
    strokeWeight(5)
    noLoop()

cx = 250
cy = 250
cRadius = 200
i = 0

def draw():
    global cx,cy, cR, i
    
    while i < 2*PI:
        i +=PI/300
        stroke(i*35)
        x1 = cos(i)*cRadius + cx
        y1 = sin(i)*cRadius + cy
        line(cx, cy, x1, y1)
    line(cx, cy, x1, y1)

def keyPressed():
    if key =="s":
        saveFrame("wawa")
