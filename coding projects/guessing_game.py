##############################################
# Number guessing game in python
# -------------------------------
# Prompts user to opt for an unlimited number of tries
# or a random number of tries in the range of 1-10.
# User must guess a number within the range of 1-100.
# Once a correct guess is recorded the program prints
# game stats such as number of tries, max and min guess,
# summation of scores, mean, and also the secret number.
#
# To run the program download and in the terminal type:
# python guessing_game.py
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###############################################

from random import randint

option = input("Do you want unlimited tries? Enter 'y' or 'n' ")

the_secret_number = randint(1, 100)
option = option.lower()
number_of_tries = 0
max_number, min_number = the_secret_number, the_secret_number
summation = 0

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
    print('You have', number_of_tries, 'tries')
    start, count = number_of_tries, 0
    while start > 0:
        your_guess = int(input('Enter a number in the range of 1-100 '))
        if your_guess < 0 or your_guess > 100:
            print('Invalid input: Must enter within the range of 1-100')
            break
        print(start - 1, 'tries left!')
        if your_guess > the_secret_number:
            print(your_guess, 'is bigger than the secret number ')
        elif your_guess < the_secret_number:
            print(your_guess, 'is less than the secret number ')
        count += 1
        summation += your_guess
        start -= 1
        if your_guess == the_secret_number and number_of_tries == 1:
            max_number = your_guess
            min_number = your_guess
        if your_guess > max_number:
            max_number = your_guess
        elif your_guess < min_number:
            min_number = your_guess
        elif your_guess == the_secret_number and number_of_tries == 1:
            max_number = your_guess
            min_number = your_guess
        if your_guess == the_secret_number:
            print(your_guess, 'is the correct answer')
            print('Number of tries =', count)
            print('Max number you guessed =', max_number)
            print('Min number you guessed =', min_number)
            print('Summation of numbers =', summation)
            print('The average of numbers =', round(summation / count, 2))
            break
        elif your_guess is not the_secret_number and start == 0:
            print('Good try :-)!')
            print('Secret number is ', the_secret_number)
            print('Number of tries =', count)
            print('Max number you guessed =', max_number)
            print('Min number you guessed =', min_number)
            print('Summation of numbers =', summation)
            print('The average of numbers =', round(summation / count, 2))
else:
    print('Invalid option! Program terminates...')
