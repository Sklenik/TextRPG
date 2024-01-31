# game.py

## Functions

### play()

Creates player alongside some game intro and launches the game loop

### loop()

The game loop consists of the following simple schema:

 - enemy is created alongside a message displayed to the player
 - the player is prompted for actions (more about player actions in [playerInput.md](../Modules/handlers/playerInput.md))

How does the game loop work?

![Game Loop](/Data/Static/gameLoop.png)

After player chooses an actton, the enemy AI is handled, after which the *handleResult()* function is run. The function asks the player if he wishes to continue or end the game.

### handleResult()

Asks the player if he wishes to continue or end the game. If the player wants to continue, the game loop repeats.
