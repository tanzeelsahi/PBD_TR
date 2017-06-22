# define a class for a car

class Car:
	## 
	
	def __init__(self):
		self.__make = 'Ferriri'
		self.__colour = 'Red'
		self.__mileage = 0
		self.engineSize = '5.41'
		
	def getMake(self):
		return self.__make
		
	def getcolour(self):
		return self.__colour
		
	def getmileage(self):
		return self.__mileage
		
	def setMake(self,make):
		self.__make = make
		
	def setmileage(self, mileage):
		self.__mileage = mileage
		
	def setcolour(self, colour):
		self.__colour = colour
		
	def move(self,distance):
		print ('car has moved' + str(distance) + 'kms.')
		self.__mileage = self.__mileage + distance
	
	def paint(self,colour):
		print('getting a paint job - new clour is : ' + colour)
		self.__colour = colour
	
class ElectricCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberFuelCelles = 1

	def getNumberFuelCelles(self):
		return self.__numberFuelCelles
		
	def setNumberFuelCells(self,Valu):
		self.numberFuelCelles = Valu
		

		
		



