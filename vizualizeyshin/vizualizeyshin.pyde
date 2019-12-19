add_library('sound')

    
def setup():
    global img
    size(900, 900)
    noFill()
    strokeWeight(4)
    sample = SoundFile(this, "sample.mp3") 
    sample.loop()
    img = loadImage("gip.jpg")
    
t = 0
n = 90

def draw():
    image(img, 0, 0)
    global t
    translate(width/2, height/2)
    for i in range(n):
        rotate(radians(360/n))
        pushMatrix()
        translate(200,0)
        rotate(radians(t+2*i*360/n))
        stroke(0.1*i, 5, 5)
        r(100)
        popMatrix()
    t+=1
def r(length):
    triangle(0, -length, -length*sqrt(3)/2, length/2, length*sqrt(3)/2, length/2)
