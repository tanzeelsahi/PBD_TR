


from carsforrent import Car,PetrolCar,DieslCar,ElectricCar,HybridCar,Customer


class DbsCarRental(object):

	def __init__(self):
		self.petrol_cars = []
		self.Diesl_cars   =[]
		self.electric_cars = []
		self.Hybrid_cars = []
		self.Customer = []
	def create_current_stock(self):
		for i in range(20):
			self.petrol_cars.append(PetrolCar())
		for i in range(8):
			self.Diesl_cars.append(DieslCar())
		for i in range(4):
			self.electric_cars.append(ElectricCar())
		for i in range(8):
			self.Hybrid_cars.append(HybridCar()) 		

	def stock_count(self):
		print 'petrol cars in stock ' + str(len(self.petrol_cars))
		print 'Diesl  cars in stock ' + str(len(self.Diesl_cars))
		print 'electric cars in stock ' + str(len(self.electric_cars))
		print 'Hybrid cars in stock ' + str(len(self.Hybrid_cars))

	def rent(self, car_list, amount):
		if len(car_list) < amount:
			print 'Not enough cars in stock'
			return
		total = 0
		while total < amount:
			car_list.pop()
			total = total + 1
			
			
	def process_rental(self):
		answer = raw_input('would you like to rent a car? y/n')
		if answer == 'y':
			answer = raw_input('what type would you like? p/d/e/h')
			amount = int(raw_input('how many would you like?'))
			if answer == 'p':
				self.rent(self.petrol_cars, amount)
			elif answer == 'd':
				self.rent(self.Diesl_cars, amount)
			elif answer == 'e':
				self.rent(self.electric_cars, amount)
			else:
				self.rent(self.Hybrid_cars, amount)
			self.stock_count()
			
	def returnCar(self,car_list,amount):
		
			self.stock_count += numCars
			print('Available ' + str(slef.stock_count))


	def process_return(self):
		answer = raw_input('would you like to return a car? y/n')
		if answer == 'y':
			answer = raw_input('what type would you like return? p/d/e/h')
			amount = int(raw_input('how many would you like return?'))
			
			if answer == 'p':
				self.returnCar(self.petrol_cars, amount)
			elif answer == 'd':
				self.returnCar(self.Diesl_cars, amount)
			elif answer == 'e':
				self.returnCar(self.electric_cars, amount)
			else:
				self.returnCar(self.Hybrid_cars, amount)
			self.stock_count()
			print self.stock_count()

dbsCarRental = DbsCarRental()
dbsCarRental.create_current_stock()
dbsCarRental.stock_count()
proceed = 'y'
while proceed == 'y':
	
	dbsCarRental.process_rental()
	dbsCarRental.process_return()
	proceed = raw_input('continue? y/n')

