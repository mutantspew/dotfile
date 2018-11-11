from dialog import Dialog
import os
import sys
import time
import argparse

class OSPackage:
  package_manager = "apt install"
  package_manager_no_confirm = "-y"

def clear():
  os.system('clear')

def clearAndExit():
  os.system('clear')
  sys.exit()

def downloadDotFiles():
  d.infobox("Downloading dotfiles")
  time.sleep(3)
  #download with curl?
  #probably git clone dotfiles

def preinstall():
  for x in range(10):
    installPackage(x)

def linkDotFiles():
  pass

# def set_args(parser):
  # parser.add_argument()
  # add default ubuntu
  # add change pacman
  # add change package file
  # add change dotfile git

def setArgs():
  parser = argparse.ArgumentParser()

  # set_args()

  args = parser.parse_args()

def installPackage(package):
  d.infobox("Installing package '{}'".format(package))
  time.sleep(2)
  #install package here

def finalize():
  d.msgbox("Finished install")

# PASS OPTIONS???
# ARGS?????
setArgs()

d = Dialog(dialog="dialog", autowidgetsize=True)

d.set_background_title("Dotfiles Bootstrapper")

welcome_msg = """Welcome to Jacob's Dotfile Bootstrapper
Written by: Jacob Joslin
Email: <mutantspew@gmail.com>

License: GNU GPLv3"""

d.msgbox(welcome_msg)

# replace with menu, menu selects linking, or installing
if d.yesno("Ready to start?") == d.CANCEL:
  clearAndExit()

#install backend
d.msgbox("First we install some files")
preinstall()

# download dotfiles
d.msgbox("Now, we will link the dotfiles")
downloadDotFiles()

# link dotfiles
d.msgbox("Linking files")
linkDotFiles()

finalize()
clear()