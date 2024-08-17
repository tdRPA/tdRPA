from tdrpa import tdcore

import keyboard


if __name__ == '__main__':
    #获取UiBot任务栏图标
    selectorTaskbarIcon='''
[
  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'explorer.exe') ] } ,
  { 'ctrl' : [ ('AutomationId' , '40965') ] } ,
  { 'ctrl' : [ ('Text' , '运行中的应用程序') , ('aaRole' , '10') ] } ,
  { 'ctrl' : [ ('Text' , '运行中的应用程序') , ('aaRole' , '22') ] } ,
  { 'ctrl' : [ ('AutomationId' , 'UiBot-creator-5.6.0') ] }
]
'''
    taskbarIcon=tdcore.LocatorWindows.findElement(selectorTaskbarIcon)

    #双击UiBot任务栏图标，让它显示在最上层
    taskbarIcon.DoubleClick()

    #F5 "运行"
    keyboard.send('F5')