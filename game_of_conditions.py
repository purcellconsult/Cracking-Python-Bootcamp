###########################################################
# A Game of Conditions: Text Based Fantasy Game in Python
# --------------------------------------------------------
# This is the text based adventure game.
# It works by asking the gender of the user,
# asking them additional questions, and then modifying the
# storyline accordingly.
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###########################################################


def male_adventure():
    your_name = input('Enter your name: ')
    queen_name = input('What\'s the name of your queen? ')
    kingdom = input('What\'s the name of your kingdom? ')
    your_name, queen_name, kingdom = your_name.capitalize(), queen_name.capitalize(), kingdom.capitalize()
    have_allies = input('Do you have allies? Enter "y" for yes or "n" for no. ')
    have_enemies = input('Do you have enemies? Enter "y" for yes or "n" for no. ')
    have_allies, have_enemies = have_allies.lower(), have_enemies.lower()

    if have_allies == 'y':
        paladin = input('Enter your paladin\'s name ')
        wizard = input('Enter your wizard\'s name ')
        warrior = input('Enter your warrior\'s name ')
        paladin, wizard, warrior = paladin.capitalize(), wizard.capitalize(), \
                                   warrior.capitalize()
    elif have_allies == 'n':
        pass

    if have_enemies == 'y':
        print('{} got enemies, got a lot of enemies'.format(your_name))
        villian = input('Enter your villian\'s name ')
        war_name = input('What\'s the name of your war? ')
        years = int(input('How many years did the war last? '))
        thief = input('Enter your thief\'s name ')
        evil_sorcerer = input('Enter evil sorcerer\'s name ')
        rogue = input('Enter rogue\'s name ')
        thief, evil_sorcerer, rogue = thief.capitalize(), evil_sorcerer.capitalize(), rogue.capitalize()
    elif have_enemies == 'n':
        pass

    if have_allies == 'y' and have_enemies == 'y':
        message = """
            The great {0} and his queen {1} peacefully ruled the kingdom of
            {2}. However, a great war called {3} erupted. {0}'s nemesis {4} invaded
            his kingdom. With the help of {5}, {6}, and {7}, {4} pillaged their land,
            stole precious resources, and brutally attacked their villagers.
            King {0} and Queen {1} with the help of {8}, {9}, and {10} valiantly 
            fought back and defeated {4} after {11} years of fierce fighting. Order was finally
            restored and everyone in their kingdom lived happily ever after :-).""".format(your_name, queen_name,
                                                                                           kingdom, war_name, villian,
                                                                                           thief, evil_sorcerer, rogue,
                                                                                           paladin, wizard, warrior,
                                                                                           years)
        print(message)
    elif have_allies == 'y' and have_enemies == 'n':
        message = """
            The great {0} and his queen {1} peacefully ruled the kingdom of
            {2}. With the help of {3}, {4}, and {5}, {0} and {1} were able to keep their
            kingdom safe forever. The entire kingdom of {2} lived happily ever after :-).True Story.THE END.""".format(
            your_name, queen_name,
            kingdom, paladin, wizard, warrior, kingdom)
        print(message)
    elif have_allies == 'n' and have_enemies == 'y':
        message = """
                        The great {0} and his queen {1} peacefully ruled the kingdom of
                        {2} for many years. However, one evening their nemesis {3} with the help of
                        {4}, {5}, and {6} invaded their kingdom which lead to an infamous war in {2}
                        history called {8}. This war lasted {9} years. In the end {3} and his goons pillaged the land, destroyed the villagers,
                        and usurped {0} and {1}. THE END :-(""".format(your_name, queen_name, kingdom, villian, thief,
                                                                       evil_sorcerer, rogue, kingdom, war_name, years)
        print(message)
    elif have_enemies == 'n' and have_enemies == 'n':
        message = """
            The great {0} and his queen {1} lived in the kingdom of
                        {2} for many years alone. 
            """.format(your_name, queen_name, kingdom)
        print(message)
        pass


def female_adventure():
    """This the function for the female adventure."""
    your_name = input('Enter your name: ')
    king_name = input('What\'s the name of your king? ')
    kingdom = input('What\'s the name of your kingdom? ')
    have_allies = input('Do you have allies? Enter "y" for yes or "n" for no. ')
    have_enemies = input('Do you have enemies? Enter "y" for yes or "n" for no. ')

    if have_allies == 'y':
        paladin = input('Enter your paladin\'s name ')
        wizard = input('Enter your wizard\'s name ')
        warrior = input('Enter your warrior\'s name ')

    if have_allies == 'n':
        pass

    if have_enemies == 'y':
        print('{} got enemies, got a lot of enemies'.format(your_name))
        villian = input('Enter your villian\'s name ')
        war_name = input('What\'s the name of your war? ')
        years = int(input('How many years did the war last? '))
        thief = input('Enter your thief\'s name ')
        evil_sorcerer = input('Enter evil sorcerer\'s name ')
        rogue = input('Enter rogue\'s name ')
    if have_enemies == 'n':
        pass

    if have_allies == 'y' and have_enemies == 'y':
        message = """
            The great {0} and her king {1} peacefully ruled the kingdom of
            {2}. However, a great war called {3} erupted. {0}'s nemesis {4} invaded
            her kingdom. With the help of {5}, {6}, and {7}, {4} pillaged their land,
            stole precious resources, and brutally attacked their villagers.
            Queen {0} and King {1} with the help of {8}, {9}, and {10} valiantly 
            fought back and defeated {4} after {11} years of fierce fighting. Order was finally
            restored and everyone in their kingdom lived happily ever after :-).""".format(your_name.capitalize(),
                                                                                           king_name.capitalize(),
                                                                                           kingdom.capitalize(),
                                                                                           war_name.capitalize(),
                                                                                           villian.capitalize(),
                                                                                           thief.capitalize(),
                                                                                           evil_sorcerer.capitalize(),
                                                                                           rogue.capitalize(),
                                                                                           paladin.capitalize(),
                                                                                           wizard.capitalize(),
                                                                                           warrior.capitalize(), years)
        print(message)
    elif have_allies == 'y' and have_enemies == 'n':
        message = """
            The great {0} and her king {1} peacefully ruled the kingdom of
            {2}. With the help of {3}, {4}, and {5}, {0} and {1} were able to keep their
            kingdom safe forever. The entire kingdom of {2} lived happily ever after :-).True Story.THE END.""".format(
            your_name, king_name,
            kingdom, paladin, wizard, warrior, kingdom)
        print(message)
    elif have_allies == 'n' and have_enemies == 'y':
        message = """
                        The great {0} and her king {1} peacefully ruled the kingdom of
                        {2} for many years. However, one evening their nemesis {3} with the help of
                        {4}, {5}, and {6} invaded their kingdom which lead to an infamous war in {2}
                        history called {7}. This war lasted {8} years. In the end {3} and his goons pillaged the land, destroyed the villagers,
                        and usurped {0} and {1}. THE END :-(""".format(your_name, king_name, kingdom, villian,
                                                                       thief, evil_sorcerer, rogue, kingdom,
                                                                       war_name, years)
        print(message)
    elif have_enemies == 'n' and have_enemies == 'n':
        message = """
            The great {0} and her king {1} lived in the kingdom of
                        {2} for many years alone. 
            """.format(your_name, king_name, kingdom)
        print(message)
        pass


gender = input('Enter your gender: "m" for male, "f" for female.'
               )

# converts input to lower
gender = gender.lower()
if gender == 'f':
    female_adventure()
elif gender == 'm':
    male_adventure()
else:
    print('Enter correct option or you "can\'t" play!')



