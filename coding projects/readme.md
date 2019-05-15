# Descriptions of projects for Master Python Course

The massive headline pretty much said it all. Anyhoo, below is a comprehensive summary of all of the ~~cool~~ coding projects that accompanies the Master Python course.


# Project #1: Text Based Calculator

In this project you'll build a text based calculator that emulates the functionality of a scientific calculator. Below are the features that should be emulated:
addition

 - subtraction 
 - multiplication 
 - division 
 - modulus 
 - square root 
 - exponential
 - basic trigonometry: shows sin(), cos(), tan() results for a number
   entered both in radians and degrees. 
 - logarithm

Since I didn't teach functions yet don't worry about making the code modular. Instead, just get the program to work. Here's some code to get you started:

    '''
    
    addition operation
    
    '''
    
    a1 = float(input('Addition. Enter first number '))
    
    a2 = float(input('Enter second number '))
    
    a3 = a1 + a2
    
    print(a1, '+', a2, '=', a3)

Also, here's a test case so that you can verify that the code works:

    Addition. Enter first number 10
    Enter second number 10
    10.0 + 10.0 = 20.0
    Subtraction: Enter first number 20
    Enter second number 100
    20.0 - 100.0 = -80.0
    Multiplication: Enter first number 100
    Enter second number 100
    100.0 x 100.0 = 10000.0
    Division: Enter first number 5
    Enter second number 2
    5.0 / 2.0 = 2.5
    Modulus: Enter first number 10
    Enter second number 3
    10.0 % 3.0 = 1.0
    Square root: Enter number to take square root of 9
    √ 9.0 = 9.0
    Exponentiation. Enter a number for the 'base' 10
    Enter the power 3
    10.0 ^ 3 = 1000.0
    Enter number to compute, sin, cos, and tan of 115.5
    0.9025852843498607 ° sine
    0.6734960211850264 r sine
    -0.4305110968082949 ° cosine
    -0.7391908477842096 r cosine
    -2.0965435990881756 ° tangent
    -0.9111260281480631 r tangent
    Logarithm. Enter the value of x 9
    Enter the base 2
    log base 2.0 of 9.0 = 3.1699250014423126


Once done, name the program *py_text_calculator.py* and upload to your GitHub account. Congrats on taking steps to improving your python programming skills!
