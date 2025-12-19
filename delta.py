import math


a = float(input())
b = float(input())
c = float(input())


delta = b**2 - 4*a*c


if delta > 0:
    root1 = (-b + math.sqrt(delta)) / (2*a)
    root2 = (-b - math.sqrt(delta)) / (2*a)
    print( root1, root2)
elif delta == 0:
    root = -b / (2*a)
    print(root)
else:
    print( None)