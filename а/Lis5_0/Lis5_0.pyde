wW = 500
wH = 500
eS = 100
eW = 200
eH = 300

size(500,500)
smooth()
background(255)
fill(50,80)
stroke(100)
strokeWeight(3)
noLoop()

ellipse(wW/2,wH/2 - eS/2,eW,eH)
ellipse(wW/2 - eS/2, wH/2,eW,eH)
ellipse(wW/2 + eS/2, wH/2,eW,eH)
ellipse(wW/2, wH/2 + eS/2,eW,eH)
