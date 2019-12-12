size(550,500)
smooth()
background(255)
strokeWeight(30)
noLoop()

i = 1
while i < 8:
    i = i + 1
    stroke(20*i)
    line(i*50, 200, 150 + (i-1)*50, 300)
    line(i*50 + 100, 200, 50 + (i-1)*50, 300)
      
