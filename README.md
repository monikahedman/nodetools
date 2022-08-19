# Node Tool Scripts for Houdini
This is an ongoing group of tools used to format and manipulate nodes in the Network Editor to standardize and simplify formatting.

## Installation
Right click the Houdini shelf you would like the tool in and choose *New Tool*. Name the tool whatever you'd like under the *Options* tab. You can upload an image under *Icon* if you'd like. Paste the contents of the script in the *Script* tag. Make sure the Script Language is set to Python. If you would like, you can set a hotkey for the tool under the *Hotkeys* tab. Then, *Accept* the tool. You can always edit the tool later.

## Note
Because this project is ongoing, I will later be adding in functionality to make it easier for users who are less familiar with Python to use and customize these tools. If there is any functionality you'd like to see or any tools you're looking for, feel free to send me an email at monika@monikahedman.com.

## Tool List
### OUT Null Node Formatting
** Filename: out_format.py**
Prepends "OUT_" to the name of the node if that is not already included in the name. Changes the node to a "pointy" shape and makes it red. If a node already exists with that name, a counter is appended.
![alt text](https://github.com/monikahedman/nodetools/blob/main/images/out.jpg?raw=true)

### Controller Formatting
** Filename: ctrl_format.py**
Names the node CTRL and makes it a yellow circle. If a node already exists with that name, a counter is appended.
![alt text](https://github.com/monikahedman/nodetools/blob/main/images/ctrl.jpg?raw=true)
