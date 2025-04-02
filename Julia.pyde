xmin = -2
xmax = 2
xscl = 0
rangex = xmax - xmin


ymin = -2
ymax = 2
yscl = 0
rangey = ymax - ymin


def complexAdd(a,b):
    return [a[0] + b[0], a[1] + b[1]]

def complexMultiply(u,v):
    return [u[0] * v[0] - u[1] * v[1], u[1] * v[0] + u[0] * v[1]]

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)

def julia(z, c, num):
    count = 0
    z1 = z
    while count < num:
        #check divergence
        if magnitude(z1) > 2.0:
            return count
        z1 = complexAdd(complexMultiply(z1,z1), c)
        count += 1
    return num

def setup():
    global xscl, yscl
    size(800,800)
    noStroke()
    colorMode(HSB)
    xscl = float(rangex)/width
    yscl = float(rangey)/height
    
def draw():
    for x in range (width):
        for y in range(height):
            z = [(xmin + x * xscl), (ymin + y * yscl)]
            c = [0.36, 0.1]
            divergenceCount = julia(z,c,100)
            if divergenceCount == 100:
                fill(0)
            else:
                fill(3 * divergenceCount, 255, 255)
            rect(x,y,1,1)
