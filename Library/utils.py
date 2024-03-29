import random
from .handlers import messageHandler

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

def selectRandomKeyAndValue(dict) -> list:
    dictList =  list(dict.items())
    keyAndValue = selectRandom(dictList)
    return keyAndValue

def enterContinue(message='', addspacebefore=False, addspaceafter=True):
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
    if chance(failChance):
        fail = selectRandom(fails)
        if fail["damage"] > 0:
            print(failMessage%(fail["info"], fail["damage"]))
            player.hp -= fail["damage"]
            if player.hp <= 0:
                messageHandler.gameOver(player,fail["deathMessage"]) # TODO maybe move the gameOver inside the player class ? how would it work tho? something like checkPlayerDead ?
        else:
            print(fail["info"])
        
        return True
    else:
        return False
    
def getRarity():
    if chance(5):
        return "legendary"
    if chance(10):
        return "epic"
    if chance(20):
        return "super rare"
    if chance(30):
        return "rare"
    if chance(40):
        return "uncommon"

    return "common"