# Author : Patrick James R. Cada
# Course and Year : BSIT - 2nd
# Author : Patrick James R. Cada
# Course and Year : BSIT - 2nd
# Filename : Cada-probc
# Description : Reads the if the ip you input is valid or not.
# Honor Code : I have not given nor received any unathorized help in
# completing this exercise. I am also well aware of the
# policies stipulated in the AdNU student handbook.

T = int(input())
output = ""			
Validate = "n"		
for n in range(0, T):	
	enterIP = input()	#enter the ip's
	for a in range(0, 4):
		b = int(enterIP.split(".")[a])	
		if b >= 0 and b <= 500:
			Validate = "y"			#if yes	or no for the constraints.
		else:
			Validate = "n"			
			break
	output += ("CASE "+ str(n+1) +": ")	#the amount of cases you entered.	
	if Validate == "y":
		output += ("VALID\n")		#output for valid
	elif Validate == "n":
		output += ("INVALID\n")		#output for invalid
print("\n"+output)
