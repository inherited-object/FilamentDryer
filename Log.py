#!/usr/bin/env python

__author__      = "Inherited Object"
__source__      = "github.com/inherited-object/FilamentDryer"
__copyright__   = "Copyright 2024, Inherited Object"

# Collect & store activity
# @TODO add levels of logging (e.g. None, Some, More, Allot...)



import re
from _ast import Try
from apt_pkg import DATE
import datetime
#from os.path import exists
#from os import path
import os
#from ast import _new

class Log:
    def __init__(self, _filePath, _tryCreate = True):
        self.filePath = _filePath

        if(_tryCreate == True):
            self.logCreated = self.create()
        
    def create(self):
        _created = False
        if(self.filePath != ""):
            if(os.path.exists(self.filePath) == False):
                _action = "Log Created, Logging Started"
                
            if(os.path.exists(self.filePath) == True):
                if(os.stat(self.filePath).st_size > 5):
                    _action = "\n\n---------------------------------------\n---------------------------------------\nPreviously Created, Logging Restarted"
                else:
                    _action = "Previously Created, Logging Started"
            
            try:
                f = open(self.filePath, "a")
                dt = datetime.datetime.now()
                f.write("\n{} - {}".format(dt.strftime("%Y-%m-%d %H:%M:%S"), _action))
                f.close()
            except NameError:
                print("UNABLE TO CREATE LOG FILE")
                
        else:
            print("self.filePath is empty")
            
        return _created
        
    def addEntry(self, _entryText, _newlinePrefix = True, _dateStamp = True, _separatorText = " - "):
                
        try:
            f = open(self.filePath, "a")
            dt = datetime.datetime.now()
            f.write("{}{}{}{}".format("\n" if _newlinePrefix else "", dt.strftime("%Y-%m-%d %H:%M:%S") if _dateStamp else "", _separatorText, _entryText))
            f.close()
        except:
            create = False
        
