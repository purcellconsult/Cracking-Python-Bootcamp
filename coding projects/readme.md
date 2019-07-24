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


## Project # 5: A Game of conditions: Text Based Fantasy Game in Python.

This project requires the programmer to tap into their creative side. Who doesn’t like a good fantasy like _Game of Thrones_? Well, while few programmers posses the creative and literary prose of George R. R. Martin we can still create an interactive and fun text based game using python. This program allows the user to create their own fantasy kingdom filled with allies such as wizards and paladins and littered with obstacles such as your nemesis and rogues.

## Skills required to complete this project:

This project will test your knowledge of control flow and string manipulation and formatting in python. An auxiliary skill that you’ll harness is creativity.

**Rule #1**: When the program runs it prompts the user for their sex which is either _male_ or _female_.

**Rule #2**: The program will have two separate branches: one for the male story line, and another for the female version. The story line will be the same for each branch with the exception that the pronouns from each branch are gendered.

**Rule # 3**: Every story need characters and a plot, and this story will be nonetheless. Below are the characters that the story may include:

-   King
    
-   Queen
    
-   Paladin (a heroic knight)
    
-   Name of your kingdom
    
-   A wizard
    
-   A warrior
    

  
  Every story needs some bad guys. Here are a list of characters that the story may include:

-   Main nemesis
    
-   A thief
    
-   A sorcerer's name
    
-   A rogue
    

 Then, you need some tension to stir up the plot. Therefore the following elements may be implemented into the story:

-   The name of a war.
    
-   The duration for how long it lasted.
    
-   The outcome of the war and how all of the players played a role in it.  
      
    
**Rule # 4**: The program should ask the user in a _y_ or _n_ format if they have allies and if they have enemies. Their answer should play a role on the outcome of the game. If the user doesn’t have allies and they have enemies, how will that effect the outcome of the war? If the user have allies and no enemies then again, how will that effect the outcome of the war? Lastly, what if they had no enemies and no allies?

**Rule # 5**: The user input should be normalized so that when the user enters input such as a capital Y, it will be lower cased or capitalized for consistency. This is important so when you need to do conditional checks the case of the user input won’t matter against your check. Also, the names of the characters entered via the user input should be normalized as well. All the names should be capitalized including the name of the war as well for consistency.

**Rule #6**: Once you’re done writing this script, upload it to your GitHub and email a friend to play the game. Walk them through the steps of installing python on their platform, and then provide them instructions on how to run the script via the python interpreter.

### Sample Input/Output #1. The male story line.

    Enter your gender: "m" for male, "f" for female. m
    
    Enter your name: Voltron
    
    What's the name of your queen? Jacqueline
    
    What's the name of your kingdom? Aephegia
    
    Do you have allies? Enter "y" for yes or "n" for no. y
    
    Do you have enemies? Enter "y" for yes or "n" for no. y
    
    Enter your paladin's name Vasite
    
    Enter your wizard's name costa
    
    Enter your warrior's name Tepasta
    
    Voltron got enemies, got a lot of enemies
    
    Enter your villian's name Chaewudor
    
    What's the name of your war? bizarre
    
    How many years did the war last? 20
    
    Enter your thief's name Aidinethen
    
    Enter evil sorcerer's name Ewupeocan
    
    Enter rogue's name Ysalt

  Output:

    The great Voltron and his queen Jacqueline peacefully ruled the
    kingdom of Aephegia. However, a great war called Bizarre erupted.
    Voltron's nemesis Chaewudor invaded his kingdom. With the help of
    Aidinethen, Ewupeocan, and Ysalt, Chaewudor pillaged their land, stole
    precious resources, and brutally attacked their villagers.
           
    King Voltron and Queen Jacqueline with the help of Vasite, Costa, and Tepasta valiantly fought back and defeated Chaewudor after 20 years of fierce fighting. Order was finally restored and everyone in their kingdom
    lived happily ever after :-).

  

