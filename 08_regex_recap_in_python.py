####################################
# Regular expressions patterns
# ----------------------------
#
# Self documenting examples
# about regular expressions along
# with resources on how to use them
# for better coding.
#
# Python Docs: https://docs.python.org/3/library/re.html
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#####################################

import re

# Simple demo of regexes

print('Simple Demo of Regexes')
print('-----------------------')

phrase = 'Learn how regular expressions work in python.'
match = re.search('python', phrase)
if match:
    print('A match is found starting at {}'
          ' and ending at {}'.format(match.start(), match.end()))
else:
    print('No match found!')

start = match.start()   # finds where key starts at in string
end = match.end()       # finds where key ends in string
print(phrase[start:end])    # python
print()

# Regex functions
# ---------------
# search(pattern, string, flags=0) -> scans the ENTIRE string for a match
# match(pattern, string, flags=0)  -> returns a match if 0 or more characters at the BEGINNING of string matches the regex
# fullmatch(pattern, string, flags=0) -> returns a match if the whole string matches the regex
# split(pattern, string, maxsplit=0, flags=0) -> split string by the pattern
# findall(pattern, string, flags=) -> returns non overlapping matches of pattern in string

print('Regex functions')
print('---------------')
print()

the_eagle_poem = """
He clasps the crag with crooked hands;

Close to the sun in lonely lands,

Ring'd with the azure world, he stands.

 
The wrinkled sea beneath him crawls;

He watches from his mountain walls,

And like a thunderbolt he falls.
"""

find_word = re.search('azure', the_eagle_poem) # <_sre.SRE_Match object; span=(92, 97), match='azure'>
print(find_word)

print(re.match('walls', the_eagle_poem))    # None
print(re.match('', the_eagle_poem))         # <_sre.SRE_Match object; span=(0, 0), match=''>
print(re.fullmatch(the_eagle_poem, the_eagle_poem))  # <_sre.SRE_Match object; span=(0, 227) ...>
print(re.split(';', the_eagle_poem))                 # ['\nHe clasps the crag with crooked hands', "\n\nClose to the sun in lonely lands...]
print(re.findall('the', the_eagle_poem))

# Matching single characters
# --------------------------
print()
phrase = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHABCDEFGHABCDEFGH'
print('Matching Characters')
print('-------------------')
print(re.search('h', phrase))           # <_sre.SRE_Match object; span=(7, 8), match='h'>
print(re.search('b', capital_letters))  # None
print(re.search('b', capital_letters, re.IGNORECASE))   # <_sre.SRE_Match object; span=(1, 2), match='B'>
print(re.findall('C', capital_letters))     # ['C', 'C', 'C']

alpha_pattern = '0123456789abcdefgh'

print(re.search('5', alpha_pattern))    # <_sre.SRE_Match object; span=(5, 6), match='5'>
print(re.search('a', alpha_pattern))    # <_sre.SRE_Match object; span=(10, 11), match='a'>

alpha_pattern_1 = '[0-9][a-z]'      # any digit or lowercase letter
print(re.match(alpha_pattern_1, '9'))   # None

print(re.search('[a-z]', '9920202022j22929'))   # <_sre.SRE_Match object; span=(10, 11), match='j'>
print(re.search('[A-Z]', 'abcdefghijklmn83nOjsksZ'))    # <_sre.SRE_Match object; span=(17, 18), match='O'>
print(re.search('[!@#$%^&*()-+{}[]|\;"<>?', 'zvgsggs272292hkOwuyeg%ss'))   # <_sre.SRE_Match object; span=(21, 22), match='%'>
print(re.search('[a-zA-Z]', '22838828289020932;/asksk'))    # <_sre.SRE_Match object; span=(19, 20), match='a'>

# verifies a sequence of characters in a certain order

