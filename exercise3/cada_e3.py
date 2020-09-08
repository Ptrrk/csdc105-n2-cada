# Author          : Patrick James Cada
   # Course and Year : BSIT - 2ndyear
   # Filename        : cada_e3.py
   # Description     : Shows the rules of each classification of the quarantine levels.
   # Honor Code      : I have not given nor received any unathorized help in
   #                   completing this exercise. I am also well aware of the 
   #                   policies stipulated in the AdNU student handbook.
   
import sys

try:
	activityOrsector = sys.argv[1].lower()    # reading first arg.
	classification = sys.argv[2].lower() #reading second arg.

except:
	print("Usage: python3 <program-name> <activity-or-sector> <quarantine-classification> ")
	sys.exit()

#i put spaces in every ifelse so it is easier to check even though it is not needed.
#for people
if activityOrsector == "people" and classification == "ecq":
		print("100% stay at home; Exception for workers in offices or industries permitted to operate.")
	
elif activityOrsector == "people" and classification == "mecq":
		print("100% stay at home; Restricted movement, only for accessing essential goods and services; Exception for workers in offices or industries permitted to operate; Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home.")
	
elif activityOrsector == "people" and classification == "gcq":
		print("Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home.")
	
elif activityOrsector == "people" and classification == "mgcq":
		print("Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home.")
	

	
		

#for transport
elif activityOrsector == "transport" and classification == "ecq":
		print("No domestic flights, with limited international flights; Public transportation is not allowed; Shuttle services for employees of permitted offices or establishments, as well as point-to-point transport service, granted permission to operate by the government, with healthcare workers and other frontliners given priority.")
	
elif activityOrsector == "transport" and classification == "mecq":
		print("No domestic flights, with limited international flights; Controlled inbound flights; No inter-island travel; Public transportation is not allowed; Private transportation such as company shuttles and personal vehicles allowed subject to the guidelines provided by the Department of Transportation (DOTr); Biking and non-motorized transport encouraged.")
	
elif activityOrsector == "transport" and classification == "gcq":
		print("Public transport is allowed with strict social distancing; Inter-island travel from GCQ to GCQ allowed with safety protocols.")
	
elif activityOrsector == "transport" and classification == "mgcq":
		print("Public transport is allowed with strict social distancing Inter-island travel from GCQ to GCQ allowed with safety protocols.")
	

	
	
	
#for gatherings
elif activityOrsector == "gatherings" and classification == "ecq":
		print("Mass gatherings are not allowed; Only mass gatherings that are essential for the provision of government services or authorized humanitarian activities permitted.")
	
elif activityOrsector == "gatherings" and classification == "mecq":
		print("Highly restricted (maximum of 5); Non-essential work gatherings are prohibited.")
	
elif activityOrsector == "gatherings" and classification == "gcq":
		print("Gatherings are limited to not more than ten (10) persons; Non-essential work gatherings are prohibited.")
	
elif activityOrsector == "gatherings" and classification == "mgcq":
		print("Fifty percent (50%) of the seating or venue capacity for movie screenings, concerts, sporting events, and other entertainment activities, religious services, and work conferences.")
	

	
	
	
#for schools
elif activityOrsector == "schools" and classification == "ecq":
		print("School premises are closed.")
	
elif activityOrsector == "schools" and classification == "mecq":
		print("School premises are closed.")
	
elif activityOrsector == "schools" and classification == "gcq":
		print("Skeletal workforce permitted in schools; Face-to-face or in-person classes are suspended.")
	
elif activityOrsector == "schools" and classification == "mgcq":
		print("Limited face-to-face or in-person classes may be conducted; strict compliance with minimum public health standards and consultations with local government units (LGUs) and guidelines set by the Commission on Higher Education (CHED).")
	

	
	
		
	
#for work rules.
elif activityOrsector == "work" and classification == "ecq":
		print("Select industry workers permitted.")
	
elif activityOrsector == "work" and classification == "mecq":
		print("Essential industries permitted to work at full capacity, with others operating at a fifty percent (50%) capacity; Work-from-home and other flexible work arrangements encouraged.")
	
elif activityOrsector == "work" and classification == "gcq":
		print("Alternative work arrangements.")
	
elif activityOrsector == "work" and classification == "mgcq":
		print("Full operating capacity for work in all public and private offices; Alternative work arrangements for persons who are sixty (60) years old and above, or those with other health risks.")
	

		
	
#for government rules
elif activityOrsector == "government" and classification == "ecq":
		print("Skeletal workforce onsite; Work from home arrangements.")
	
elif activityOrsector == "government" and classification == "mecq":
		print("Skeletal workforce onsite; Work from home arrangements.")
	
elif activityOrsector == "government" and classification == "gcq":
		print("Work in all government offices under alternative work arrangements.")
	
elif activityOrsector == "government" and classification == "mgcq":
		print("Work in government offices may be at full operational capacity, or under alternative work arrangements  Exercise and Sports.")
	
else: 
	      print("Error: Input is Invalid!")
