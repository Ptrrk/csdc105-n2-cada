# Author          : {Patrick James R. Cada}
# Course and Year : {BSIT - 2}
# Filename        : {geometry.py}
# Description     : {the formula/function for computing}
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

import math
import sys
def perimeter(*side_lengths):
	P = 0
	for n in side_lengths:
		P += n
	return P
def triangle_heronsarea (a,b,c):
	s = (perimeter(a,b,c))/(2)
	heronsarea = math.sqrt(s*(s-a)*(s-b)*(s-c))
	return heronsarea
def Checker(a,b,c):
	if ((a+b) < c) or ((b+c) < a) or ((a+c) < b):
		return False
	else:
		return True
