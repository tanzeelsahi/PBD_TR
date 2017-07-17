import math

# Calculator handling lists

print 'Wellcome to my Calculator'
print
print

# 1 defined functions for addition
	
def addMap(First_List, Second_List):
	return map(lambda x, y: x+y, First_List, Second_List)
	
def addReduce(First_List):
    return reduce(lambda x, y: x+y, First_List)	
	
def addfilter(First_List):
	return filter(lambda x: x%2==0, First_List)
	

	
# 2 defined fuctions for subtraction 

def SubtractMap(First_List, Second_List):
	return map(lambda x, y: x-y, First_List, Second_List)
	
def SubtractReduce(First_List):
    return reduce(lambda x, y: x-y, First_List)	
	
def Subtactfilter(First_List):
	return filter(lambda x: x%2==0, First_List)
	
# 3 defined fuctions for Multiplication 

def MultiplyMap(First_List, Second_List):
	return map(lambda x, y: x*y, First_List, Second_List)
	
def MultiplyReduce(First_List):
    return reduce(lambda x, y: x*y, First_List)	
	
def Multiplyfilter(First_List):
	return filter(lambda x: x%2==0, First_List)

	
# 4 defined fuctions for Division 

def divideMap(First_List, Second_List):
	return map(lambda x, y: x/y, First_List, Second_List)
	
def divideReduce(First_List):
    return reduce(lambda x, y: x/y, First_List)	
	
def dvidefilter(First_List):
	return filter(lambda x: x%2==0, First_List)


# 5 Exponent defined fuctions

def ExponentMap(First_List, Second_List):
	return map(lambda x, y: x**y, First_List, Second_List)
	
def ExponentReduce(First_List):
    return reduce(lambda x, y: x**y, First_List)	
	
def Exponentfilter(First_List):
	return filter(lambda x: x%2, First_List)
	
# 6 defined fuctions for Cube 

def CubeMap(First_List, Second_List):
	return map(lambda x,: x*x*x, First_List)
	

	
def Cubefilter(First_List):
	return filter(lambda x: x%2, Second_List)
	

# 7  defined fuctions for Max Value in the List

def MaxMap(First_List, Second_List):
	return map(lambda x, y: x if (x>y) else y,First_List, Second_List)
	
def MaxReduce(First_List):
    return reduce(lambda x, y: x if (x>y)else y, First_List)	
	
def Maxfilter(First_List):
	return filter(lambda x: x%2, First_List)



# 8  defined fuctions for Min Values in the List

def MinMap(First_List, Second_List):
	return map(lambda x, y: x if (x<y) else y,First_List, Second_List)
	
def MinReduce(First_List):
    return reduce(lambda x, y: x if (x<y)else y, First_List)	
	
def Minfilter(First_List):
	return filter(lambda x: x%2, First_List)

# 9  defined fuctions for square of Values in the List

def SquareMap(First_List):
	return map(lambda x: x*x,First_List)
	
	
def Squarefilter(First_List):
	return filter(lambda x: x%2, First_List)	
	
# 10  defined fuctions for squareRoot of Values in the List

def SquareRootMap(First_List):
	return map(lambda x: x**0.5,First_List)
	

	
def SquareRootfilter(First_List):
	return filter(lambda x: x%2, First_List)



# validation routine for input and printing  output:
invalid = 1
while invalid == 1:
	invalid = 0 	
	if __name__ == '__main__':
		try:
			x = int(raw_input('who many numbers are in your First list? 	'))
			First_List  = []
			for i in range (x):
				First_List.append(int(raw_input("Enter Number: " )))
			y = int(raw_input('who many numbers are in your Second list	'))
			Second_List = []
			for i in range (y):
				Second_List.append(int(raw_input("Enter Number: " )))
			print
			print
			print 'Ans addition map			',addMap(First_List, Second_List)
			print 'Ans additin Reduce			',addReduce(First_List)
			print 'Ans addition FILTER			',addfilter(First_List)	
			print
			print 'answers for subtraction'
			print
			print 'Ans Subtraction map			',SubtractMap(First_List, Second_List)
			print 'Ans subtraction Reduce			',SubtractReduce(First_List)
			print 'Ans subtraction filter			',Subtactfilter(First_List)
			print
			print 'answers for Multiplication'
			print
			print 'Ans Multiplication map			',MultiplyMap(First_List, Second_List)
			print 'Ans Multiplication Reduce		 ',MultiplyReduce(First_List)
			print 'Ans Multiplication filter			',Multiplyfilter(First_List)
			print
			print 'answers for Division'
			print
			print 'Ans Division map			',divideMap(First_List, Second_List)
			print 'Ans Division Reduce			',divideReduce(First_List)
			print 'Ans Division filter			',dvidefilter(First_List)
			print
			print 'answers for Exponent'
			print
			print 'Ans Exponent map			',ExponentMap(First_List, Second_List)
			print 'Ans Exponent Reduce			',ExponentReduce(First_List)
			print 'Ans Exponent filter			',Exponentfilter(First_List)
			print
			print 'answers for Cube'
			print
			print 'Ans Cube map			',CubeMap(First_List,First_List)
			print 'Ans Cube filter			',Cubefilter(Second_List)
			print
			print 'answers for Max '
			print
			print 'Ans Max map			',MaxMap(First_List, Second_List)
			print 'Ans Max Reduce		 ',MaxReduce(First_List)
			print 'Ans Max filter			',Maxfilter(First_List)
			print
			print 'answers for Min '
			print
			print 'Ans Min map			',MinMap(First_List, Second_List)
			print 'Ans Min Reduce		 ',MinReduce(First_List)
			print 'Ans Min filter			',Minfilter(First_List)
			print
			print 'answers for Square '
			print
			print 'Ans Square map			',SquareMap(First_List)
			print 'Ans Square filter			',Squarefilter(First_List)
			print
			print 'answers for SquareRoot '
			print
			print 'Ans SquareRoot map			',SquareRootMap(First_List)
			print 'Ans SquareRoot filter			',SquareRootfilter(First_List)
		except ValueError:
			print 'Enter number only'
			invalid = 1 
















			
