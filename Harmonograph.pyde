t = 0
points = []
gridSize = 800

amplitude1, amplitude2, amplitude3, amplitude4 = 100, 100, 100, 100
frequency1, frequency2, frequency3, frequency4 = 2.01, 3, 3, 2
phaseShift1, phaseShift2, phaseShift3, phaseShift4 = -PI/2, 0, -PI/16, 0
decay1, decay2, decay3, decay4 = 0.00085,0.0065,0,0

def xCoefficient(a,f,t,p,d):
    return a * cos(f * t + p) * exp(-d * t)

def yCoefficient(a,f,t,p,d):
    return a * sin(f * t + p) * exp(-d * t)

def harmonograph(t):
    global amplitude1, amplitude2, amplitude3, amplitude4, frequency1, frequency2, frequency3, frequency4, phaseShift1, phaseShift2, phaseShift3, phaseShift4, decay1, decay2, decay3, decay4
    
    x = xCoefficient( amplitude1, frequency1, t, phaseShift1, decay1) + xCoefficient( amplitude3, frequency3, t, phaseShift3, decay3) 
    y = yCoefficient( amplitude2, frequency2, t, phaseShift2, decay2) + yCoefficient( amplitude4, frequency4, t, phaseShift4, decay4) 
    
    return [x, y]

def setup():
    size(gridSize, gridSize)
    
def draw():
    background(255)
    translate(width/2,height/2)
    global t, points
    while t < 1000:
        points.append(harmonograph(t))
        t += 0.01
        
    for i,p in enumerate(points):
        stroke(255,0,0,50)
        alpha(50)
        if i < len(points)-1:
            line(p[0],p[1],points[i+1][0],points[i+1][1])
