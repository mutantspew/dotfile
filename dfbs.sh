#!/bin/env sh

# Dot File Bootstrap Script (dfbs)
# by Jacob Joslin <mutantspew@gmail.com>

# some ideas taken from Luke Smith <luke@lukesmith.xyz>

# License: GNU GPLv3

while getopts ":ah" o; do case "${o}" in
  h) echo "HALP" && exit ;;
  a) packagemanager="pacman -Sy" ;;
  *) echo "-$OPTARG is not a valid option." && exit ;;
esac done

# default ubuntu
# if arch do blah blah
# if distro do blah blah
# pass package manager and no confirm via args

# defaults
[ -z ${packagemanager+x} ] && packagemanager="apt install"

# make sure python is installed
sudo $packagemanager python3 pip3 python3-dialog

# download python scripts and program list
curl "" > "dfbs.py"
curl "" > "progs.csv"

# run the script
sudo python3 "dfbs.py" #args

# clear the screen before quiting
# clear