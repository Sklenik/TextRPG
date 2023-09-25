from . import utils, entities
from .handlers import playerInput, messageHandlers

# Labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vrrs to create translations ?
playerNameMessage = "How do you wish to be called? : "
dangerousJourneyMessage = "A dangerous journey awaits!"

creatureSpawned = "A %s appeared!"
tooWeak = "The %s instantly died because it was too weak."

handleResultMessage = "Do you wish to continue on your journey? (y/n): "

# Main
def play():
    player = entities.player()
    player.hp = 10 # TODO difficulty options, affect damage as well, affect also the enemy, both hp and damage
    messageHandlers.intro()
    player.name = input(playerNameMessage)
    utils.enterContinue(dangerousJourneyMessage, False, True)
    loop(player)

def loop(player):    
    # TODO create diferent enemies, not just creatures ?
    # TODO maybe only the enemy class is needed ?
    creature = entities.createCreature()
    print(creatureSpawned%(creature))
    if creature.hp == 0:
        # TODO custom death messages, make this very rare to happen as well
        utils.enterContinue(tooWeak%creature, False, True)
        loop(player)
    else:
        playerInput.handlePlayerInput(player, creature)
    handleResult(player, creature)
    
def handleResult(player, creature):
    # TODO get rid of these prints, just add the \n to the start of the lines? or something like that?
    print('')
    # TODO (y/n) action handler function ?
    action = input(handleResultMessage)
    if action == "y":
        loop(player)
    elif action == "n":
        messageHandlers.handleVictory(player)
    else:
        handleResult(player, creature)