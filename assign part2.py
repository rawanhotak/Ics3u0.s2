"""
name:rawan abdelbasit
date:28/3/2005
virables:a: edge length of the cube
d: space diagonal of the cube, calculated using the formula d = a * √3
# This program calculates the space diagonal of a cube using the formula: diagonal = side × √3
"""
a = float(input("please enter the edge length of your cube:"))
#this calculate the length of the inner diagonal of a cube using the formula d = a *, where 'a' is the side length.
d=a*math.sqrt(3)
print(f"the length of the inner diagonal of a cube with side lenght {a} is: {d:.2f}")
