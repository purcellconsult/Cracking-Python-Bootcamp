#####################################################
# A sports betting script written in python.
# What the script handles:
#
# American odds formula:
# Decimal odds formula:
# Percentage odds formula:
# Implied probability formula:
#   + 1P = 100 / (odd + 100)
#   - 1P = (-1 x odd) / ((-1 x odd) + 100)
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
#####################################################

from fractions import Fraction


def odds_calculator(american_odds, amount=100):
    """provides the amount to win and the payout."""

    if american_odds > 0:

        fractional_odds = Fraction(american_odds, 100)

        to_win = float(fractional_odds * amount)
        payout = float(to_win + amount)
        decimal_odds = 1 + fractional_odds
        decimal_odds = float(decimal_odds)
        implied_prob = round(100 / (american_odds + 100), 3)
        implied_prob *= 100
        print('-----------------------')
        print(
              f'To win: {to_win} \n'
              f'Payout: {payout} \n'
              f'American odds: {american_odds} \n'
              f'Fractional odds: {fractional_odds} \n'
              f'Decimal odds: {decimal_odds} \n'
              f'Implied probability: {implied_prob} '
              )
    else:
        american_odds = (american_odds)
        fractional_odds = abs(Fraction(100, american_odds))
        to_win = int(amount * fractional_odds)
        payout = int(to_win + amount)
        decimal_odds = 1 + fractional_odds
        implied_prob = (-1 * american_odds)
        implied_prob = round(implied_prob / ((-1 * american_odds) + 100),3)
        implied_prob *= 100
        print(
            f'To win: {to_win} \n'
            f'Payout: {payout} \n'
            f'American odds: {american_odds} \n'
            f'Fractional odds: {fractional_odds} \n'
            f'Decimal odds: {decimal_odds} \n'  
            f'Implied probability: {implied_prob} '
        )


if __name__ == '__main__':
    print('Welcome to the odds calculator: ')
    odds = int(input('Enter the odds '))
    wager = int(input('Enter wager (bet amount)'))
    print(f'Bet {wager}')
    odds_calculator(odds, wager)


