#!/bin/bash

# vim: tabstop=4 shiftwidth=4 softtabstop=4
# -*- sh-basic-offset: 4 -*-

NATWEST_LOGIN_ITEM="${NATWEST_LOGIN_ITEM:=Natwest}"
NATWEST_PIN_ITEM="${NATWEST_PIN_ITEM:=Natwest PIN}"

if [ -z "$OP_ORG" ]; then
    echo "1Password organization not set."
    exit 1
fi

# Collect user input
IFS=' '
echo -n "Enter the requested requested PIN numbers (e.g. 1 2 3) and press [ENTER]: " 
read -ra PIN_OBJECTS

if [ -z "$PIN_OBJECTS" ]; then
    echo "The PIN objects are required."
    exit 1
fi

echo -n "Enter the requested requested password characters (e.g. 1 2 3) and press [ENTER]: " 
read -ra PASSWORD_OBJECTS

if [ -z "$PASSWORD_OBJECTS" ]; then
    echo "The password objects are required."
    exit 1
fi

# Get the 1password environment
eval $(op signin "$OP_ORG")

# Get the password and PIN
PASSWORD=$(op get item "$NATWEST_LOGIN_ITEM" | jq -r '.details.fields[] | select(.designation=="password").value')
PIN=$(op get item "$NATWEST_PIN_ITEM" | jq -r '.details.fields[] | select(.designation=="password").value')

# Print back the data
for p in "${PIN_OBJECTS[@]}"; do
    # We need to offset the item below by one
    offset=$(($p-1))
    echo ${PIN:$offset:1} 
done

echo "The requested password items are as follows:"
for p in "${PASSWORD_OBJECTS[@]}"; do
    # We need to offset the item below by one
    offset=$(($p-1))
    echo ${PASSWORD:$offset:1} 
done
