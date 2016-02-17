# Author: Giancarlo Rosa
# Purpose: This program will take the user's values in standard form, and display
#          the answer to the quadratic formula.
# Status: COMPLETE

import math

# DOCU: Lines 11-16 will print a welcome statement, as well as credits to the program
# author.

print( "" )
print( "" )
print( "Welcome to the Quadratic Formula Calculator!" )
print( "(c) 2016 Giancarlo Rosa" )
print( "" )
print( "" )

# DOCU: Line 22-26 will ask the user how many equations need to be solved. The
# user's input will be assigned to the variable "numOfEquations". If an invalid
# number is entered, the program will ask the user to verify their input.

numOfEquations = eval(input( "How many quadratic equations would you like to solve?: " ) )
while ( numOfEquations < 1 ):
    print( "Please enter a number larger than 0." )
    print( "" )
    numOfEquations = eval(input( "How many quadratic equations would you like to solve?: " ) )

# DOCU: Lines 30-31 will prepare setup for a loop. 

startingNumber = 1
equationNumber = startingNumber

# DOCU: Lines 36-59 will collect the user's values, solve the equation, and print
# an answer. 

while (( equationNumber >= 1 ) and ( equationNumber <= numOfEquations )):
    aValue = eval(input( "Please enter the value of 'a' in equation #" + str(equationNumber) + ": " ))
    if ( aValue == 0 ):
        while ( aValue == 0 ):
            print( "This equation is not quadratic." )
            aValue = eval(input( "Please enter the value of 'a' in equation #" + str(equationNumber) + ": " ))
    bValue = eval(input( "Please enter the value of 'b' in equation #" + str(equationNumber) + ": " ))
    cValue = eval(input( "Please enter the value of 'c' in equation #" + str(equationNumber) + ": " ))
    discriminent = bValue * bValue - 4 * aValue * cValue
    if ( discriminent < 0 ):
        print( "There is no solution because you can not square root a negative." )
        print( "The discriminent is", str(discriminent) + "." )
    elif ( discriminent == 0 ):
        denominator = 2 * aValue
        solution = ( ( bValue / -1 ) + math.sqrt( discriminent ) ) / denominator
        print( "There is only one root. The root is", str(solution) + "." )
        print( "The discriminent is", str(discriminent) + "." )
    else:
        denominator = 2 * aValue
        xValueOne = ( ( bValue / -1 ) + math.sqrt( discriminent ) ) / denominator
        xValueTwo = ( ( bValue / -1 ) - math.sqrt( discriminent ) ) / denominator 
        print( "There are two roots. The first root is", str(xValueOne), "and the second root is", str(xValueTwo) + "." )
        print( "The discriminent is", str(discriminent) + "." )
    equationNumber = equationNumber + 1
    
# DOCU: Lines 63-68 will print a goodbye and credit message.

print( "" )
input( "Press <enter> to finish." )
print( "" )
print( "Thank you for using the Quadratic Equation Calculator!" )
print( "(c) 2016 Giancarlo Rosa" )
print( "https://github.com/giancarloarosa" )
