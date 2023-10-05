import random

# labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vars to create translations ?
enterContinueMessage = "Press enter to continue..."
yesNoMessage = "%s (y/n): "
yesAction = "y"
noAction = "n"

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

def yesNoActionHandler(message):
    action = input(yesNoMessage%message)
    if action == yesAction:
        return 1
    elif action == noAction:
        return 2
    else:
        return 0