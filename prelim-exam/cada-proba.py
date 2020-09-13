# Author : Patrick James R. Cada
# Course and Year : BSIT - 2nd
# Filename : Cada-proba.py
# Description : Prints a triangle/pyramid shape of the sign that you will put
# Honor Code : I have not given nor received any unathorized help in
# completing this exercise. I am also well aware of the
# policies stipulated in the AdNU student handbook.

T = int(input())
output = ""
case = 1 #counter for how many cases you want.
while case <= T:
	k,c = input().split() #number for the rows and ASCII to be printed.
	k = int(k)
	output += "CASE: " + str(case) + "\n"	#case str
	for r in range(0,k):
		for space in range(0,k-r-1):	#loop for the output of the pyramid.
			output +=" "
		for j in range(0,2*r+1):
			output +=str(c) 
		output += '\n'
	case += 1
print(output)
