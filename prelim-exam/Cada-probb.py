# Author : Patrick James R. Cada
# Course and Year : BSIT - 2nd
# Filename : Cada-probb.py
# Description : Outputs a fibonacci number depends on the users input number.
# Honor Code : I have not given nor received any unathorized help in
# completing this exercise. I am also well aware of the
# policies stipulated in the AdNU student handbook.


T = int(input())
output = ""	

i = 1
while i <= T:
	fibo = int(input()) 
	a = 0
	b = 1
	
	output += ("CASE " + str(i) +": ") #how many cases you input
	c = 0
	while c < fibo+1:
		output += (str(a)+",")	
		Fn = a + b	#adding both putting it in the Fn cont
		a = b
		b = Fn	
		c+=1
		
	if output.endswith(","):	
		output = output[:-1]	#output of the numbers that reads to -1 loc
		output += ("\n")
	i+=1
print("\n"+output)

