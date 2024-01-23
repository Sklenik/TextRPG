# Documentation (rename this header to project name later)
 - The following table displays the version, description and date of the update
 - The version format is currently {major}.{minor}.{patch}-{prerelease}-{prerelease version}
###

   Version    |      Description      |     Date    |                   Patch notes                   |
--------------|-----------------------|-------------|-------------------------------------------------|
 1.0.0-Alfa-1 | Project Alfa Release  | 24. 9. 2023 | [1.0.0-Alfa-1.md](./patchNotes/1.0.0-Alfa-1.md) |
 1.0.0-Alfa-2 | Bugfixes, added Magic | 25. 9. 2023 | [1.0.0-Alfa-2.md](./patchNotes/1.0.0-Alfa-2.md) |

## Game mechanics
Game consists of a narrative supported by player text input. Player selects actions from offered options via entering their names in the console. The game then reacts accordingly.


### Intro
Game begins with short intro, then the player is prompted to name his character and the game begins with some more intro text.

## Documentation for developers
This section contains detailed explanation of all packages, modules, functions, proceses and modability of the game.

### Data management
This game manages data in two ways:
 - The data it uses are stored in JSON files, accesed by the handy [jsonHelper](./Modules/jsonHelper.md) module.
 - All data the game *generates* (ie. player hp or name, enemy hp, states, etc.) are stored mostly in the classes the data belongs to. Future data storage management options are not planned yet, but I might use the JSONs as well if I decide to implement some kind of backpack functionality.

### Mods
The game is being programmed in a way that allows for external modifications. Right now the customizable functionality includes *Enemy Colors, Enemy Sizes, Enemy Types, Spells, Consumables*. All of the mentioned is being stored via the JSON file format, so anyone willing to do so is able to extend these files.

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

#### enemies.json
This file contains arrays of enemy types.\
As of the current version which is *1.0.0-Alfa-2*, there's only the *creatures* array, meaning only enemies with the entityType *creature* appear in the game.\
This array will be probably splitted into different arrays in the future. Planned enemy types include (but are not limited to) *inteligent races, animals, fantasy creatures, demons, ghosts, spirits, undead creatures, creatures with magic properties, bosses, npcs*.

As of version *1.0.0-Alfa-2* the file contains:
   - *creatures*:
      - goblin
      - vampire
      - skřítek Filípek - requested by my girlfriend, please don't ask what this is
      - centaur
#### magic.json
As of the versoin *1.0.0-Alfa-2* this is the most complicated of the JSON files.

This file stores the spells used by the player along with the spell effects and a chance to fail. If the spell fails, the file stores fails for each individual spells. The effects are resolved immediately, a short message prints out, fail  damage is deducted from player hp, and some fails can eventualy lead to the player dying. For this case, there are death messages that get executed if the player gets killed by the spell failure.

Spells also have a type. Currently there is only one spell type implemented - *heal*. Spells of type heal can heal (how unexpected) the player. The outcome is chosen randomly and the heal value is used to specify the amount of hp that is added to the player hp upon succesful casting.

## Library package
This section is dedicated to the different modules of the Library package used in this project. These modules are vital and the project cannot function without them, because they contain all of the code.

Here are links to all currently existing package and/or subpackage modules that are being used by the game. Each file contains detailed documentation of all the functions and processes.

1. [game.py](./Modules/game.md) - launching the game and the game loop
1. [entities.py](./Modules/entities.md) - classes and functions required for creation and management of player and enemy objects
1. [utils.py](./Modules/utils.md) - various useful functions, right now contains some vital code that will be moved to new yet to be created module *handlers.py*
1. [jsonHelper.py](./Modules/jsonHelper.md) - vital module for JSON file management (mostly data retrieval but there are some useful functions for JSON data management)
