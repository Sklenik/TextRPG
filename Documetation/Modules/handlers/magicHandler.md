# magicHandler.py

## Funtions

### handleMagic

This function is run via the playerInput.py, when the player chooses the magic option.

Parses the [magic.json](/Data/JSON/magic.json) into a variable to be used later.

Runs the *[chooseSpell](#chooseSpell)** function to retrieve a spellname, by which it gets the spell data from the json.

Then the *[failHandler](../utils.md#failhandler)* is run to determine, if the spell fails or not. If it fails, it exits the handleMagic function and provides output for the player.

If the spell doesn't fail, the *[handleSpellEffects](#handlespelleffects)* function is run to determine, what does the spell do. Say the player casts a heal spell and it's succesfull -> the *[handleSpellEffects](#handlespelleffects)* funciton gets healvalue from the json and increments the player hp by that amount.

### chooseSpell

Parses spellnames into a list that's shown to the player and procesess the player input.

The list can look like this
```
>>> Choose a spell (Heal): 
```

Only literall spell names are accepted as input, the function repeats the input until it gets something it can process. That means until it gets something from the spelllist by the spell name the player provides. Then it returns the spellname.

### handleSpellEffects

Gets the spell from the provided spell list by the provided spellname. Then runs a check for the spell type which determines, what is the spell effect gonna be. After that the function runs relevant code for the spell effect and displays relevant message to the user, after which the entire spellHandlers exits and the enemyAI is run.