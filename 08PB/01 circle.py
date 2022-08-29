import math 

def circle(r) :
    area = math.pi*r*r
    return area

def circumference(r) :
    circum = 2*math.pi*r
    return circum

def sphere(r) :
    volumn = (4/3)*math.pi*r*r*r
    return volumn

r = float(input("Enter a radius: "))

print('Area of a circle with radius %.2f is %.2f.' % (r, circle(r)))
print('Circumference of a circle with radius %.2f is %.2f.' % (r, circumference(r)))
print('Volume of sphere with radius %.2f is %.2f.' % (r, sphere(r)))