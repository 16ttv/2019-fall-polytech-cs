def setup():
    size(600, 600)
    noLoop()

def cc(a):      
    fill(a)
    rect(0,50,150,50)
    rect(50,0,50,150)

def draw():
    
    background(20)
    smooth()
    noStroke()

    pushMatrix()
    translate(100,0)
    cc(180)
    rotate(PI/4)
    popMatrix()

    pushMatrix()
    translate(220, 110)
    scale(2)
    cc(220)
    rotate(PI/4)
    popMatrix()

    pushMatrix()
    translate(520, 350)
    scale(1.4)
    cc(80)
    rotate(PI/4)
    popMatrix()
