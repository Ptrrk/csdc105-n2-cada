# Author          : {Patrick James R. Cada}
# Course and Year : {BSIT - 2}
# Filename        : {cada_e4.py}
# Description     : {function for computing the triangle and mostly the code}
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.
import geometry
numbers = input("Enter the side lengths of a triangle: ")
side_lengths = []
for number in numbers.split(","):
	side_lengths.append(float(number))
a = side_lengths[0]
b = side_lengths[1]
c = side_lengths[2]
valid = geometry.Checker(a,b,c)
if(valid is True):
	semi_perimeter = geometry.perimeter(a,b,c)
	area_of_the_triangle = geometry.triangle_heronsarea(a,b,c)
	print("Perimeter: ", "%.2f" %  round(semi_perimeter,2))
	print("Area: ", "%.2f" % round(area_of_the_triangle,2))
else:
	print("Invalid Input")
