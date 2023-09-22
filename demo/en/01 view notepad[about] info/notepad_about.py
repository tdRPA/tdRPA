#import tdcore module
from tdrpa import tdcore

#get 'Desktop' root element
desktop=tdcore.LocatorWindows.findElement()
#print root 'Name' property
print(desktop._element.Name)

#open 'notepad.exe'
import os
os.popen('notepad.exe')

#wait 1 second
import time
time.sleep(1)

#click 'Help' menu
helpSelector="[  { 'wnd' : [ ('Text' , 'Untitled - Notepad') , ('aaRole' , '10') , ('App' , 'notepad.exe') ] } ,  { 'ctrl' : [ ('AutomationId' , 'MenuBar') , ('Text' , 'Application') ] } ,  { 'ctrl' : [ ('Text' , 'Help') , ('aaRole' , '12') ] }]"
helpElement=tdcore.LocatorWindows.findElement(helpSelector)
helpElement._element.Click()

#click 'About' item
aboutSelector="[  { 'wnd' : [ ('Text' , 'Untitled - Notepad') , ('aaRole' , '10') , ('App' , 'notepad.exe') ] } ,  { 'wnd' : [ ('Text' , 'Help') , ('aaRole' , '11') ] } ,  { 'ctrl' : [ ('AutomationId' , '65') , ('Text' , 'About Notepad') ] }]"
aboutElement=tdcore.LocatorWindows.findElement(aboutSelector)
aboutElement._element.Click()

#For the properties and methods of "_element", please refer to the "uiautomation" https://pypi.org/project/uiautomation/ open-source library or use a programming environment with code completion and intelligent suggestions