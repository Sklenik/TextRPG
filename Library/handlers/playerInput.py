from .. import utils
from . import messageHandlers, enemyAI, playerAttack, magicHandlers

# Labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vrrs to create translations ?
handlePlayerInputMessage = 'What do you wish to do? (Attack, Item, Magic, Random, Flee): '
AttackAction = "Attack"
ItemAction = "Item"
MagicAction = "Magic"
RandomAction = "Random"
FleeAction = "Flee"

class actions:
    act1 = AttackAction
    act2 = ItemAction
    act3 = MagicAction
    act4 = RandomAction
    act5 = FleeAction

fleeQuestion = "Are you sure you want to flee?"
fleeMessage = "%s has decided to quit adventuring for now."

# player actions
def handlePlayerInput(player, enemy):
    print(enemy.info())
    print(player)
    action = input(handlePlayerInputMessage)
    global AttackAction, ItemAction, MagicAction, RandomAction, FleeAction


    match action:
        case actions.act1: # Attack
            playerAttack.handleAttack(player, enemy)
        
        case actions.act2: # Item
            print("Feature not implemented yet.")
            handlePlayerInput(player, enemy)
        
        case actions.act3: # Magic
            magicHandlers.handleMagic(player, enemy)
        
        case actions.act4: # Random
            print("Feature not implemented yet.")
            handlePlayerInput(player, enemy)
        
        case actions.act5: # Flee
            handleFlee(player, enemy)

        case _:
            handlePlayerInput(player, enemy)
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
    # TODO item usage - potions, food, etc..
    pass

def handleRandom(player, enemy): # TODO in version after handleItem is finnished and tested
    pass

def handleFlee(player, enemy): 
    print('')
    action = utils.yesNoActionHandler(fleeQuestion)
    if action == 1:
        print('')
        print(fleeMessage%player.name)
        messageHandlers.scoreMessage(player)
    elif action == 2:
        handlePlayerInput(player, enemy)
    elif action == 0:
        handleFlee(player, enemy)
