# NatPass
NatPass is a password assistance tool that helps dealing with NatWest's annoying password system.

# Requirement

* Mac OS X
* 1Password
  * An entry in 1Password named 'NatWest' that holds your account password
  * An entry in 1Password named 'NatWest PIN' that holds your PIN
* A NatWest account (d'oh!)

# Usage

Whenever you log into NatWest, you're prompted with a dialogue like this:

![Netwest Login](img/natwest_prompt.png)

Well, if you're a modern human being, you're most likely using a password management tool (such as 1Password). This login page is far from compatible with modern password practices.

To solve this, I whipped up a Python tool that to simplify this. Enter NatPass.

```
$ ./natpass.py --pin 1 2 3 --password 2 16 17

 _   _       _  ______
| \ | |     | | | ___ \
|  \| | __ _| |_| |_/ /_ _ ___ ___
| . ` |/ _` | __|  __/ _` / __/ __|
| |\  | (_| | |_| | | (_| \__ \__ \
\_| \_/\__,_|\__\_|  \__,_|___/___/

A NatWest password assistance tool by @vpetersson.

Please enter your master password:

______ _____ _   _
| ___ \_   _| \ | |
| |_/ / | | |  \| |
|  __/  | | | . ` |
| |    _| |_| |\  |
\_|    \___/\_| \_/


Number 1 is f
Number 2 is o
Number 3 is o

______                                   _
| ___ \                                 | |
| |_/ /_ _ ___ _____      _____  _ __ __| |
|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` |
| | | (_| \__ \__  \ V  V / (_) | | | (_| |
\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|

Number 2 is b
Number 16 is a
Number 17 is r
```

# Installation

```
$ pip install -r requirements.txt
$ ./natpass.py --help
```
