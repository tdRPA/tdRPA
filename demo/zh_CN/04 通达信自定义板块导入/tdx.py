'''
本流程演示了如何通过tdRPA自动化通达信金融终端（模拟交易V7.642版本）中的自定义板块设置列表。
用户（即本人：有闲王员外）每天晚上会通过数据分析生成三个列表文件，分别是bounce.txt（震荡策略）、up.txt（追高策略）和b3.txt（回调策略）。随后，这些列表将被导入到通达信软件的自定义板块中。
由于每天手动导入这些列表颇为繁琐，因此开发了此自动化流程以简化导入操作，大大提高了效率。
关于具体工具的使用方法，请搜索tdRPA获取更多信息。
'''
import sys

from datetime import datetime

from tdrpa.tdworker import *


#清空并导入list
def clear_then_import(filePath):
    #点清空
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'ctrl' : [ ('Text' , '自定义板块管理') , ('aaRole' , '38') ] } ,  { 'ctrl' : [ ('ControlType' , 'Button') , ('Text' , '清空') ] }]"
    WinMouse.Action(selector)

    #点确定
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'wnd' : [ ('Text' , '自定义板块设置') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('ControlType' , 'Button') , ('Text' , '确定') ] , 'index' : '1' }]"
    WinMouse.Action(selector)

    #导入板块
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'ctrl' : [ ('Text' , '自定义板块管理') , ('aaRole' , '38') ] } ,  { 'ctrl' : [ ('Text' , '导入板块∨') ] }]"
    WinMouse.Action(selector)

    #从文本导入
    selector="[  { 'wnd' : [ ('aaRole' , '11') , ('App' , 'tdxw.exe') ] } ,  { 'ctrl' : [ ('Text' , '从文本中导入') ] }]"
    WinMouse.Action(selector)

    #选择文件
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'wnd' : [ ('Text' , '自定义板块设置') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('Text' , '取文本文件..') ] }]"
    WinMouse.Action(selector)

    #输入文件路径
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'wnd' : [ ('Text' , '打开') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('Text' , '文件名(N):') ] , 'index' : '1' } ,  { 'ctrl' : [ ('Text' , '文件名(N):') ] }]"
    WinKeyboard.InputText(selector,filePath)

    #点打开
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'wnd' : [ ('Text' , '自定义板块设置') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('Text' , '打开(O)') ] }]"
    WinMouse.Action(selector)

    #点确定
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'wnd' : [ ('Text' , '自定义板块设置') , ('aaRole' , '18') ] } ,  { 'wnd' : [ ('Text' , '从文本中导入') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('Text' , '确定') ] }]"
    WinMouse.Action(selector)

    #提示弹框确定
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'wnd' : [ ('Text' , '自定义板块设置') , ('aaRole' , '18') ] } ,  { 'wnd' : [ ('Text' , 'TdxW') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('Text' , '确定') ] }]"
    WinMouse.Action(selector)

def do(shift):
    ###### 长时间不用会自动退出，检测登录窗口存在就登录下
    #登录窗口密码控件
    selector="[  { 'wnd' : [ ('aaRole' , '18') , ('App' , 'tdxw.exe') ] } ,  { 'ctrl' : [ ('ControlType' , 'Pane') , ('ClassName' , 'SafeEdit') ] }]"
    if WinElement.Exists(selector):
        #登录按钮找不到控件，通过密码控件作为锚点，偏移鼠标解决
        WinMouse.Action(selector,cursorOffsetY=70,delayAfter=8000)
    else:
        #双击任务栏图标显示主窗口
        selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'explorer.exe') ] } ,  { 'ctrl' : [ ('Text' , '*通达信金融终端*' , 'fuzz') ] }]"
        WinMouse.Action(selector,clickType='dblclick')

    #关闭可能出现的广告弹窗，关闭按钮X选不到，就用窗口右上角偏移一点去点
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'wnd' : [ ('Text' , '通达信信息') , ('aaRole' , '18') ] }]"
    WinMouse.Action(selector,cursorPosition='topRight',cursorOffsetX=-8,cursorOffsetY=8,continueOnError=True,searchDelay=2000)
    
    #快捷键方式打开自定义板块设置
    WinKeyboard.Press('.')
    WinKeyboard.Press('9')
    WinKeyboard.Press('3')
    WinKeyboard.Press('1')
    WinKeyboard.Press('Enter')

    ###### 主体导入功能开始
    #震荡list，点bounce
    btnText='bounce'
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'ctrl' : [ ('Text' , '自定义板块管理') , ('aaRole' , '38') ] } ,  { 'ctrl' : [ ('Text' , '%s') , ('aaRole' , '34') ] }]" % btnText
    WinMouse.Action(selector,cursorPosition='topLeft')
    clear_then_import(r'C:\Dev\_sync_\sTide\bounce.txt')

    weekDay=datetime.now().isoweekday() % 7 + shift
    #追高list，点up_X, X是星期几的数字
    btnText='up_%d' % weekDay
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'ctrl' : [ ('Text' , '自定义板块管理') , ('aaRole' , '38') ] } ,  { 'ctrl' : [ ('Text' , '%s') , ('aaRole' , '34') ] }]" % btnText
    WinMouse.Action(selector,cursorPosition='topLeft')
    clear_then_import(r'C:\Dev\_sync_\sTide\up.txt')

    #回调list，点back_X, X是星期几的数字
    btnText='back_%d' % weekDay
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'ctrl' : [ ('Text' , '自定义板块管理') , ('aaRole' , '38') ] } ,  { 'ctrl' : [ ('Text' , '%s') , ('aaRole' , '34') ] }]" % btnText
    WinMouse.Action(selector,cursorPosition='topLeft')
    clear_then_import(r'C:\Dev\_sync_\sTide\b3.txt')

    #关闭板块
    selector="[  { 'wnd' : [ ('aaRole' , '10') , ('App' , 'tdxw.exe') ] } ,  { 'wnd' : [ ('Text' , '自定义板块设置') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('Text' , '确定') ] }]"
    #WinMouse.Action(selector)



if __name__ == '__main__':
    #shift 日期调整值，当天晚上导入的数据供明天用，所以是1
    shift=int(sys.argv[1])
    do(shift)