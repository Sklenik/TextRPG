from . import utils, entities
from .handlers import messageHandler, playerInput

# Labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vrrs to create translations ?
playerNameMessage = "How do you wish to be called? : "
dangerousJourneyMessage = "A dangerous journey awaits!"

creatureSpawned = "A %s appeared!"
tooWeak = "The %s instantly died because it was too weak."

handleResultMessage = "Do you wish to continue on your journey?"

# Main
def play():
    player = entities.player()
    player.hp = 10 # TODO difficulty options, affect damage as well, affect also the enemy, both hp and damage
    messageHandler.intro()
    player.name = input(playerNameMessage)
    utils.enterContinue(dangerousJourneyMessage)
    loop(player)

def loop(player):    
    creature = entities.createCreature()
    print()
    print(creatureSpawned%(creature))
    if creature.hp == 0:
        # TODO custom death messages, make this very rare to happen as well
        utils.enterContinue(tooWeak%creature)
        loop(player)
    else:
        playerInput.handlePlayerInput(player, creature)
    handleResult(player, creature)
    
def handleResult(player, creature):
    print()
    action = utils.yesNoActionHandler(handleResultMessage)
    if action == 1:
        loop(player)
    elif action == 2:
        messageHandler.handleVictory(player)
    elif action == 0:
        handleResult(player, creature)