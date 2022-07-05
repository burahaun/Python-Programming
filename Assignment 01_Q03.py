import math
pi = math.pi


r = float(input("Enter the radius of a sphere: "))

def sphere_volume(r):
    volume = 4/3 * pi * r**3
    return volume

sphere_volume(r)
print(sphere_volume(r))


