wW = 500
wH = 500
eS = 100

size(500,500)
smooth()
background(255)
fill(50,80)
stroke(100)
strokeWeight(3)
noLoop()

ellipse(wW/2,wH/2 - eS/2,eS,eS)
ellipse(wW/2 - eS/2, wH/2,eS,eS)
ellipse(wW/2 + eS/2, wH/2,eS,eS)
ellipse(wW/2, wH/2 + eS/2,eS,eS)
