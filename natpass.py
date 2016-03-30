#!/usr/bin/env python

import os
import sys
import argparse
import settings
from getpass import getpass
from onepassword import Keychain


def find_keychain():
    search_path = [
        '~/Dropbox/1Password.agilekeychain',
        '~/Dropbox/1Password/1Password.agilekeychain',
        '~/1Password.agilekeychain',
        '~/1Password/1Password.agilekeychain',
    ]

    for p in search_path:
        expanded_path = os.path.expanduser(p)
        if os.path.isdir(expanded_path):
            return p
    return False


def arg_validator(string):
    try:
        return int(string)
    except:
        raise argparse.ArgumentTypeError(
            '{} is not a valid input.'.format(string)
        )


def print_generator(password, index):
    real_index = index - 1
    print 'Number {} is {}'.format(index, password[real_index])


def print_greeting():
    print """
 _   _       _  ______
| \ | |     | | | ___ \\
|  \| | __ _| |_| |_/ /_ _ ___ ___
| . ` |/ _` | __|  __/ _` / __/ __|
| |\  | (_| | |_| | | (_| \__ \__ \\
\_| \_/\__,_|\__\_|  \__,_|___/___/

A NatWest password assistance tool by @vpetersson.
"""


def print_pin_splash():
    print """
______ _____ _   _
| ___ \_   _| \ | |
| |_/ / | | |  \| |
|  __/  | | | . ` |
| |    _| |_| |\  |
\_|    \___/\_| \_/

 """


def print_password_splash():
    print """
______                                   _
| ___ \                                 | |
| |_/ /_ _ ___ _____      _____  _ __ __| |
|  __/ _` / __/ __\ \ /\ / / _ \| '__/ _` |
| | | (_| \__ \__ \\\ V  V / (_) | | | (_| |
\_|  \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
"""


def main():
    parser = argparse.ArgumentParser(
        description='NatWest password management tool.'
    )
    parser.add_argument(
        '--pin',
        nargs=3,
        type=arg_validator,
        help='A space separated list of entries, such as 1 3 2.'
    )
    parser.add_argument(
        '--password',
        nargs=3,
        type=arg_validator,
        help='A space separate list of entries, such as 2 4 19.'
    )
    args = parser.parse_args()
    if not (args.pin or args.password):
        parser.print_help()
        sys.exit(1)

    print_greeting()

    keychain_path = find_keychain()
    if not keychain_path:
        print 'Unable to find keychain. Exiting'
        sys.exit(1)

    keychain = Keychain(keychain_path)
    master_password = getpass('Please enter your master password:')

    try:
        keychain.unlock(master_password)
    except ValueError:
        print 'Unable to unlock keychain.'
        sys.exit(1)

    if args.pin:
        try:
            nw_pin = keychain.item(settings.PIN_ITEM).password
        except ValueError:
            print 'Unable to find item {} in the keychain.'.format(settings.PIN_ITEM)
            sys.exit(1)

        print_pin_splash()

        for i in args.pin:
            print_generator(nw_pin, i)

    if args.password:
        try:
            nw_password = keychain.item(settings.PASSWORD_ITEM).password
        except ValueError:
            print 'Unable to find item {} in the keychain.'.format(settings.PASSWORD_ITEM)
            sys.exit(1)

        print_password_splash()

        for i in args.password:
            print_generator(nw_password, i)


if __name__ == "__main__":
    main()
