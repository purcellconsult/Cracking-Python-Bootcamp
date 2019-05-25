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
    √ 9.0 = 3.0
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



## Project #2: The Dice Simulator
    
Write a program that asks the user to enter the number of games that they want to play. This number should be within the range of 1-20. Once this number is entered the user will then be asked to select a number within the range of 1-6 which models the different sides of a dice.

  Depending on the number of games the user pick, the program will run that many times. During each round the program will tell the user if they won the game or not. However, to add a bit of theatrics make the program pause for three seconds before delivering the message to the user if they won or not. The program will also keep some simple game stats.

 Once the program finishes the stats of how the dice landed should be recorded. Keep track of the number of occurrences for each side that the dice landed on. Print these stats along with the average percentage of accuracy of the user’s guesses at the end of the program.

  To read in random numbers use the randint function in the random module:



    from random import randint
    dice_result = randint(1, 6)

  

To make the program pause for x amount of seconds use the sleep() function in the time module:

  

    from time import sleep
    sleep(3)

  
To keep track of the number of occurrences of each side of the dice, consider using the dictionary data structure:

    dice_numbers = {
      1: 0,
      2: 0,
      3: 0,
      4: 0,
      5: 0,
      6: 0,
    
    }

  

To update the dictionary you could use a conditional:

      if dice_result == 1:
      dice_numbers[1] += 1

 

 ### Sample Input/Output for Dice Simulator:
    


    How many rounds you want to play? Enter a number from 1-20: 5
    
    round: 1
    
    Roll the dice. Enter a number from 1-6... 1
    
    Dice rolling...
    
    You win! The dice landed on 1
    
    round: 2
    
    Roll the dice. Enter a number from 1-6... 6
    
    Dice rolling...
    
    Better luck next time. Dice landed on 3
    
    round: 3
    
    Roll the dice. Enter a number from 1-6... 3
    
    Dice rolling...
    
    Better luck next time. Dice landed on 4
    
    round: 4
    
    Roll the dice. Enter a number from 1-6... 5
    
    Dice rolling...
    
    Better luck next time. Dice landed on 4
    
    round: 5
    
    Roll the dice. Enter a number from 1-6... 2
    
    Dice rolling...
    
    Better luck next time. Dice landed on 5
    
    Dice landed on 1: 1 times
    
    Dice landed on 2: 0 times
    
    Dice landed on 3: 1 times
    
    Dice landed on 4: 2 times
    
    Dice landed on 5: 1 times
    
    Dice landed on 6: 0 times
    
    Correct guesses: 1
    
    Average of correct guesses 0.2

  
Check for edge cases. Therefore, the program should terminate if user enters a range outside of the scope of 1-20 or 1-6.

  
### Edge case 1:
    

How many rounds you want to play? 

    Enter a number from 1-20: -1
    
    Invalid input. Exiting program...
    
    Process finished with exit code 0


### Edge case 2:
    
How many rounds you want to play? 

    Enter a number from 1-20: 21
    
    Invalid input. Exiting program...
    
    Process finished with exit code 0

  
  ## Project #3: The Secret Number
    
This is a simple number guessing game. The purpose of this game is to guess a number within the range of 1-100. Depending on the mode the user selects the program will execute two separate branches.

The first option allows the user to play the game an unlimited number of times until the correct guess is received. The second option is more challenging. If selected the user will be given an arbitrarily number of chances within the range of 1-10 to guess the secret number.

During each guess in both branches, the user should be given feedback on their guess. The program should tell if their guess is less than, greater than, or equal to the secret number. If it’s equal then the program terminates and the following is printed:


The secret numbers

-   Number of tries

-   Max number guessed

-   Min number guessed

-   Summation of all the numbers

-   The average of all of the numbers

    
If the user doesn’t guess the secret number within the allocated number of chances, then the above stats will still be displayed at the end. Make sure to check for edge cases and terminate the program if they’re triggered. Here’s some sample input/output from the program:

  

### Sample Input/Output #1:
    

     Do you want unlimited tries? Enter 'y' or 'n' y
    
    Enter a number in the range of 1-100 10
    
    10 is less than the secret number
    
    Enter a number in the range of 1-100 20
    
    20 is less than the secret number
    
    Enter a number in the range of 1-100 30
    
    30 is less than the secret number
    
    Enter a number in the range of 1-100 40
    
    40 is less than the secret number
    
    Enter a number in the range of 1-100 50
    
    50 is less than the secret number
    
    Enter a number in the range of 1-100 60
    
    60 is less than the secret number
    
    Enter a number in the range of 1-100 70
    
    70 is less than the secret number
    
    Enter a number in the range of 1-100 80
    
    80 is less than the secret number
    
    Enter a number in the range of 1-100 90
    
    90 is bigger than the secret number
    
    Enter a number in the range of 1-100 85
    
    85 is bigger than the secret number
    
    Enter a number in the range of 1-100 84
    
    84 is bigger than the secret number
    
    Enter a number in the range of 1-100 83
    
    83 is bigger than the secret number
    
    Enter a number in the range of 1-100 82
    
    82 is bigger than the secret number
    
    Enter a number in the range of 1-100 81
    
    81 is the correct answer
    
    Number of tries = 14
    
    Max number you guessed = 90
    
    Min number you guessed = 10
    
    Summation of numbers = 865
    
    The average of numbers = 61.79

  

