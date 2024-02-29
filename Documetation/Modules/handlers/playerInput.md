# playerInput.py

## Functions

### handlePlayerInput

Handles what the player does when it's time for the player action. Runs handlers in places of relevant actions.

First, the function prints out he enemy and player HUD, then it prints out what actions can the player use.

Implemented actions:
 - attack - runs the [playerAttack.py](./Modules/handlers/playerAttack.md)
 - magic - runs the [magicHandler.py](./Modules/handlers/magicHandler.md)
 - item - runs the [itemHandler.py](./Modules/handlers/itemHandler.md)
 - random - not implemented yet
 - show bag - prints player [backpack](../entities.md#backpack) to show player inventory
 - flee - quits the game

If the input of the function is somethin else, the function is rerun and user gets the actions printed out again. After player chooses an action, the results are processed and then the [enemyAI.py](./Modules/handlers/enemyAI.md) module runs to process what enemy does.

This is how it looks when the actions are shown to the player
```
>>> What do you wish to do? (Attack, Item, Magic, Random, Show Bag, Flee): 
```

### handleFlee

Asks the player if he wishes to quit or not, quits the game if the user wishes so.