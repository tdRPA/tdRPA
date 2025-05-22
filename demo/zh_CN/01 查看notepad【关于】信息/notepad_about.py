#导入tdcore包
from tdrpa.tdcore import LocatorWindows

#获取'Desktop'根元素
desktop=LocatorWindows.findElement()
#输出元素Name属性
print(desktop.Name)

#打开notepad.exe
import os
os.popen('notepad.exe')

#等待1秒
import time
time.sleep(1)

#点击'帮助'菜单栏
helpSelector="[  { 'wnd' : [ ('Text' , '无标题 - 记事本') , ('aaRole' , 'Client') , ('App' , 'notepad.exe') ] } ,  { 'ctrl' : [ ('AutomationId' , 'MenuBar') , ('Text' , '应用程序') ] } ,  { 'ctrl' : [ ('Text' , '帮助(H)') , ('aaRole' , 'MenuItem') ] }]"
helpElement=LocatorWindows.findElement(helpSelector)
helpElement.Click()

#点击'关于'菜单项
aboutSelector="[  { 'wnd' : [ ('Text' , '无标题 - 记事本') , ('aaRole' , 'Client') , ('App' , 'notepad.exe') ] } ,  { 'wnd' : [ ('Text' , '帮助(H)') , ('aaRole' , 'MenuPopup') ] } ,  { 'ctrl' : [ ('Text' , '关于记事本(A)') , ('aaRole' , 'MenuItem') ] }]"
aboutElement=LocatorWindows.findElement(aboutSelector)
aboutElement.Click()

#"element"的属性和方法，见"uiautomation" https://pypi.org/project/uiautomation/ 开源库，或使用带代码补全和智能提示的编程环境