from .. import jsonHelper, utils
from . import messageHandler, playerInput

# labels
enemyRetaliateMessage = "The %s got hit but refuses to give up and retaliates!"
enemyAttackMessage = "The %s attacks!"
enemyInflictsDamageMessage = "The %s inflicts %d points of damage."

playerKilledMessage = "You were slain by %s"

enemyMissedMessage = "The %s missed"

enemyKilledMessage = "You have killed the %s !"

enemyLootLabel = "Enemy loot"
playerBackpackLabel = "Your backpack"
enemyDroppedLootMessage = "The enemy had some items, do you want to loot them?"

# functions
def handleEnemyAI(player, enemy) -> int:
    if not enemy.isDead:
        if enemy.hit:
            utils.enterContinue(enemyRetaliateMessage%enemy.name)
            enemy.hit = False
        else:
            utils.enterContinue(enemyAttackMessage%enemy.name)
            
        enemyDmg = enemy.calculateAttack()
        if enemyDmg > 0:
            utils.enterContinue(enemyInflictsDamageMessage%(enemy.name, enemyDmg), False, False)
            player.hp -= enemyDmg
            if player.hp <= 0:
                messageHandler.gameOver(player,playerKilledMessage%(enemy))
            else:
                playerInput.handlePlayerInput(player, enemy)
                return 1
        else:
            utils.enterContinue(enemyMissedMessage%enemy.name, False, False)
            playerInput.handlePlayerInput(player, enemy)
            return 1
        return 1
    else:
        sizes = jsonHelper.getSizes()
        player.score += 1 * 5 - sizes.index(enemy.size);
        player.enemiesSlain += 1
        utils.enterContinue(enemyKilledMessage%enemy)
        handleEnemyDropSystem(player, enemy)
        return 0
        # this is where handleResult was in the early version. Now that it is
        # gone, the handleEnemyAI function ends, then the handlePlayerInput function
        # ends, and then the code continues in the game.py again

def handleEnemyDropSystem(player, enemy) -> int:
    if enemy.loot.IsEmpty():
        return 1
    
    print(enemyLootLabel)
    print(enemy.loot)
    print('\n' + playerBackpackLabel)
    print(player.backpack)
    action = utils.yesNoActionHandler(enemyDroppedLootMessage)
    
    if action == 1:
        lootEnemy(player, enemy)
        return 1

    elif action == 2:
        return 1

    elif action == 0:
        handleEnemyDropSystem(player, enemy)
        return 1
    
    return 0

def lootEnemy(player, enemy):
    for item in enemy.loot.items:
        if item.name != '':
            player.backpack.addItem(item)