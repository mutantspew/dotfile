from dialog import Dialog
import os
import sys
import time
# import argparse
import requests

# inputbox for custom download url,filename??
#   use for custom program.csv's?

def downloadFile(url, filename):
  d.gauge_start(width = 60, text = "Downloading file {}".format(filename)) # start the dialog widget

  d.gauge_update(0)

  with open(filename, 'wb') as file:
    resp = requests.get(url, stream=True)
    total_len = resp.headers.get('content-length')

    if total_len is None: # no content length header
      file.write(resp.content)
      d.gauge_update(100)
    else:
      dl = 0
      total_len = int(total_len)
      for data in resp.iter_content(chunk_size=4096):
        dl += len(data)
        file.write(data)
        done = int(dl / total_len)

        time.sleep(1)

        d.gauge_update(done)

  exit_code = d.gauge_stop() # clean up

  return exit_code

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

def installLoop():
  for x in range(10):
    installPackage(x)

def dotFilesLoop():
  d.msgbox("Test")

  url = "https://www.gettyimages.ie/gi-resources/images/Homepage/Hero/UK/CMS_Creative_164657191_Kingfisher.jpg"
  downloadFile(url, "FileName1.jpg")

# def set_args(parser):
  # parser.add_argument()
  # add default ubuntu
  # add change pacman
  # add change package file
  # add change dotfile git

# def setArgs():
#   parser = argparse.ArgumentParser()

  # set_args()

  # args = parser.parse_args()

def installPackage(package):
  d.infobox("Installing package '{}'".format(package))
  time.sleep(2)
  #install package here

def finalize():
  d.msgbox("Finished setup")

def mainMenu():
  choices = [("Install", "Install packages for this system"),
             ("Config", "Download dotfiles for this system"),
             ("Exit", "Exit script")]

  code, tag = d.menu("Main menu", choices=choices)

  if code == d.OK:
    if(tag == "Exit"):
      return True
    elif (tag == "Config"):
      dotFilesLoop()
    elif (tag == "Install"):
      installLoop()
  else:
    return True

# PASS OPTIONS???
# ARGS?????
# setArgs()

d = Dialog(dialog="dialog", autowidgetsize=True)

d.set_background_title("Dotfiles Bootstrapper")

welcome_msg = """Welcome to Jacob's Dotfile Bootstrapper
Written by: Jacob Joslin
Email: <mutantspew@gmail.com>

License: GNU GPLv3"""

d.msgbox(welcome_msg)

exit = False
while not exit:
  exit = mainMenu()

#install backend
# d.msgbox("First we install some files")
# preinstall()

# download dotfiles
# d.msgbox("Now, we will link the dotfiles")
# downloadDotFiles()

# link dotfiles
# d.msgbox("Linking files")
# linkDotFiles()

finalize()
clear()