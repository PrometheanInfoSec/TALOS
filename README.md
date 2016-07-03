# TALOS

### Overview
1. What's in a name
2. Basic usage
3. Resources

### What's in a name
Hello, it's nice to meet you.  I'm TALOS.  My name represents a number of things.  All of them however, tie back into my main mission.  I exist, to assist Computer Network Defenders.  
I was created to fill an obvious void in defensive methodologies.  It should be obvious to anyone.  You can never win a swordfight by attempting nothing more than parrying your adversary's attacks.  Eventually, you will mess up.  Eventually you will miss something.  And eventually, you will go down.
Active Defense offers the answer to this conundrum.  Though we may not be "hacking back."  There are plenty of things we can do to stop an attacker in his tracks, that go well above and beyond simple "hardening."  
The reason why I was created, was to provide a contral hub, through which Computer Network Defenders could operate.  Seamlessly, simply, and powerfully, to deploy Active Defense tools on their networks.
I was created to democratize Active Defense.  To give everyone a shot at protecting their turf.



### Basic Usage
TALOS can be launched by running the main console *talos.py*  It's really that simple.  Once you get into the console, you can type *help* to see a list of available commands.  My creator has attempted make me as smart as possible.  As such, I have built in shell features, such as command line history you can go through with your arrow keys.  I have smart autocomplete.  I come with aliased commands in case your human brain accidentally types in something synonymous to a command instead of the actual command.  
I function in a way very similar to many frameworks of the past.  Two frameworks which my creator had good knowledge of when he wrote me are as follows: The Metasploit Framework, and Recon-ng.
When first learning how to navigate your way through the console, don't be afraid to use the help command audaciously.  My creator has programmed the ability for the help command to bring up information about a number of things, such as specific commands, and modules.

#### The basic workflow
Here's how deploying a module usually works inside the TALOS console.
1. Load the module
2. Set the variables
3. Run the module 

###### Loading a module
To load a module, simply type `load <module_name>`
For example
```
load local/honeyports/basic
```
A number of aliases exist for this command.  These will also work.
```
module local/honeyports/basic
```
or
```
use local/honeyports/basic
```
You will know the module is loaded, when your prompt changes to read the name for the module.  
From `TALOS>>>` to this `local/honeyports/basic>>>`

###### Setting the variables
Setting the variables is also very simple.
To start with, you will want to list the available variables.
`list variables`

Each variable has four fields.  The name, the value, whether or not it is required, and a brief description.
If the description is too long, an error message will be displayed.  And you will have to run `more <variable_name>` to get the full printout.

To change a variable simply run `set <variable_name> <value>`
For example.
```
local/honeyports/basic>>> list variables
Variables
Name      Value             Required  Description
----------------------------------------------------------------------------
host                        no        Leave blank for 0.0.0.0 'all'
whitelist 127.0.0.1,8.8.8.8 no        hosts to whitelist (cannot be blocked)
port                        yes       port to listen on
----------------------------------------------------------------------------
local/honeyports/basic>>> set port 445
local/honeyports/basic>>> list variables
Variables
Name      Value             Required  Description
----------------------------------------------------------------------------
host                        no        Leave blank for 0.0.0.0 'all'
whitelist 127.0.0.1,8.8.8.8 no        hosts to whitelist (cannot be blocked)
port      445               yes       port to listen on
----------------------------------------------------------------------------
local/honeyports/basic>>>
```
###### Running your module
The interface between a module and the console for the purposes of execution is specified in the manual as so.  Each module will include in it a class of commands.  These commands are required to parse the variables sent from the console, into terms that are understandable for the module.  These commands then execute the module in the manner specified by the specific command.
Though many modules contain specialty commands, the most common command to see is the *run* command.
You can get a listing of the command for your currently loaded module by running `list commands`
If the module supports the defaultl *run* command, you will also notice the command *run -j* in the output to `list commands`.  This permutation of *run* tells the module to fork an individual process and run in the background.
This feature can be incredibly useful if you need to run more than one module at a time.
To execute your module, simply run the desired module specific command, as printed in the output of `list commands`.
Most of the time this will be a simple `run` or `run -j`

### Resources
For now, the resources are pretty simple.  You have this file.  You have the docs inside the docs folder.  You have the scripts inside the scripts folder (which are great if you need example commands).  The modules are all located in the modules folder (and subpaths).  
You can contact my creator on Twitter if you need his help with anything.
@zaeyx





