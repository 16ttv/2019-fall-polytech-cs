def setup():
    size(600,450)
    smooth()
    strokeWeight(30)
    stroke(100)
    background(0)
    
def draw():
    stroke(frameCount)
    line(frameCount, 100 + frameCount,100 + frameCount,200 + frameCount)
    line(100 + frameCount, 100 + frameCount, frameCount, 200 + frameCount)
