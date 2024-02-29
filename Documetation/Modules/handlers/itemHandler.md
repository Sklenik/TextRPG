# itemHandler.py

## Functions

### handleItem

This function runs only if the player backpack is not empty. The *checkIsEmpty* function from the [backpack](../entities.md#backpack) is called, and if the backpack is empty, it handles the situation and the *handleItem* function is never run.

When the function is run, it prints out a quick input for the player to determine, what is the player about to do with an item he chooses after the action.

The input looks like this
```
>>> What do you wish to do? (Eat, Potion, Artifact, Cancel): 
```

After the player chooses an action, the function runs the relevant functon, or goes back to the player input.

### handleEatLoop

This function is run when the player decides to consume an item. It runs the *selectItem* function provided by the [backpack](../entities.md#backpack) class, that prompts the player to select an item from the backpack.

Item can be selected or the player can choose to return back to the player actions.

If an item is selected, the player is asked for confirmation that the item is to be consumed.  
If the item has some *healValue*, the player hp is incremented by that value. Otherwise, nothing happens.