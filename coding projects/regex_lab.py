###########################################
# Regular Expressions Lab
# -----------------------
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
############################################

import requests
import re


def general_number(string):
    """
    This regular expression validates
    a number within this format:
    ###-###-####
    """
    phone_regex = '^\d{3}-\d{3}-\d{4}$'
    scan = re.search(phone_regex, string)
    if scan:
        print('Verified Number!')
    else:
        print('Doesn\'t validate!')


def ssn_checker(ssn):
    """
    A regex that verifies that the string entered is
    a valid social security number. The ssn number could be
    in the following formats:
    XXX-XX-XXXX or ...
    XXXXXXXXX
    """
    ssn_validator = '^\d{3}-\d{2}-\d{4}$|^\d{9}$'
    check = re.search(ssn_validator, ssn)
    if check:
        print('{} is a valid social security number'.format(ssn))
    else:
        print('{} is an invalid social security number'.format(ssn))


def email_address_checker(email):
    """
    Verifies if the user entered a valid
    email address.
    """
    email_checker = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,64}$'
    check = re.search(email_checker, email)
    if check:
        print('{} is a valid email address.'.format(email))
    else:
        print('{} is not a valid email address.'.format(email))


def song_stats(file):
    """
    This function parses a junk
    text file for valid email
    addresses.
    """
    data = ''
    vowels = '[aeiouy]'
    constants = '[bcdfghijklmnpqrstvwxz]'
    with open('imagine') as text:
        for line in text:
            data += line
        vowel_count = re.findall(vowels, data)
        constant_count = re.findall(constants, data)
        print(data)
        print(len(data))
        print(len(vowel_count))
        print(len(constant_count))


site = requests.get('https://en.wikipedia.org/wiki/Ferrari')
html = site.text
regex = re.compile(r'Ferrari')

hit = re.findall(regex, html)

print(len(hit))


print('General Number Function Tests')
print('-----------------------------')
general_number('263-328-8372')
general_number('263-328-83722')
general_number('2633288372')
general_number('263-328-8372')
print()

print('Social Security Number Tester')
print('-----------------------------')
ssn_checker('928-382')
ssn_checker('728-23-9272')
ssn_checker('728239272')
ssn_checker('542-50-4814')
ssn_checker('63236638232')


print('Email Address Checker')
# used the following test cases:
# https://blogs.msdn.microsoft.com/testing123/2009/02/06/email-address-test-cases
print('---------------------')
print()
print('Valid Email Tests')
print()

email_address_checker('email@domain.com')
email_address_checker('firstname+lastname@domain.com')
email_address_checker('email@subdomain.domain.com')
email_address_checker('firstname+lastname@domain.com')
email_address_checker('email@123.123.123.123')
email_address_checker('email@[123.123.123.123]')
email_address_checker('"email"@domain.com')
email_address_checker('1234567890@domain.com')
email_address_checker('email@domain-one.com')
email_address_checker('_______@domain.com')
email_address_checker('email@domain.name')
email_address_checker('email@domain.co.jp')
email_address_checker('firstname-lastname@domain.com')

print()
print('Invalid Email Tests')
print()

email_address_checker('plainaddress')
email_address_checker('#@%^%#$@#$@#.com')
email_address_checker('@domain.com')
email_address_checker('Joe Smith <email@domain.com>')
email_address_checker('email.domain.com')
email_address_checker('email@domain@domain.com')
email_address_checker('.email@domain.com')
email_address_checker('email.@domain.com')
email_address_checker('email..email@domain.com')
email_address_checker('あいうえお@domain.com')
email_address_checker('email@domain.com (Joe Smith)')
email_address_checker('email@domain')
email_address_checker('email@-domain.com')
email_address_checker('email@domain.web')
email_address_checker('email@111.222.333.44444')
email_address_checker('email@domain..com')
