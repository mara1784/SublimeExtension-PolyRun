# PolyRun

Running multiple scripts from a single opened Sublime Text editor is not enabled. This extension unlocks it.
PolyRun was made for Debian Linux. If you would like to use it with anything else, you should change the called terminal in the code.

## Features
- Opens a new external terminal window for script execution.
- Allows running multiple scripts at the same time without blocking Sublime Text.
- I pre-configured keyboard shortcut (`Ctrl+B`) for you in Default.sublime-keymap.example, if you want it, you must set up in Sublime Editor. [how to set up keybind](#Keybinds)

## Installation

### Via Package Control
1. Open Sublime Text.
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette.
3. Type `Package Control: Install Package` and press `Enter`.
4. Search for `PolyRun` and press `Enter`.

## Usage
- Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) press Enter and write into open field `Run python script in Terminal`
- If you've set up a shortcut, you can press `Ctrl+B` or your choise while editing a Python file to run it in a new terminal window.

## Keybinds
### Set up keybinds
- I recommend set up keybind.
- You can do it this way:
  1. Open Sublime Text
  2. Click on `Preferences` in top menu and there chose `Browse Packages...`
  3. Open the `User` folder
  4. In User folder insert the `Default.sublime-keymap.example` from this github site without `.example` ending.

### Customization
If you want, you can replace the default shortcut `["ctrl+b"]` by yourself in `Default.sublime-keymap.example`.
