import unittest

from ListCalculater import (addMap,addReduce,addfilter,SubtractMap,SubtractReduce,MultiplyMap,MultiplyReduce,divideMap,divideReduce
,ExponentMap,ExponentReduce,MaxMap,MinReduce,SquareMap)

class TestCalculator(unittest.TestCase):
	def testAddMap(self):
	
		self.assertEqual([4,0],addMap([2,0],[2,0]))
		self.assertEqual([-4,0],addMap([-2,0],[-2,0]))
		self.assertEqual([0,0],addMap([2,0],[-2,0]))

	def testaddReduce(self):
		self.assertEqual(3,addReduce([1,2]))
		self.assertEqual(-4,addReduce([-2,-2]))

	def testaddfilter(self):
		self.assertEqual([4],addfilter([1,3,4,5]))

	def testSubtractmap(self):
		self.assertEqual([0,1],SubtractMap([2,5],[2,4]))
		self.assertEqual([4,3],SubtractMap([2,5],[-2,2]))
		self.assertEqual([4,0],SubtractMap([2,0],[-2,0]))
	
	def testSubtractReduce(self):
		self.assertEqual(0,SubtractReduce([2,2]))
		self.assertEqual(6,SubtractReduce([4,-2]))
		
	def testMultiplyMap(self):
		self.assertEqual([4,20],MultiplyMap([2,5],[2,4]))
		self.assertEqual([-4,10],MultiplyMap([2,5],[-2,2]))
		
	
	def testMultiplyReduce(self):
		self.assertEqual(4,MultiplyReduce([2,2]))
		self.assertEqual(-8,MultiplyReduce([4,-2]))
		
	def testDivisonMap(self):
		self.assertEqual([1,5],divideMap([2,10],[2,2]))
		self.assertEqual([-1,2],divideMap([2,-6],[-2,-3]))
		
	
	def testDivisonReduce(self):
		self.assertEqual(1,divideReduce([2,2]))
		self.assertEqual(-2,divideReduce([4,-2]))
	
	
	def testExpontMap(self):
		self.assertEqual([4,625],ExponentMap([2,5],[2,4]))
		
		
	
	def testExpontReduce(self):
		self.assertEqual(4,ExponentReduce([2,2]))
	
	def testMaxMap(self):
		self.assertEqual([2,4],MaxMap([2,3],[1,4]))
		
	def testMinReduce(self):
		self.assertEqual(2,MinReduce([2,3]))
		
	def testsequarMap(self):
		self.assertEqual([4,16],SquareMap([2,4]))
		
	




if __name__=='__main__':
	unittest.main()
