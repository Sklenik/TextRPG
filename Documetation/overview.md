# Documentation (rename this header to project name later)

 - The following table displays the version, description and date of the update
 - The version format is currently {major}.{minor}.{patch}-{prerelease}-{prerelease version}
###

   Version    |      Description     |    Date
--------------|----------------------|------------
 1.0.0-Alfa-1 | Project Alfa Release | 24. 9. 2023

## Game mechanics
### TBD
This section will contain the all the basic mechanics of the game required to launch, play and of course enjoy the software.

## Library package
This section is dedicated to the different modules of the Library package used in this project. These modules are vital and the project cannot function without them, because they contain all of the code.

1. [game.py](./Modules/game.md) - launching the game and the game loop
1. [entities.py](./Modules/entities.md) - classes and functions required for creation and management of player and enemy objects
1. [utils.py](./Modules/utils.md) - various useful functions, right now contains some vital code that will be moved to new yet to be created module *handlers.py*
1. [jsonHelper.py](./Modules/game.md) - vital module for JSON file management (mostly data retrieval but there are some useful functions for JSON data management)