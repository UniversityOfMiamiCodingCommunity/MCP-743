# When you are stuck or need to explore something new start here:
# https://docs.python.org/3/tutorial/
# Also, Stackoverflow is a great resource: 
# http://stackoverflow.com
#################################################################

############################################################################################################
# Throughout these tutorials, you may have to add your own print statements to see the results of the code.
############################################################################################################

# Classes (also known as objects)
# If you need help or need to explore something new regarding classes start here: https://docs.python.org/3/tutorial/classes.html
##################################################################################################################################

# A Class for cars.
####################
class Car:

	def __init__(self):

		# Class attributes that describe the object.
		############################################
		self.year = None
		self.make = None
		self.model = None
		self.color = None

	# A class method, i.e. a function, that takes class attributes as arguments.
	############################################################################
	def printAttributes(self):

		if self.year:
			print("Year built:", self.year)
		if self.make:
			print("Make of car:", self.make)
		if self.model:
			print("Model of car:", self.model)
		if self.color:
			print("Color of car", self.color)


# Create instance, i.e. copy, of the Car class to store the details of my car.
##############################################################################
dansCar = Car()
dansCar.year = 2002
dansCar.make = "Honda"
dansCar.model = "Civic"
dansCar.color = "Silver"
dansCar.printAttributes()

# Create an instance for my other car...
########################################
dansOtherCar = Car()
dansOtherCar.year = 2017
dansOtherCar.make = "Lamborghini"
dansOtherCar.model = "Centenario"
dansOtherCar.color = "Black"
dansOtherCar.printAttributes()