print(re.search('[a-z]{11}', '2517abcd17171179Abs20abracadabra2298'))  # <_sre.SRE_Match object; span=(21, 32), match='abracadabra'>
print(re.search('[a-z]{1,5}', '2517abcde17171179'))  # <_sre.SRE_Match object; span=(4, 9), match='abcde'>
print(re.search('[a-z]{1,5}[0-9]{3}', 'c999'))  # <_sre.SRE_Match object; span=(0, 4), match='c999'>
print(re.search('[a-z]{1,5}[0-9]{3}', 'd17'))  # None. Why?
print()

# Common Regex Character Classes
# ------------------------------
# \d -> any digit
# \D -> any non digit
# \w -> any word
# \W -> any non alphanumeric character

print('Common Regex Character Classes and Repetitions ')
print('----------------------------------------------')

print(re.search('\d', 'jsjjsk273829BHAja'))  # <_sre.SRE_Match object; span=(1, 2), match='2'>
print(re.search('\d\d', '2j8k2c8c34m3ma1'))  # <_sre.SRE_Match object; span=(8, 10), match='34'>
print(re.search('\d{3}-\d{3}-\d{4}', '230-392-9327'))   # <_sre.SRE_Match object; span=(0, 12), match='230-392-9327'>

# matches any alphanumeric character and the underscore
print(re.search('\w', ';\';,.,.,.283jsns9'))    # <_sre.SRE_Match object; span=(9, 10), match='2'>
print(re.search('\w\w\w', '9d1'))   # <_sre.SRE_Match object; span=(0, 3), match='9d1'>

# Combining the \d and \w character classes:
print(re.search('\w\d\w\d', '_0_0'))    # <_sre.SRE_Match object; span=(0, 4), match='_0_0'>
print()


# Common Regex Symbols
# ------------------------------
# * -> 0 or more repetitions
# + -> 1 or more repetitions
# ? -> 0 or 1 repetitions of the proceeding
# . -> matches any character except for a newline
# $ -> matches the end of the string, or just before the newline
# ^ -> matches the start of the string


print('Common Regex Symbols ')
print('----------------------')

# the * operator matches 0 or more repetitions
print(re.search('\d*', '28392202'))     # <_sre.SRE_Match object; span=(0, 8), match='28392202'>

# the + operator matches 1 or more repetitions
print(re.search('aba+', 'abaaaaaa'))    # <_sre.SRE_Match object; span=(0, 8), match='abaaaaaa'>

# the ? causes the regex to match 0 or 1 repetitions of the preceding
print(re.search('abc?', 'ab'))    # ab validates
print(re.search('abc?', 'abc'))   # abc validates. what about ac or bc?

# the . matches any character
print(re.search('.{3}', '/,@'))   # <_sre.SRE_Match object; span=(0, 3), match='/,@'>

# $ matches just before the end of newline
print(re.search('^\d\d\d$', '278'))     # <_sre.SRE_Match object; span=(0, 3), match='278'>


# $ Matches just before the end of the string.
# If the search key appears before the end of the string, then None returns.
# It makes way more sense with a little code.

print(re.search('zo', 'zoey'))      # <_sre.SRE_Match object; span=(0, 2), match='zo'>
print(re.search('zo$', 'zoey'))     # None
print(re.search('zo$', 'hey zo'))   # <_sre.SRE_Match object; span=(4, 6), match='zo'>
print(re.search('zo$', 'Hey zo! What\'s cracking?'))  # None
print()

# ^ matches the start of the string
print(re.search('^Hi', 'Hello, Hi'))    # None
print(re.search('^Hi', 'Hi Hello'))     # <_sre.SRE_Match object; span=(0, 2), match='Hi'>
print()

# GROUPING
# --------
# [] -> a set of characters
# |  -> matches A or B
# () -> matches the regex inside the parentheses


print('GROUPING')
print('--------')
print(re.search('[a-z][A-Z][0-9][\w]', 'aB6H'))     # <_sre.SRE_Match object; span=(0, 4), match='aB6H'>
print(re.search('[a-z]|[0-9]|[>]', 'HAKSKS6,./?'))  # <_sre.SRE_Match object; span=(6, 7), match='6'>
print(re.search('(aab)(bbc)', 'aabbbc'))            # None






