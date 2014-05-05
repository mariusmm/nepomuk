#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Luca Beltrame <einar@heavensinferno.net>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# <executable> [-r] [-v] <Tagname> <file1> <file2> <file3> ...
# Add tag <Tagname> to files.
# options: -r delete tag
# options: -v verbose

import sys, getopt
import os
from PyQt4.QtCore import *

from PyQt4 import QtCore
from PyKDE4 import kdecore
from PyKDE4.nepomuk import Nepomuk
from PyKDE4.nepomuk import *



def add_tag_to_file( file_name, tag):
  
  file_info = QtCore.QFileInfo(file_name)
  absolute_path = file_info.absoluteFilePath()
  
  if verbose == True:
    print file_name + " <- " + tag.label()

  resource = Nepomuk.Resource(kdecore.KUrl(absolute_path))
  resource.addTag(tag)
  
  return


def remove_tag_to_file( file_name, tag):
  
  file_info = QtCore.QFileInfo(file_name)
  absolute_path = file_info.absoluteFilePath()
 
 
  if verbose == True:
    print file_name + " x " + tag.label()
 
  resource = Nepomuk.Resource(kdecore.KUrl(absolute_path))
  #resource.removeProperty(resource.tagUri()) # remove tags
  #resource.removeProperty(tag.resourceUri()) # remove tag
    
  
  return

def create_tag(tag_name):
  
  tag = Nepomuk.Tag( tag_name )
  tag.setLabel( tag_name )
  
  return tag


def main(argv):

    tag_name = ""
    file_name = ''
    arg_index = 1;
    delete = False;
    global verbose;
    verbose = False;
    app_name = "nepomuk_add_tag"
    program_name = kdecore.ki18n("Manage Nepomuk's tags from commandline")
    about_data = kdecore.KAboutData(QtCore.QByteArray(app_name), "",
                                program_name, QtCore.QByteArray("0.1"))

    kdecore.KCmdLineArgs.init(sys.argv, about_data)

    #the following line can be needed (?)
    #but then the program ends with a seg. fault (???!!!)
    #app = QCoreApplication(sys.argv)

    if sys.argv[arg_index] == "-r":
      print "delete"
      arg_index = arg_index + 1
      delete = True
    
    if sys.argv[arg_index] == "-v":
      arg_index = arg_index + 1
      verbose = True;
      
    tag_name = sys.argv[arg_index]
    tag = create_tag(tag_name)
    
    for i in xrange(len(sys.argv)):
      if (i > arg_index):
	
	file_name = sys.argv[i]
	 
	if delete == False:
	  #Adding tag to file
	  add_tag_to_file(file_name, tag)
	else:
	  #Removing Tag to file
	  remove_tag_to_file(file_name, tag)
	  
	  


    #remove_tag_to_file("dummy.txt", tag)

if __name__ == '__main__':
    main(sys.argv[1:])
