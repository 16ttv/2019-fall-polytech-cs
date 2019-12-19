def setup():
    size(600,600)
    smooth()
    background(255)
    noStroke()
    colorMode(HSB)

flug = bool(True)
i = 0
j = 0
def draw():
    global i , j, flug
    if( flug ):
        for i in range (-1, 10):
            i += 1
            for j in range (0, 10):
                j += 1
                fill(10,random(0,255), random(10,250))
                rect(j*40+50, j*40+50,35,35)
                rect((10-j)*40 + 10, i*40+50,35,35)
                j += 1
def mouseClicked():
    global i , j, flug
    flug = not flug
