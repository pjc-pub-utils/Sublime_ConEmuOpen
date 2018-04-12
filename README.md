Launch ConEmu or CMDER with choice of shell from sublimetext3
=============================================================

This is my tweak of  of [tianjianchn Sublime_ConEmu](https://github.com/tianjianchn/Sublime_ConEmuOpen).

## TODO
- add config file for path to shells and launch commands


------
review also:
  [Kristinita fork](https://github.com/Kristinita/Sublime_ConEmuOpen)
  [d4n13lbc fork](https://github.com/d4n13lbc/Sublime_ConEmuOpen)
  [CesarDevsa fork](https://github.com/CesarDevesa/Sublime_ConEmuOpen)


-----------------
# original

Launch [ConEmu](https://github.com/Maximus5/ConEmu) from the current or project root folder
=================================
Only works for sublime text 3 on windows!

## Features
* Support project, folder, and even files-only instance!
* Support context menu on sidebar's folder or file 
* Reuse ConEmu window and try to open in a new tab
* Open ConEmu tab with a contextual title, like `st:<project name>` and `st:<project name>: <folder relative path to the project>`

## Installation
You should install the [ConEmu](https://github.com/Maximus5/ConEmu) first, and add `ConEmu.exe` to the `%PATH%` environment var.
Then use `Package Control` to install this package. 

## Usage
* Use `alt+c` to open current file's folder, `ctrl+alt+c` to open the project or top folder.
* Command palette commands: `ConEmu: Open current file folder` and `ConEmu: Open project or top folder`.

## License :

Licensed under MIT

Copyright (c) 2015 [kiliwalk](https://github.com/kiliwalk)
