  # Author          : Patrick James Cada
   # Course and Year : BSIT - 2ndyear
   # Filename        : cada_e2.py
   # Description     : Shows information about my self.
   # Honor Code      : I have not given nor received any unathorized help in
   #                   completing this exercise. I am also well aware of the 
   #                   policies stipulated in the AdNU student handbook.

data = {"Name": "Patrick James R. Cada.", "Animal": "Panda.", "Reason": "i always want to just sleep and eat.", 
	  "Hobbies": ["Play Computer Games","Play Ukulele","Hanging out with friends."],
	  "Profession":"Flight Attendant or Programmer/Web Developer"}  


print("I am " + data["Name"])
print("My spirit animal is " + data["Animal"])	
print("because " + data["Reason"])
print("When not in School, I love to:")
for i in range(3):
	print("*" + data["Hobbies"][i]) 
print("I dream of being a/an " + data["Profession"] + " in the future.")
