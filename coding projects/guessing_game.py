##############################################
# The Secret Number Guessing Game
# -------------------------------
# User must guess a number within the range of 1-100.
# Once a correct guess is recorded the program prints
# game stats which includes number of tries, max and min guess,
# summation of scores, mean, and the secret number.
# If user fails to guess the correct number within the time
# frame then the program prints the correct number and stats.
#
# Game has two modes:
# -------------------
# Mode 1: User can guess an unlimited number of times.
# Mode 2: User is given a random number of tries in the range
# of 1-10.
#
# To run the program download it to your Desktop and within the
# terminal type: python guessing_game.py
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###############################################

from random import randint

option = input("Do you want unlimited tries? Enter 'y' or 'n' ")
option = option.lower()

"""
Variable Declarations:
---------------------
Defining the variables that don't 
need to be reset outside of the
while loops. 
"""
the_secret_number = randint(1, 100)
number_of_tries, summation, count = 0, 0, 0
max_number, min_number = the_secret_number, the_secret_number

if option == 'y':
    while True:
        your_guess = int(input('Enter a number in the range of 1-100 '))
        if your_guess < 0 or your_guess > 100:
            print('Invalid input: Must enter within the range of 1-100')
            break
        elif your_guess > the_secret_number:
            print(your_guess, 'is bigger than the secret number ')
        elif your_guess < the_secret_number:
            print(your_guess, 'is less than the secret number ')
        number_of_tries += 1
        summation += your_guess
        if your_guess > max_number:
            max_number = your_guess
        elif your_guess < min_number:
            min_number = your_guess
        elif your_guess == the_secret_number and number_of_tries == 1:
            max_number = your_guess
            min_number = your_guess
        if your_guess == the_secret_number:
            print(your_guess, 'is the correct answer')
            print('Number of tries =', number_of_tries)
            print('Max number you guessed =', max_number)
            print('Min number you guessed =', min_number)
            print('Summation of numbers =', summation)
            print('The average of numbers =', round(summation / number_of_tries, 2))
            break

elif option == 'n':
    number_of_tries = randint(1, 10)
    print('You have', number_of_tries, 'number of tries.')
    while number_of_tries > 0:
        your_guess = int(input('Enter a number in the range of 1-100 '))
        if your_guess < 0 or your_guess > 100:
            print('Invalid number: Must be in range of 1-100')
            break
        print(number_of_tries - 1, 'tries left!')
        if your_guess > the_secret_number:
            print(your_guess, 'is bigger than the secret number ')
        elif your_guess < the_secret_number:
            print(your_guess, 'is less than the secret number ')
        count += 1
        summation += your_guess
        number_of_tries -= 1

        """
        Takes care of the special case in which
        the user only gets one chance to
        guess the number.
        """
        if number_of_tries == 0 and count == 1:
            max_number = your_guess
            min_number = your_guess
        if your_guess > max_number:
            max_number = your_guess
        elif your_guess < min_number:
            min_number = your_guess

        """
        Prints the user stats. 
        ----------------------
        The first branch computes the stats if the user 
        guesses the correct number before number_of_tries 
        is equal to 0. The elif branch computes the stats if 
        the user doesn't guess the correct number within
        the allocated number of tries.
        """
        if your_guess == the_secret_number:
            print(your_guess, 'is the correct answer')
            print('You win!')
            print('Number of tries =', count)
            print('Max number you guessed =', max_number)
            print('Min number you guessed =', min_number)
            print('Summation of numbers =', summation)
            print('The average of numbers =', round(summation / count, 2))
            break
        elif your_guess is not the_secret_number and number_of_tries == 0:
            print('Good try :-)!')
            print('Secret number is ', the_secret_number)
            print('Number of tries =', count)
            print('Max number you guessed =', max_number)
            print('Min number you guessed =', min_number)
            print('Summation of numbers =', summation)
            print('The average of numbers =', round(summation / count, 2))

else:
    print('Invalid option! Program terminates...')
