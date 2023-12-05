from tdrpa import tdcore

import uiautomation

import keyboard


if __name__ == '__main__':
    #获取UiBot任务栏图标
    selectorTaskbarIcon='''
[
  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'explorer.exe') ] } ,
  { 'ctrl' : [ ('AutomationId' , '40965') ] } ,
  { 'ctrl' : [ ('Text' , '运行中的应用程序') , ('aaRole' , '10') ] } ,
  { 'ctrl' : [ ('Text' , '运行中的应用程序') , ('aaRole' , '22') ] } ,
  { 'ctrl' : [ ('Text' , 'Creator') , ('aaRole' , '43') ] }
]
'''
    taskbarIcon=tdcore.LocatorWindows.findElement(selectorTaskbarIcon)._element

    #双击UiBot任务栏图标，让它显示在最上层
    taskbarIcon.DoubleClick()

    #获取UiBot主窗口元素
    selectorUiBotWnd='''
[
  { 'wnd' : [ ('Text' , 'Creator') , ('aaRole' , '16') , ('App' , 'UiBot.exe') ] } ,
]
'''
    wnd=tdcore.LocatorWindows.findElement(selectorUiBotWnd)._element

    #显示并最大化窗口
    wnd.ShowWindow(uiautomation.SW.ShowMaximized)
    
    #F5 "运行"
    keyboard.send('F5')