## Sample Input/Output #2: The female story line.

  

    Enter your gender: "m" for male, "f" for female.f
    
    Enter your name: Jacqueline
    
    What's the name of your king? Voltron
    
    What's the name of your kingdom? Aephegia
    
    Do you have allies? Enter "y" for yes or "n" for no. y
    
    Do you have enemies? Enter "y" for yes or "n" for no. y
    
    Enter your paladin's name Vasite
    
    Enter your wizard's name costa
    
    Enter your warrior's name tepasta
    
    Jacqueline got enemies, got a lot of enemies
    
    Enter your villian's name Chaewudor
    
    What's the name of your war? bizzare
    
    How many years did the war last? 20
    
    Enter your thief's name aidinethen
    
    Enter evil sorcerer's name ewupeocan
    
    Enter rogue's name ysalt

  
Output:

    The great Jacqueline and her king Voltron peacefully ruled the kingdom of
    
    Aephegia. However, a great war called Bizzare erupted. Jacqueline's nemesis Chaewudor invaded her kingdom. With the help of Aidinethen, Ewupeocan, and Ysalt, Chaewudor pillaged their land,
    
    stole precious resources, and brutally attacked their villagers.
    
    Queen Jacqueline and King Voltron with the help of Vasite, Costa, and Tepasta valiantly fought back and defeated Chaewudor after 20 years of fierce fighting. Order was finally restored and everyone in their kingdom lived happily ever after :-).
    
    
    


## Project # 6: The California Lottery
    
All but six States in the US have state lotteries so it’s no secret that it’s big business. How big? According to the CNN article _Lotteries: America’s $70 Billion Shame_’ by Derek Thompson, Americans spent $70 billion on lotto games in 2014. What’s shocking is  that’s more than what Americans in all 50 states spent on sports tickets, books, video games, movie tickets, and recorded music sales combined.

That's a big deal, and this project is not to convince you to lobby against the lottery. Instead, it’s going to help you hone your python programming skills while also shedding light on the odds you have at winning the lottery… even the ones with a smaller prize. We’re going to model the Daily 3 and Daily 4 lotteries in a simple script.
    
