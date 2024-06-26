from .. import utils, jsonHelper, entities
from . import messageHandler, enemyAI, playerInput

# Labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vrrs to create translations ?
handleItemMessage = 'What do you wish to do? (Eat, Potion, Artifact, Cancel): '

EatAction = "Eat"
PotionAction = "Potion"
ArtifactAction = "Artifact"
CancelAction = "Cancel"

class actions:
    act1 = EatAction
    act2 = PotionAction
    act3 = ArtifactAction
    act4 = CancelAction

selectEatMessage = "What do you wish to eat? : "
doYouWantToEatMessage = "Are you sure you want to eat the %s ?"
youAteMessage = "You ate the %s. (heal %d)"

# item action
def handleItem(player, enemy):
    action = input(handleItemMessage)

    match action:
        case actions.act1: # Eat
            handleEatLoop(player, enemy)

        case actions.act2: # Potion
            print("Feature not implemented yet.")
            handleItem(player, enemy)
        
        case actions.act3: # Artifact
            print("Feature not implemented yet.")
            handleItem(player, enemy)
        
        case actions.act4: # Cancel
            playerInput.handlePlayerInput(player, enemy)

        case _:
            handleItem(player, enemy)

def handleEatLoop(player, enemy, dialog=True, itemToEat=entities.nullItem()) -> int:
    if dialog:
        itemToEat = player.backpack.selectItem(selectEatMessage)
        if itemToEat.name == '':
            handleEatLoop(player, enemy, dialog, itemToEat)
            return 0

    action = utils.yesNoActionHandler(doYouWantToEatMessage%itemToEat.name)
    
    if action == 1:
        if itemToEat.healValue != 0:
            player.hp += itemToEat.healValue
        player.backpack.substractItem(itemToEat)
        print(youAteMessage%(itemToEat.noQtyName(),itemToEat.healValue))

    elif action == 2:
        playerInput.handlePlayerInput(player, enemy)
    
    elif action == 0:
        handleEatLoop(player, enemy, dialog, itemToEat)
    
    return 1
