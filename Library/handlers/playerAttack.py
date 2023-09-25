# Labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vrrs to create translations ?
playerAttackMessage = "You attacked for %d damage."
playerMissMessage = "You missed"

# Handlers

def handleAttack(player, enemy):
    print('')
    playerDmg = player.calculateAttack()
    if playerDmg > 0:
        enemy.hit = True
        print(playerAttackMessage%playerDmg)
        enemy.hp -= playerDmg
        if enemy.hp <= 0:
            enemy.isDead = True
    else:
        print(playerMissMessage)