# NatPass
NatPass is a password assistance tool that helps dealing with NatWest's annoying password system.

# Requirement

* Mac OS X
* Python 2.7 (The 1pass library doesn't support Python 3)
* 1Password
  * An entry in 1Password that holds your NatWest password (default 'Natwest')
  * An entry in 1Password that holds your NatWest online PIN (default 'Natwest PIN')
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

To override the default entries ('Natwest' and 'Natwest PIN'), you can export the environment variables 'PASSWORD_ITEM' and 'PIN_ITEM'.

You might also want to create a shorthand script as follows to more easily work with Natpass. Here's one example:

```
#!/bin/bash

NATPASS="/path/to/natpass"
export PIN_ITEM="Your PIN Item"
export PWD_ITEM="Your Password Item"

cd "$NATPASS"
source "venv/bin/activate"

python natpass.py "$@"
```

# Troubleshooting

If you're having issues installing m2crypto on macOS, try the following ([credits](https://stackoverflow.com/questions/33005354/trouble-installing-m2crypto-with-pip-on-os-x-macos)):

```
brew install openssl
brew install swig
env LDFLAGS="-L$(brew --prefix openssl)/lib" \                                                                                                ⏎ ✹
CFLAGS="-I$(brew --prefix openssl)/include" \
SWIG_FEATURES="-cpperraswarn -includeall -I$(brew --prefix openssl)/include" \
pip install m2crypto==0.26.0
```
