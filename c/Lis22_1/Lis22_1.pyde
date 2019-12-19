size(600, 800)
smooth()
background(255)
strokeWeight(30)
noLoop()
noStroke()

for i in range(0, 10):
    for k in range(0, 10):
     fill(i*20)
     rect(i*50 + 50, 220 + 40*k, 40, 35)
    
