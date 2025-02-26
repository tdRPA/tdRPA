from tdrpa.tdworker import *


def do():
    ###### 长时间不用会自动退出，检测登录窗口存在就登录下
    #登录窗口密码控件
    selector="[  { 'wnd' : [ ('aaRole' , '18') , ('App' , 'tdxw.exe') ] } ,  { 'ctrl' : [ ('ControlType' , 'Pane') , ('ClassName' , 'SafeEdit') ] }]"
    if WinElement.Exists(selector):
        #登录按钮找不到控件，通过密码控件作为锚点，偏移鼠标解决
        WinMouse.Action(selector,cursorOffsetY=70,delayAfter=8000)

    #选项菜单
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'ctrl' : [ ('AutomationId' , '12289') ] } ,  { 'ctrl' : [ ('AutomationId' , '3020') ] }]"
    WinMouse.Action(selector)

    #自定义板块设置菜单项
    selector="[  { 'wnd' : [ ('Text' , '上下文') , ('aaRole' , '11') , ('App' , 'tdxw.exe') ] } ,  { 'ctrl' : [ ('AutomationId' , '9051') , ('Text' , '自定义板块设置') ] }]"
    WinMouse.Action(selector,setForeground=False)





if __name__ == '__main__':
    do()