import os, sys, time, pprint
from subprocess import check_output

class OS:
  def __init__(self):
    sysname, host_name, kernel = os.uname()[0:3]

    self.sysname = sysname
    self.host_name = host_name
    self.kernel = kernel
  
  def getOSInfo(self):
    return "{} {} {}".format(self.sysname, self.host_name, self.kernel)
  
  def getAllPackages(self):
    self.packages = check_output(["apt", "list", "--installed"])

    return self.packages

o = OS()

print(o.getOSInfo())

pkgs = o.getAllPackages()

pprint.pprint(pkgs.split())

