

#CA 4 Part A
# student number 1604233


#print
#print ("WellCome to My Calculater")
#print


#1 defined Addition function

add <- function (x,y){
  return (paste("The sum of the two numbers", (x+y)))}

# calles for the Function

add (1,5)
add (10,15)
add (-10,-5)
add (100,-1)
add (-300,-1)


#2 defined substraction function		

subtract <- function (x,y){
  return (paste("Subtracting First number from Second ", (x-y)))}

# calles for the Function

subtract (15,19)
subtract (-100,300)
subtract (-10,-30)
subtract (4.0,5.3)

#3 Defined multiply function 

multiply <- function (x,y){
  return(paste("The Multplication of two numbers is", (x*y)))}

# calles for the Function

multiply (19,20)
multiply (0,3)
multiply (-1,-1)
multiply (19,-1)
multiply (45,-1)
multiply (34,0)
multiply (2.3,5.3)

#4 defined divison function 

divide <- function (x,y){
  return(paste("Divison of X into  Y  is  ", (x/y)))}

# calles for the Function


divide (15,15)
divide (9,3)
divide (-2,1)
divide (-1,-1)
divide (45,-55)



#5 defined square function

square <- function (x){
  return(paste("The sum of square is", (x*x)))}

# calles for the Function

square (5)
square (15)
square (-25)
square (0)
square (10.5)

#6 Defined Cube function 
Cubeof <- function (x){
  return(paste("The Cube of any given number ", (x*x*x)))}

Cubeof (3)
Cubeof (5)
Cubeof (-6)

#7 Defined Cuberoot  function
cuberoot <- function (x)
{return(paste("The Cuberoot of number x is", (x**0.3333)))}

cuberoot (10)
cuberoot (5)
cuberoot (1)
cuberoot (5.4)

#8 square root of a number function

square_root <- function (x){
  return(paste("The squareroot of number x is", (x**0.5)))}

square_root (5)
square_root (7)
square_root (15)
square_root (3)


#9 Defined Exponent of a number function
Exponent <- function (x,y){
  return(paste("The Exponent of number x is", (x**y)))}

#call The function

Exponent (3,7)
Exponent (-3,-7)
Exponent (1,1.3)


#10 Remainder function

Remainder <- function (x,y)
{return(paste("The result of numbers Remainder is", (x%%y)))}

# call the Function

Remainder (11,5)
Remainder (24,5)
Remainder (16.5,5)
