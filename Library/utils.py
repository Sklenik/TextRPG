import random

# labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vars to create translations ?
enterContinueMessage = "Press enter to continue..."

# functions
def selectRandom(group):
    position = random.randint(0,len(group)-1)
    return group[position]

def enterContinue(message, addspacebefore, addspaceafter):
    if addspacebefore:
        print()
    if message != '':
        print(message)
    inputText = input(enterContinueMessage)
    if addspaceafter:
        print()
    return inputText