### Sample Input/Output #2:
    

  

    Do you want unlimited tries? Enter 'y' or 'n' n
    
    You have 9 tries
    
    Enter a number in the range of 1-100 50
    
    8 tries left!
    
    50 is less than the secret number
    
    Enter a number in the range of 1-100 70
    
    7 tries left!
    
    70 is bigger than the secret number
    
    Enter a number in the range of 1-100 60
    
    6 tries left!
    
    60 is bigger than the secret number
    
    Enter a number in the range of 1-100 55
    
    5 tries left!
    
    55 is bigger than the secret number
    
    Enter a number in the range of 1-100 54
    
    4 tries left!
    
    54 is bigger than the secret number
    
    Enter a number in the range of 1-100 53
    
    3 tries left!
    
    53 is bigger than the secret number
    
    Enter a number in the range of 1-100 52
    
    2 tries left!
    
    52 is bigger than the secret number
    
    Enter a number in the range of 1-100 51
    
    1 tries left!
    
    51 is the correct answer
    
    Number of tries = 8
    
    Max number you guessed = 70
    
    Min number you guessed = 50
    
    Summation of numbers = 445
    
    The average of numbers = 55.62

 

### Edge Case # 1:
    
  

    Do you want unlimited tries? Enter 'y' or 'n' y
    
    Enter a number in the range of 1-100 101
    
    Invalid input: Must enter within the range of 1-100


 ### Edge Case #2:
    

     Do you want unlimited tries? Enter 'y' or 'n' n
    
    You have 10 tries
    
    Enter a number in the range of 1-100 -1
    
    Invalid input: Must enter within the range of 1-100

  

### Normalizing Textual Input
    

 One way you can read in user input and normalize the text is by using the lower() method in the string class which will make the text lowercase. For example,

    option = input("Do you want unlimited tries? Enter 'y' or 'n' ")
    option = option.lower()

  
This way it doesn’t matter if the user enters uppercase or lowercase letters.

  ## Project #4: Viva Las Vegas: Sports Betting Calculator
    
Las Vegas, aka Sin City is a city that’ quite unlike any other. A now desert oasis that was once a front to a shady underworld. Not only can you get married at a wedding chapel, feast on cuisines by world class chefs, and party at one of the pricey and crowded super clubs, you can also lose all of your money as well. We’re going to explore one of the features in Vegas that attracts visitors worldwide which is the gaming, and more explicitly, sports betting.
    

Write a python script that prompts the user to enter the American odds for a sporting event, and then the script computes the respective fractional/decimal odds and implied probability. To make it easier to compute the fraction odds consider using the fractions module in python: [https://docs.python.org/3/library/fractions.html](https://docs.python.org/3/library/fractions.html)

  
  

**American:** Also known as money line odds or US odds. The odds are preceded by either a plus or minus symbol. If the odds includes a minus, then that indicates the favorite and represents the amount you need to win $100. If it includes a + then that indicates the underdog and the amount won for ever $100 staked. A bet or wager is the amount of money you wish to risk.

**Fractional**: Also known as UK odds are typically used in the UK and Ireland. The numerator represents the amount your wager will yield and the denominator represents the amount that’s bet. For example, 20/15 means you bet $150 to win $200.

**Decimal**:Also known as European or continental odds, is a form of sports betting that’s popular in Continental Europe, Australia, New Zealand, and Canada. The decimal odds represent the amount that a better wins for every $1 wagered. What makes decimal odds different from American and Fractional odds is that your stake is already included in the decimal number, therefore no need to add back your stake. Therefore, the formula for computing decimal odds is:

_Total Return = Stake x Decimal Odds Number_

If you have calculated the fractional odds, then you can translate the fractional odds to decimal odds simply by adding a 1 to it.

**Implied Portability**: This is the conversion of betting odds into a percentage and that’s important to know if you want to become a professional sports better because it helps you access the potential value on a particular market. You can calculate the implied probability for American, fractional, and decimal odds by using the following formulas:

### American:
    
The equation to convert negative American odds:

Negative American odds / (Negative American odds + 100) * 100
    
The equation to convert positive American odds:
    
100 / (positive American odds + 100) * 100 
    
### Fractional odds:
    
The formula to calculate implied probability from fractional odds:
    
denominator / (denominator + numerator) * 100 
    
### Decimal odds:
    
The formula for calculating implied probability from decimal odds is:
    
    (1/ decimal odds) * 100 = implied probability
    
### Sample Input/Output #1:
    
    Welcome to the odds calculator:
        
    Enter the odds 200
    
    Enter wager (bet amount)500
    
    Bet 500
    
    -----------------------
    
    To win: 1000.0
    
    Payout: 1500.0
    
    American odds: 200
    
    Fractional odds: 2
    
    Decimal odds: 3.0
    
    Implied probability: 33.300000000000004
    
      

  

### Sample Input/Output #2:
    

    Welcome to the odds calculator:
    
    Enter the odds -100
    
    Enter wager (bet amount)200
    
    Bet 200
    
    To win: 200
    
    Payout: 400
    
    American odds: -100
    
    Fractional odds: 1
    
    Decimal odds: 2
    
    Implied probability: 50.0


