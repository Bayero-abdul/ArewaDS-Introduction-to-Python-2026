import math

# TODO: your program here
"""
Compute the circumference and area of a circle
"""

radius = int(input("Enter radius: "))
circ = 2 * math.pi * radius
area = math.pi * radius**2
print(f'circumference:', str(circ))
print(f'area:', str(area))