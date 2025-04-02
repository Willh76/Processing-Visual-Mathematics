gridSize = 600

outerCircleRadius = 300.0
innerCircleRadius = 112.0
dotRadius = 5.0
dotProportion = 0.7

x1 = 0
y1 = 0

t = 0 

points = []

def setup():
    size(gridSize, gridSize)
    
def draw():
    global outerCircleRadius,innerCircleRadius,dotRadius,dotProportion,x1,y1,t,points
    translate(width/2,height/2)
    background(255)
    noFill()
    ellipse(x1,y1,2*outerCircleRadius,2*outerCircleRadius)
    
    x2 = (outerCircleRadius - innerCircleRadius) * cos(t)
    y2 = (outerCircleRadius - innerCircleRadius) * sin(t)

    ellipse(x2, y2, 2 * innerCircleRadius, 2 * innerCircleRadius)
    
    x3 = x2 + dotProportion * (innerCircleRadius - dotRadius) * cos(-((outerCircleRadius - innerCircleRadius)/innerCircleRadius) * t)
    y3 = y2 + dotProportion * (innerCircleRadius - dotRadius) * sin(-((outerCircleRadius - innerCircleRadius)/innerCircleRadius) * t)
    
    fill(255,0,0)
    ellipse(x3,y3,2*dotRadius,2*dotRadius)
    
    points = [[x3, y3]] + points[:2000]
    for i,p in enumerate(points):
        if i < len(points)-1:
            line(p[0],p[1],points[i+1][0],points[i+1][1])

    t += 0.05
