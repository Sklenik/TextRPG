from .. import jsonHelper, utils
from . import messageHandlers, playerInput

# labels
enemyRetaliateMessage = "The %s got hit but refuses to give up and retaliates!"
enemyAttackMessage = "The %s attacks!"
enemyInflictsDamageMessage = "The %s inflicts %d points of damage."

playerKilledMessage = "You were slain by %s"

enemyMissedMessage = "The %s missed"

enemyKilledMessage = "You have killed the %s !"

# functions
def handleEnemyAI(player, enemy):
    if not enemy.isDead:
        if enemy.hit:
            utils.enterContinue(enemyRetaliateMessage%enemy.type, True, True)
            enemy.hit = False
        else:
            utils.enterContinue(enemyAttackMessage%enemy.type, True, True)
            
        enemyDmg = enemy.calculateAttack()
        if enemyDmg > 0:
            utils.enterContinue(enemyInflictsDamageMessage%(enemy.type, enemyDmg), False, True)
            player.hp -= enemyDmg
            if player.hp <= 0:
                messageHandlers.gameOver(player,playerKilledMessage%(enemy))
            else:
                playerInput.handlePlayerInput(player, enemy)
        else:
            utils.enterContinue(enemyMissedMessage%enemy.type, False, True)
            playerInput.handlePlayerInput(player, enemy)
    else:
        sizes = jsonHelper.getSizes()
        player.score += 1 * 5 - sizes.index(enemy.size);
        player.enemiesSlain += 1
        utils.enterContinue(enemyKilledMessage%enemy, False, True)
        # this is where handleResult was in the early version. Now that it is
        # gone, the handleEnemyAI function ends, then the handlePlayerInput function
        # ends, and then the code continues in the game.py again