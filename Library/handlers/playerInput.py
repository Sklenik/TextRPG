from .. import utils
from . import playerAttack, enemyAI, messageHandlers

# Labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vrrs to create translations ?
handlePlayerInputMessage = 'What do you wish to do? (Attack, Item, Magic, Random, Flee): '
repeatPlayerInputMessage = "Say, what was it again?"

fleeQuestion = "Are you sure you want to flee? (y/n): "
fleeMessage = "%s has decided to quit adventuring for now."

# player actions
def handlePlayerInput(player, enemy):
    print(enemy.info())
    print(player)
    action = input(handlePlayerInputMessage)
    match action:
        case "Attack":
            playerAttack.handleAttack(player, enemy)
        case "Item":
            print("Feature not implemented yet.")
            handlePlayerInput(player, enemy)
        case "Magic":
            print("Feature not implemented yet.")
            handlePlayerInput(player, enemy)
        case "Random":
            print("Feature not implemented yet.")
            handlePlayerInput(player, enemy)
        case "Flee":
            handleFlee(player, enemy)
        # TODO add option pass ? So that with future over time effects like
        # poison or regeneration, the player can "skip turn"  or wait for
        # the enemy to die from effects instead of provoking it ?
        # TODO which leads to enemies being always hostile now, focus more on
        # the RPG aspect and enable finding and provoking enemies? stealth? KO ?
        # lot of work needs to be done it seems

    utils.enterContinue('', False, True)
    enemyAI.handleEnemyAI(player, enemy)

def handleItem(player, enemy): # TODO in version after handleMagic is finnisher
    # TODO make enemies drop collectable loot -> will there be an encumbrance or a backpack ? I dont know yet
    pass

def handleRandom(player, enemy): # TODO in version after handleItem is finnished and tested
    pass

def handleFlee(player, enemy): 
    print('')
    action = input(fleeQuestion)
    if action == "y":
        print('')
        print(fleeMessage%player.name)
        messageHandlers.scoreMessage(player)
    elif action == "n":
        handlePlayerInput(player, enemy)
    else:
        handleFlee(player, enemy)
