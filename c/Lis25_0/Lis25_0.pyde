def setup():
    size(1000, 500)
    smooth()
    strokeWeight(30)
    stroke(100)
    
def draw():
    background(0)
    line(frameCount, 300,100 + frameCount,400)
    line(100 + frameCount, 300, frameCount, 400)
