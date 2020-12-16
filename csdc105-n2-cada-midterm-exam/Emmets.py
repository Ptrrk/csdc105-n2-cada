class Emmet: # cointains the main method which represents the whole program it is also could be the name for your module.
	def __init__(self, raw): # initializes self and raw that can be accessed
		self.raw = raw # an attribute that is also accessible
		self.ParentChild() # an attribute that is also accessible

	def ParentChild(self): # string representation of the object
		ParentBranch = self.raw.split("+") # stores and splits the raw whenever there is a "+" symbol.
		self.HTML(ParentBranch) # html variable stores the output.

	def HTML(self, ParentBranch): # string representation of the object
		for i in range(len(ParentBranch)): # for loop of the output
			Branch = ParentBranch[i].split(">")
			z = 0
		while z < len(Branch): # semi length checker for proceeding
			print(("   "*i)+ "<" + Branch[z] + ">")
			z +=1
		for k in range(len(Branch),0,-1):
			print(("   "*k-1)+ "<" + Branch[k-1] + ">")

class Checker: # checker of true
	def __init__(self,raw):
		self.raw = raw
		self.inputChecker()

def inputChecker(self): # the checker of signs
		valid = ["+", ">"]
		while(True):
			if self.raw and all(word in valid for word in self.raw):
				return True
		self.raw = self.raw.replace('div','')
		self.raw = self.raw.replace('nav','')
		self.raw = self.raw.replace('span','')
		self.raw = self.raw.replace('p','')
		if self.raw == '':
			return True
		else:
			return False
