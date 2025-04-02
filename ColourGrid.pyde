gridSize = 600
amountOfSquaresInGrid = 50
squareSize = gridSize/amountOfSquaresInGrid

def setup():
    size(gridSize, gridSize)
    rectMode(CENTER)
    colorMode(HSB)
    
def draw():
    background(0)
    translate(20,20)
    for x in range(amountOfSquaresInGrid):
        for y in range(amountOfSquaresInGrid):
            d=dist(squareSize*x,squareSize*y,mouseX,mouseY)
            fill(0.5*d,255,255)
            rect(squareSize*x,squareSize*y,squareSize,squareSize)
              
    
