#####################################
# A simple dice rolling simulator.
# A simple program that models dice
# rolling in python.
# Program asks user to enter
#
#
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
######################################


from random import randint
from time import sleep

number_of_rolls = int(input('How many rounds you want to play? '
                            'Enter a number from 1-20: '))

if number_of_rolls < 0 or number_of_rolls > 20:
    print('Invalid input. Exiting program...')
    exit(0)

correct_guesses = 0
dice_numbers = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}

tries = 1
while tries < number_of_rolls + 1:

    print('round:', tries)
    your_guess = int(input('Roll the dice. Enter a number from 1-6... '))
    if your_guess < 0 or your_guess > 6:
        print('Invalid input. Must enter numbers within range of 1...6')
        print('Exiting...')
        break
    print('Dice rolling...')
    sleep(3)
    dice_result = randint(1, 6)
    if your_guess == dice_result:
        print('You win! The dice landed on', dice_result)
        correct_guesses += 1
    else:
        print('Better luck next time. Dice landed on', dice_result)
    tries += 1

    if dice_result == 1:
        dice_numbers[1] += 1
    elif dice_result == 2:
        dice_numbers[2] += 1
    elif dice_result == 3:
        dice_numbers[3] += 1
    elif dice_result == 4:
        dice_numbers[4] += 1
    elif dice_result == 5:
        dice_numbers[5] += 1
    elif dice_result == 6:
        dice_numbers[6] += 1

    if tries - 1 == number_of_rolls:
        print('Dice landed on 1:', dice_numbers[1], 'times')
        print('Dice landed on 2:', dice_numbers[2], 'times')
        print('Dice landed on 3:', dice_numbers[3], 'times')
        print('Dice landed on 4:', dice_numbers[4], 'times')
        print('Dice landed on 5:', dice_numbers[5], 'times')
        print('Dice landed on 6:', dice_numbers[6], 'times')
        print('Correct guesses: ', correct_guesses)
        print('Average of correct guesses', correct_guesses / number_of_rolls)
