import unittest

from carsforrent import Car,PetrolCar,DieslCar,ElectricCar,HybridCar,Customer

# test the car functionality
# test the car functionality
class TestCar(unittest.TestCase):

    def test_petrol_car_cylinder(self):
		petrol_car = PetrolCar()
		self.assertEqual(1, petrol_car.getNumberCylinders())
		petrol_car.setNumberCylinders(4)
		self.assertEqual(4, petrol_car.getNumberCylinders())



    def test_diesl_car_cylinder(self):
		diesel_car = DieslCar()
		self.assertEqual(1, diesel_car.getNumberDieselCylinders())
		diesel_car.setNumberDieselCylinders(4)
		self.assertEqual(4, diesel_car.getNumberDieselCylinders())

    def test_hybrid_car_fuel_cells(self):
		hybrid_car = HybridCar()
		self.assertEqual(1, hybrid_car.getNumberFuelCellsCylinders())
		hybrid_car.setNumberFuelCellsCylinders(4)
		self.assertEqual(4, hybrid_car.getNumberFuelCellsCylinders())

    def test_electric_car_fuel_cells(self):
		electric_car = ElectricCar()
		self.assertEqual(1, electric_car.getNumberFuelCells())
		electric_car.setNumberFuelCells(4)
		self.assertEqual(4, electric_car.getNumberFuelCells())



if __name__ == '__main__':
    unittest.main()
