import sys
import random

# TODO Clean up this mess, utils.py should not be so flooded

# Labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vrrs to create translations ?
introMessage = "Welcome brave adventurer!"  # TODO redo with pyfiglet ?
enterContinueMessage = "Press enter to continue..."

# Selection functions
def selectRandom(group):
    position = random.randint(0,len(group)-1)
    return group[position]

# Console Output
def intro():
    print(introMessage)

def enterContinue(message, addspacebefore, addspaceafter):
    if addspacebefore:
        print('\n')
    if message != '':
        print(message)
    if addspaceafter:
        print('\n')
    return input(enterContinueMessage)