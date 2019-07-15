###########################################
# ATM Machines
# ------------
# Models an ATM machine in python. Contains the
# following functions:
#
# deposit: adds money to an account.
# withdrawal: withdraws money from an account.
# check_balance: check the current account balance.
# get_transactions: shows the date and amount of recent transaction.
# get_withdrawals:
# pin: get your pin number.
# get_name: get the customer's name.
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#############################################

import datetime


class Atm:
    """
    Models an ATM machine in python using
    oop.
    """

    def __init__(self, name, pin):
        self.name = input("What's your name? ")
        self.name = self.name.capitalize()
        print('Welcome to Your Virtual ATM {} '.format(self.name))
        self.amount = 0
        self.transactions = dict()
        self.withdrawals = dict()
        self.pin = ''
        if pin.isdigit() and len(pin) == 4:
            self.pin = pin
        else:
            raise ValueError('Invalid Pin Number')
        self.customer_account = dict()
        self.customer_account.update(name=self.name)
        self.customer_account.update(pin=self.pin)

    def deposit(self, cash):
        """
        Deposits money into an account as long
        as the deposit is less than $1000 and greater
        than $0.
        """
        if cash > 0 < 1000:
            self.amount += cash
            date_stamp = str(datetime.datetime.now())
            self.transactions.update(transaction=[date_stamp, cash])
        else:
            print('Transaction Declined.')

    def withdraw(self, cash):
        """
        withdraw money from the atm machine.
        """
        if cash > 0 < 500:
            if cash > self.amount:
                print('Insufficient funds in account')
            elif cash < 1:
                print('Invalid amount. Enter at least $1')
            else:
                self.amount -= cash
                date_stamp = str(datetime.datetime.now())
                self.withdrawals.update(withdrawal=[date_stamp, -cash])

    def check_balance(self):
        """
        returns the current balance
        of the account.
        """
        return self.amount

    def get_transactions(self):
        """
        returns the account details.
        """
        return self.transactions

    def get_withdrawals(self):
        """
        returns the recent withdrawal.
        """
        return self.withdrawals

    def get_pin(self):
        """
        gets the pin
        """
        return self.pin

    def get_name(self):
        """
        returns the name of the customer.
        """
        return self.name


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

jill = Atm('Jill', '29321')

henry = Atm('henry', '3821')
henry.deposit(1000)
print(henry.get_transactions())
henry.withdraw(2000)