To learn the rules of the various California lotteries view the website:[https://www.lotterypost.com/results/ca](https://www.lotterypost.com/results/ca)
    

## The rules of Daily 3 and 4:
    
The Daily 3 lotto allows the player to pick any three numbers within the range of 0-9. In order to win the player must pick the correct number and must also get the ordering right. Therefore, if the Daily three numbers are 5, 9, and 2 then the user must enter the following numbers in the following order:
    
      [5, 9, 2]
    
It’s really simple, and modeling the simulation of the three numbers in python is also simple. We can use the randint() function from random to do this. For example, if we want to pick a random number then we can do something like the following:

        
    >>> from random import randint
        
    >>> randint(0, 9)
        
    4
    
The Daily 4 rules are exactly the same except it has four numbers instead of three. Write a python script that models the Daily 3 and Daily 4 in the California Lottery. After the user enters in their guess, the program should display a message letting the user know if they won or not. The winning numbers should also be displayed which should be stored in a list.

After you get the program to work try playing it 10 times. What can you conclude about winning the lottery from your own script?



# Project # 7: _Stat-tastic!_

This  project helps you to practice creating functions by coding common statistic formulas in python. Here's the functions that you will code:

-   Total: Gets the total count of data in a set.
    
-   Summation: Sums all of the data in a set.
    
-   Sample mean: Computes the average.
    
-   Sample standard deviation: Computes the average of the squared differences from the mean.
    
-   Median: The middle value.
    
-   Min: The smallest number in the set.
    
-   Max: The largest number in the set.
    

## Need a Quick Overview of Statistics?

Read this article from [Statistics Solutions](https://www.statisticssolutions.com/common-statistical-formulas) .

## Dummy Data to work with

In order to test your functions you need a dummy data set to work with.[Use the dataset here](https://github.com/purcellconsult/Master-Python-3-Course-/blob/master/coding%20projects/sample_dataset).

Here’s the results you should expect from each function call:

-   total() → 1000
    
-   summation() → 51404
    
-   sample_mean() → 51.404
    
-   sample_variance() → 834.4034034034034
    
-   sample_standard_dev() → 28.886041670734386
    
-   median() → 53
    
-   min() → 1
    
-   max() → 100
    

## How to open files in Python

Use the [with statement in python](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement).

An example of how to use it is listed below: 

    DATA = 'sample_dataset'
    with open(DATA) as file:
    for line in file:
        pass
         
Note,  for this project don’t use the built in [statistics module](https://docs.python.org/3/library/statistics.html).

Using it won’t make the exercise interesting! Also, don’t use the builtin max, min, or sorted functions from the [python library](https://docs.python.org/3/library/functions.html).


## Project #8:  Unit Testing Lab

The goal of this project is simple, to get you comfortable with writing unit tests in python. There’s many different options for crafting tests in python such as unittest, pytest, pylint, nose, and doctest. However, in this project we’ll simply use the built in unittest module in python. Below are the details of the project. Write unit tests for the various builtin functions in python:

    • abs()
    • bin()
    • bool()
    • callable()
    • chr()
    • dict()
    • divmod()
    • enumerate()
    • float()
    • format()
    • hex()
    • int()
    • len()
    • list()
    • max()
    • min()
    • next()
    • oct()
    • sorted()
    • sum()

Make sure to use at least 10 of the assert methods from the unittest module:https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

## Project #9: The Python Virtual ATM Machine

Object oriented programming is another paradigm that’s allowed in the python programming language. Most people are familiar with ATMs which are those little machines that we can put our card into, type in a pin, and then do various functions such as _get money._

The focal point of object oriented programming is to model real world objects, so let’s utilize python to model a virtual ATM machine. Here are the functionalities that we’ll implement in a class called ATM:

**deposit()**: Adds money to an account. The maximum amount the customer can add is $1000 USD, and there should be a condition in place that checks for edge cases. For example, a ValueError() exception should be raised if a customer tries to deposit a negative amount. 
  
**withdrawal()**: Withdraws money from an account. The maximum amount that can be withdrew is $500, and like with the deposit method, edge cases should be checked. To generate timestamps for the deposit() and withdrawl() methods, use the builtin datetime class: https://docs.python.org/3/library/datetime.html

**check_balance()**: Returns the current balance in the account.

**get_transactions()**: Returns the recent transaction with the time stamp appended to it.

**get_withdrawals()**: Returns the recent withdrawal with the time stamp appended to it.

**get_name()**: Returns the name of the customer.

**pin()**: Returns the pin of the customer.

**__init__()**: The init method will only require that the customer enter in their pin number. The program needs to include code that validates that the pin is a correct one. Once entered, the program will ask the customer for their name and then prints the following message: **Welcome to Your Virtual ATM** **YOUR_NAME**

### Here's some sample input/output:
  

        jack = Atm('Jack', '3282')  
        jack.deposit(100)  
        print(jack.get_transactions())  
        jack.deposit(200)  
        print(jack.get_transactions())  
        jack.withdraw(10)  
        print(jack.get_withdrawals())  
        jack.deposit(100)  
        print(jack.get_transactions())  
        jack.withdraw(100)  
        print(jack.get_withdrawals())  
        print(jack.get_pin())  
        print(jack.get_name())
    
    What's your name? jack
    Welcome to Your Virtual ATM Jack 
    {'transaction': ['2019-07-09 23:15:14.905258', 100]}
    {'transaction': ['2019-07-09 23:15:14.905351', 200]}
    {'withdrawal': ['2019-07-09 23:15:14.905404', -10]}
    {'transaction': ['2019-07-09 23:15:14.905452', 100]}
    {'withdrawal': ['2019-07-09 23:15:14.905497', -100]}
    3282
    Jack
    
    
    jill = Atm('Jill', '29321')
    
    What's your name? jill
    Welcome to Your Virtual ATM Jill 
     Traceback (most recent call last):
       File "/home/doug/PycharmProjects/master_python_course/coding_projects/atm_amchine.py", line 118, in <module>
    jill = Atm('Jill', '29321')
     File "/home/doug/PycharmProjects/master_python_course/coding_projects/atm_amchine.py", line 40, in __init__
    raise ValueError('Invalid Pin Number')
     ValueError: Invalid Pin Number
     
     henry = Atm('henry', '3821')
     henry.deposit(1000)
     print(henry.get_transactions())
     henry.withdraw(2000)
     
     What's your name? henry
     Welcome to Your Virtual ATM Henry 
     {'transaction': ['2019-07-09 23:30:33.705834', 1000]}
     Insufficient funds in account
     
     
     
## Project 10: Regex Lab 

### Phone Number Validator

Create a function that includes a regular expression that validates if a number is accurate or not. The regex should check for a number in the following format:

> ###-###-####

Sample input and output is listed below: 

Input:

    general_number('263-328-8372') general_number('263-
    
    328-83722')
    general_number('2633288372') general_number('263-328-8372')

Output:

    Verified Number!
    Doesn't validate!
    Doesn't validate!
    Verified Number!

### Social Security Number Validator

In the United States a Social Security Number (SSN) is a 9 digit number that has become the de facto national identification number for taxation and other purposes. Write a function that includes a regex which verifies that the user input is a valid social security number. Below is sample input/output for the function: 

Input:

    ssn_checker('928-382')
    ssn_checker('728-23-9272')
    ssn_checker('728239272')
    ssn_checker('542-50-4814')
    ssn_checker('63236638232')

Output:

    928-382 is an invalid social security number
    728-23-9272 is a valid social security number
    728239272 is a valid social security number
    542-50-4814 is a valid social security number
    63236638232 is an invalid social security number

### Email Address Validator

Write a regex that would validate all email addresses from every type of website (.com, info, net) and also every top-level domain  (us, ca, in, de) in existence. Try and get your regex to pass as many of the test cases as possible on the [Microsoft Developer Blog](https://blogs.msdn.microsoft.com/testing123/2009/02/06/email-address-test-cases/).

### Parse Your Favorite Song Lyrics

Music makes the world goes around, and luckily we can access a bunch of lyrics from lyrics.com. In this exercise write a function that includes a regex to parse your favorite song for the number of vowels and constants. If you want a default song to parse then use Imagine by John Lennon. 

### Parse The Ferrari Wikipedia Page 

Using the requests and regex modules, access the [Ferrari Wikipedia page](https://en.wikipedia.org/wiki/Ferrari) and then return the total count of the term Ferrari. Assume that the matches are case insensitive. 



## Project 11: A Web Parser for Your State's Government's Website

Using requests and bs4 the web scraper should parse the website for the following details:

-   header data
    
    -   get ALL anchor text in the header
        
    -   get ALL urls in the header
        
-   footer data:
    
    -   get ALL anchor text in the footer
        
    -   get ALL urls in the footer
        
-   All headings h1-h6. If a heading doesn’t exist the message ‘heading doesn’t exist’ should be printed.
    
-   All paragraph text from the site.
    
-   ALL links to the images. I.e,  < img src="https://california.azureedge.net/cdt/CAgovPortal/images/Uploads/service-Find-State-Park.jpg" > is no bueno. Instead, the following is needed: https://california.azureedge.net/cdt/CAgovPortal/images/Uploads/service-Find-State-Park.jpg
    
-   ALL social media links. Yes, there may be overlap with the links that’s generated, but the goal is to also parse specifically for just social media links.
    
-   If the site has embedded social media such as embedded tweets, then scrape them as well.
    
You can format the output in simple print statement. For example, here’s some sample data written for the website: [https://www.ca.gov](https://www.ca.gov/)


    ----- header anchor text -----
    Getting Services
    Doing Business
    Working
    Learning
    Living
    Visiting
    Government
    
    ----- header links -----
    https://www.ca.gov/services/
    https://www.ca.gov/doingbusiness/
    https://www.ca.gov/working/
    https://www.ca.gov/learning/
    https://www.ca.gov/living/
    https://www.ca.gov/visiting/
    https://www.ca.gov/government/
    javascript:;

At the end of this project make a list of the top 3 things you’ve learned about website development from learning web parsing.
 
