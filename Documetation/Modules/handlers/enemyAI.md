# enemyAI.py

## Function

### handleEnemyAI

This funciton is run after the *[playerInput](../handlers/playerInput.md)* function, i.e. after the player executes any action.

First, the function checks that the enemy was not killed by any previous attacks. If the enemy is dead, the score is calculated and added to the total player score, the total enemy slayed variable is incremented, and the function runs the *[handleEnemyDropSystem](#handleenemydropsystem)* funciton, to provide player with the enemy loot. Then the function ends and the game *[loop](../game.md#loop)* reaches it's end. The [handleResult](../game.md#handleresult) function is run to determine, if player wishes to carry on with the game, or quit.

Otherwise, the game checks if the enemy was hit previously. This affects the message that is displayed to the player before the enemy attacks.

Afterwards, the enemy attack damage is calculated, a message indicating the enemy is attacking is shown to the player, and if enemy doesn't miss, the atack damage is substracted from the player hp.

If player hp is lower than or equal to zero, the game ends with the [gameover](../handlers/messageHandler.md#gameover) function from the message handler.

If both player and the enemy survive, the *[playerInput](../handlers/playerInput.md)* is run and the player can choose an action again.

### handleEnemyDropSystem

This function prints out the enemy backpack, the player backpack, and prompts the player to either loot all items or leave them be.

If the player chooses to loot the enemey, the [lootEnemy](#lootenemy) function is run to transfer the enemy backpack contents to the player backpack and resolve any relevant problems.

### lootEnemy

Tries to transfer all items from the enemy backack to the player backpack. If the function reaches an item that cannot be added to the backpack anymore, the backpack functionality resolves this by asking the player if he wishes to replace some existing item or throw the current one away.