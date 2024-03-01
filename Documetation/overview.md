# Documentation (rename this header to project name later)
 - The following table displays the version, description and date of the update
 - The version format is currently {major}.{minor}.{patch}-{prerelease}-{prerelease version}

### Changes

   Version    |      Description                                  |     Date    |                   Patch notes                   |
--------------|---------------------------------------------------|-------------|-------------------------------------------------|
 1.0.0-Alfa-1 | Project Alfa Release                              | 24. 9. 2023 | [1.0.0-Alfa-1.md](./patchNotes/1.0.0-Alfa-1.md) |
 1.0.0-Alfa-2 | Bugfixes, added Magic                             | 25. 9. 2023 | [1.0.0-Alfa-2.md](./patchNotes/1.0.0-Alfa-2.md) |
 1.0.0-Alfa-3 | Magic fix, Items, Backpack & project structure    |  1. 3. 2024 | [1.0.0-Alfa-3.md](./patchNotes/1.0.0-Alfa-3.md) |

## Playing

The game is a turn based text RPG where the player and enemy take turns to attack each other until one of them wins.

Upon launch there is a short introduction, then the player is prompted to enter a name. After doing this, the player is welcomed to the game and the first enemy is spawned.

When the enemy is spawned, the player is prompted for an action. As of version *1.0.0-Alfa-3* the player can use the following actions:

1. Attack - attack the enemy
1. Item - use one item the player chooses from his backpack and what to do with it
   - Eat - The player may eat an item. If it has some healvalue, it is displayed to the player and the player is healed by that much.
   - Potion - not implemented yet
   - Artifact - not implemented yet
1. Magic - use spells (*heal*)
1. Random - not implemented yet
1. Show Bag - show player inventory
1. Flee - quit current game

## Documentation for developers

This section contains detailed explanation of all packages, modules, functions, proceses and modability of the game.

### Data management

This game manages data in two ways:
 - The data it uses are stored in JSON files, accesed by the handy [jsonHelper](./Modules/jsonHelper.md) module.
 - All data the game *generates* (ie. player hp or name, enemy hp, states, etc.) are stored mostly in the classes the data belongs to. Future data storage management options are not planned yet, but I might use the JSONs as well.

### Mods

The game is being programmed in a way that allows for external modifications. Right now the customizable functionality includes *Enemy Colors, Enemy Sizes, Enemy Types, Spells, Items*. All of the mentioned is being stored via the JSON file format, so anyone willing to do so is able to extend these files.

It is not recommended to completely delete anything from the base game as it might break the game entirely:
 - ie. deleting all of the colors from the *default.json* is game breaking but if you delete all but the one color then nothing should happen
 - absolutely do **NOT** delete anything that has a parent in the JSONs except for array values. IF for example the *magic.json* file has incorrect format then the game will bug out when the player tries to use it. More on magic in the next section.

#### default.json

This file contains basic resources for the game processes.\
As of version *1.0.0-Alfa-2* it contains:
 - *entityTypes* - Used to diferentiate between player and enemies. This functionality is not being used in the current version and might be removed in the next one. Modifying it does plain noting but deletion will result in some bugs or crashes.
 - *sizes* - Contains sizes used to create enemies. Size of the enemy is chosen randomly upon the enemy creation. However this array is very important to following processes:
    - calculation of the enemy hp using the following formula : *entity.hp = len(sizes) - sizes.index(entity.size)*
    - calculation of the enemy dmg using the following formula : *enemyDmg = 6 - sizes.index(self.size)*, there is then a chance for the hp to be doubled **or** 0, in which case the enemy instantly dies, which is then followed by some humorous narrative.
    - looking at the mentioned formulas, you have for sure undrestood the importance of the sizes array. In case you didn't, let me explain: the more sizes there are the bigger damage and hp the enemies can possibly have.
 - *colors* - Contains colors used to create enemies. The color of the enemy is chosen randomly upon the enemy creation and does not affect the enemy stats. Yet.

#### enemies.json

This file contains arrays of enemy types.\
As of the current version which is *1.0.0-Alfa-2*, there's only the *creatures* array, meaning only enemies with the entityType *creature* appear in the game.\
This array will be probably splitted into different arrays in the future. Planned enemy types include (but are not limited to) *inteligent races, animals, fantasy creatures, demons, ghosts, spirits, undead creatures, creatures with magic properties, bosses, npcs*.

Each enemy has a bagsize and rarity. Bagsize specifies how many slots the enemy has in its inventory. Rarity specifies how rare the enemy is, meaning how rare it is for the enemy to spawn and what quality is the enemy loot.

As of version *1.0.0-Alfa-3* the file contains:
   - *creatures*:
      - goblin
      - vampire
      - centaur
      - ogre
      - skřítek Filípek - requested by my girlfriend, please don't ask what this is
      - dragon

#### magic.json

This file stores the spells used by the player along with the spell effects and a chance to fail. If the spell fails, the file stores fails for each individual spells. The effects are resolved immediately, a short message prints out, fail  damage is deducted from player hp, and some fails can eventualy lead to the player dying. For this case, there are death messages that get executed if the player gets killed by the spell failure.

Spells also have a type. Currently implemented spell types:
1. *heal*. Spells of type heal can heal (how unexpected) the player. The outcome is chosen randomly and the heal value is used to specify the amount of hp that is added to the player hp upon succesful casting.

## Library package

This section is dedicated to the different modules of the Library package used in this project. These modules are vital and the project cannot function without them, because they contain all of the code.

Each file contains detailed documentation of all the functions and processes.

1. [game.py](./Modules/game.md) - launching the game and the game loop
1. [entities.py](./Modules/entities.md) - classes and functions required for creation and management of objects
1. [utils.py](./Modules/utils.md) - various utilities
1. [jsonHelper.py](./Modules/jsonHelper.md) - vital module for JSON file management (mostly data parsing but there are some useful functions for JSON data management)

## Handlers package

This section covers the different modules of the handlers package. These modules are used for different game mechanics.

Each file contains detailed documentation of all the functions and processes.

1. [playerInput.py](./Modules/handlers/playerInput.md) - handles the player input and points the game towards the correct action handlers like attack for example. Also handles the Flee action (if the player decides to abandon the current game).
1. [playerAttack.py](./Modules/handlers/playerAttack.md) - handles the player attack action
1. [magicHandler.py](./Modules/handlers/magicHandler.md) - handles the player magic action
1. [itemHandler.py](./Modules/handlers/itemHandler.md) - handles the player item action
1. [messageHandler.py](./Modules/handlers/messageHandler.md) - handles all kinds of messages displayed to the player
1. [enemyAI.py](./Modules/handlers/enemyAI.md) - handles the enemy behaviour after player input ends