# utils.py

## Functions

### selectRandom

Selects random member of a list, array or such.

### selectRandomKeyAndValue

Selects random key and valyue from a provided dictionary. Returns list.

### enterContinue

This function is used a *LOT*. Used to print the *press enter to continue* message and handle the result. Can print space before or after the message. Can print the space in both places if needed.

### yesNoActionHandler

Handles (y/n) input and returns integers to indicate the result.

### chance

Nice little function that handles any events with percentual chance to occur. The chance is passed to the function as a parameter and the function returns the result (boolean).

### failHandler

Handles fails, currently only for the spell system but maybe I'll use it for other thins, so I decided to put in in there.

List of fails is passed as parameter. Currently follows the spell fail template and it will probably stay so.

FailMessage is passed as parameter and printed if the fail occurs.

Failchance is passed as parameter and used in the *chance* function to determine if the fail occurs. If it does, player hp is reduced by the fail damage (if there is any). If the player is killed by the fail, the deathMessage of the fail is displayed.

### getRarity

Returns random rarity. Currrently hardcoded, I should add the rarities to default.json in the future and rework it so it's nice and linear.
