gridSize = 1000
t = 0
phaseChange = 2
numberOfTriangles = 90

def setup():
    size(gridSize, gridSize)
    rectMode(CENTER)
    colorMode(HSB)
    
def draw():
    global t
    translate(width/2,height/2)    
    background(255)
    for i in range(numberOfTriangles):
        rotate(radians(360/numberOfTriangles))
        pushMatrix()
        translate(200,0)
        rotate(radians(t+phaseChange*i*360/numberOfTriangles))
        equilacteralTriangle(100,i)
        popMatrix()
    t+=0.5
    
def equilacteralTriangle(length, i):
    noFill()
    stroke(255*i/numberOfTriangles,255,255)
    triangle(0,-length,-length*sqrt(3)/2,length/2,length*sqrt(3)/2,length/2)
