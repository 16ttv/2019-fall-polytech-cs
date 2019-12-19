def setup():
    size(300, 300)
    smooth()
    strokeWeight(3)
    background(0)

i = 0
k = 1
flug = 1

def upDate():
    global i, k, flug
    i +=k
    if i == 255:
        k=-1
    if i == 0:
        k=1

def draw():
    global i, k, flug
    stroke(i,20)
    
    if flug == 1:
        line(mouseX,mouseY, random(0,500), 0)
    else:
        line(mouseX, mouseY,  random(0,500), random(0,500))
    upDate()
        
def keyPressed():
    global i, k, flug
    if key == "q":
        flug = flug*(-1)
    if key == "s":
        saveFrame("meProcessing.png")
