

class Car(object):
    # implement the car object.
    
	def __init__(self):
		self.__colour = ''


	def getColour(self):
		return self.__colour


class PetrolCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberCylinders = 1

	def getNumberCylinders(self):
		return self.__numberCylinders

	def setNumberCylinders(self, value):
		self.__numberCylinders = value

		
class DieslCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberDieselCylinders = 1

	def getNumberDieselCylinders(self):
		return self.__numberDieselCylinders

	def setNumberDieselCylinders(self, value):
		self.__numberDieselCylinders = value


class ElectricCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberFuelCells = 1

	def getNumberFuelCells(self):
		return self.__numberFuelCells

	def setNumberFuelCells(self, value):
		self.__numberFuelCells = value

		
class HybridCar(Car):

	def __init__(self):
		Car.__init__(self)
		self.__numberFuelCellsCylinders = 1

	def getNumberFuelCellsCylinders(self):
		return self.__numberFuelCellsCylinders

	def setNumberFuelCellsCylinders(self, value):
		self.__numberFuelCellsCylinders = value	


class Customer(object):

	def __init__(self):
		self.__number = ''
	


