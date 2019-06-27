##########################################
# Get practice for the California lottery!
# See list of California Lottery Results:
# https://www.lotteryusa.com/california
#
# This script models the following:
# Daily 3
# Daily 4
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
###########################################

from random import randint
from time import sleep

daily_3 = input("Would you like to play the Daily 3? Enter 'y' for yes or 'n' for no ")

# normalizes the text
daily_3 = daily_3.lower()

if daily_3 == 'y':
    lucky_num_1 = randint(0, 9)
    lucky_num_2 = randint(0, 9)
    lucky_num_3 = randint(0, 9)
    lucky_nums = [lucky_num_1, lucky_num_2, lucky_num_3]
    user_input_1 = int(input('Enter your lucky number #1 '))
    user_input_2 = int(input('Enter your lucky number #2 '))
    user_input_3 = int(input('Enter your lucky number #3 '))
    print('Lucky number number 1...')
    sleep(1)
    print(lucky_num_1)
    print('Lucky number number 2...')
    sleep(1)
    print(lucky_num_2)
    print('Lucky number number 3...')
    sleep(1)
    print(lucky_num_3)
    sleep(1)

    print('The Daily 3 Are:', lucky_nums)

    if user_input_1 == lucky_num_1 and user_input_2 == lucky_num_2 and user_input_3 == lucky_num_3:
        print('You won the daily 3!')
    else:
        print('You didn\'t win the lucky 3 :-(')
else:
    pass

daily_4 = input("Would you like to play the Daily 4? Enter 'y' for yes or 'n' for no ")

# normalizes the text
daily_4 = daily_4.lower()

if daily_4 == 'y':
    lucky_num_1 = randint(0, 9)
    lucky_num_2 = randint(0, 9)
    lucky_num_3 = randint(0, 9)
    lucky_num_4 = randint(0, 9)
    lucky_nums = [lucky_num_1, lucky_num_2, lucky_num_3, lucky_num_4]
    user_input_1 = int(input('Enter your lucky number #1 '))
    user_input_2 = int(input('Enter your lucky number #2 '))
    user_input_3 = int(input('Enter your lucky number #3 '))
    user_input_4 = int(input('Enter your lucky number #4 '))
    print('Lucky number number 1...')
    sleep(1)
    print(lucky_num_1)
    print('Lucky number number 2...')
    sleep(1)
    print(lucky_num_2)
    print('Lucky number number 3...')
    sleep(1)
    print(lucky_num_3)
    sleep(1)
    print('Lucky number number 4...')
    sleep(1)
    print(lucky_num_4)

    print('The Daily 4 Are:', lucky_nums)

    if user_input_1 == lucky_num_1 and user_input_2 == lucky_num_2:
        if user_input_3 == lucky_num_3 and user_input_4 == lucky_num_4:
            print('You won the daily 3!')
        else:
            print('Didn\'t win the lucky 4 :-(')
    else:
        print('Didn\'t win the lucky 4 :-(')

