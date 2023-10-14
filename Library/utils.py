import random
from .handlers import messageHandlers

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
    
def chance(percent=100): 
    num = random.randint(0, 100)
    if num <= percent:
        return True
    return False
    
def failHandler(fails, failChance, failMessage, player):
    failInt = random.randint(0,failChance)
    if failInt == failChance:
        fail = selectRandom(fails)
        if fail["damage"] > 0:
            print(fail["info"] + " (" + format(fail["damage"]) +" damage)")
            print(failMessage%(fail["info"], fail["damage"]))
            player.hp -= fail["damage"]
            if player.hp <= 0:
                messageHandlers.gameOver(player,fail["deathMessage"]) # TODO maybe move the gameOver inside the player class ? how would it work tho? something like checkPlayerDead ?
        else:
            print(fail["info"])
        
        return True
    else:
        return False