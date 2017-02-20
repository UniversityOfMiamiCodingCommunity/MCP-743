###############################
#Classes and Functions
###############################

#1 Create a function from equations

def Newtons_Second_Law(m,a):
	"""Newtons Second Law"""
	Force= m*a
	print ("the force of an object with mass %d kg and acceleration %d m/s^2 is %d Newtons." %(m, a, Force))

Newtons_Second_Law(6,20)

def heat_transfer(m, C, T):
	"""Used to calculate amount of heat (q) in a substance"""
	Q= m*C*T
	#m= mass of substance in kg
	#C= specific heat of substance
	#T= change in temperature in Kelvin (K)
	print ("The heat of this substance is:", Q, "joules")
	
heat_transfer(10,2,15)



#2 Create a class 

class Anemias():
	"""Classification of different anemias"""
	def __init__(self, MCV, retic_count):
		self.MCV= MCV
		self.retic_count= retic_count
	
	def type(self):
		"""is the anemia microcytic or macrocytic?"""
		if  self.MCV < 80:
			return ("this type of anemia is microcytic")
		elif self.MCV > 100:
			return ("This type of anemia is macrocytic")
		else:
<<<<<<< HEAD
			return ("this type if anemia is normocytic")
=======
			print ("this type if anemia is normocytic")

>>>>>>> origin/Derek
	def erythropoesis(self):
		"""is the anemia characterized by reduced/increased rbc production?"""
		if self.retic_count > 1.5:
			return ("This anemuia has increased erythropoesis")
		elif self.retic_count < 0.5:
			return ("This anemia has decreased erythropoesis")
		else:
			return ("This anemia appears to have normal eryhthropoesis")

patient1_anemia= Anemias(85, 1.0)
<<<<<<< HEAD

print (patient1_anemia.type()) 
print (patient1_anemia.erythropoesis())
 
=======
print (patient1_anemia.type())
>>>>>>> origin/Derek
