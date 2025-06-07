"""
特别声明：
本代码仅供演示tdRPA功能使用，不得用于任何非法、违规或未经授权的操作。
使用者须自行承担因使用本代码引发的一切法律责任，tdRPA开发方不承担任何直接或间接责任。
请严格遵守相关法律法规，谨慎合法使用。
"""

from tdrpa.tdworker import WinElement
from tdrpa.tdworker import WinKeyboard
from tdrpa.tdworker import WinMouse
from tdrpa.tdworker import Window

import re

from data import config # 发送群消息配置 key/value key：群名字开始字符串；value：群发消息内容

import log
logger=log.getLogger('log')

import traceback


def main():
    logger.info('====  开始 ====')

    #最大化微信窗口并置顶
    selectorString = "[  { 'wnd' : [ ('Text' , '微信') , ('aaRole' , '10') , ('App' , 'WeChat.exe') ] } ]"
    Window.SetActive(selectorString)
    Window.Show(selectorString,'max')

    #按照配置逐个群发
    for key,value in config.items():
        try:
            logger.info('---- %s ----' % key)

            #点通讯录
            selectorString = "[  { 'wnd' : [ ('Text' , '微信') , ('aaRole' , '10') , ('App' , 'WeChat.exe') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('Text' , '导航') , ('aaRole' , '22') ] } ,  { 'ctrl' : [ ('Text' , '通讯录') , ('aaRole' , '43') ] }]"
            WinMouse.Action(selectorString)

            #搜索框输入
            selectorString = "[  { 'wnd' : [ ('Text' , '微信') , ('aaRole' , '10') , ('App' , 'WeChat.exe') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('Text' , '搜索') , ('aaRole' , '42') ] }]"
            WinKeyboard.InputText(selectorString,key,clickBeforeInput=True,delayAfter=2000)

            #点群聊的显示全部，有可能没有此控件
            selectorString = "[  { 'wnd' : [ ('Text' , '微信') , ('aaRole' , '10') , ('App' , 'WeChat.exe') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('Text' , '@str:IDS_FAV_SEARCH_RESULT:3780') , ('aaRole' , '33') ] } ,  { 'ctrl' : [ ('Text' , '显示全部*' , 'fuzz') , ('aaRole' , '34') ] , 'index' : '1' }]"
            WinMouse.Action(selectorString,searchDelay=1000,continueOnError=True)
            selectorString = "[  { 'wnd' : [ ('Text' , '微信') , ('aaRole' , '10') , ('App' , 'WeChat.exe') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('Text' , '@str:IDS_FAV_SEARCH_RESULT:3780') , ('aaRole' , '33') ] } ,  { 'ctrl' : [ ('Text' , '显示全部*' , 'fuzz') , ('aaRole' , '34') ] }]"
            WinMouse.Action(selectorString,searchDelay=1000,continueOnError=True)
            
            #鼠标滚动，使群名字都显示出来，微信可能用到了lazy display，不在可视区名字是空的
            WinMouse.Move(150,200)
            WinMouse.Wheel(30)

            #获取到搜索结果群List
            selectorString = "[  { 'wnd' : [ ('Text' , '微信') , ('aaRole' , '10') , ('App' , 'WeChat.exe') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('Text' , '@str:IDS_FAV_SEARCH_RESULT:3780') , ('aaRole' , '33') ] } ,  { 'ctrl' : [ ('Text' , '群聊') , ('aaRole' , '41') ] }]"
            群聊分组Control=WinElement.FindElementByTd(selectorString)
            群聊的上一个Control=WinElement.GetParent(群聊分组Control)

            群聊List=[]
            while True:
                nextControl=WinElement.GetSibling(群聊的上一个Control)
                群聊的上一个Control=nextControl
                #挑选出是群聊的
                if nextControl and nextControl.ControlTypeName=='ListItemControl':  #控件类型，换其它不是群聊的，会以Panel过渡
                    selectorString = "[  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '43') ] }]"
                    群聊头像Control=WinElement.FindElementByTd(selectorString,nextControl,searchDelay=200,continueOnError=True)
                    if 群聊头像Control: #有头像，换其它，不会带头像
                        selectorString = "[  { 'ctrl' : [ ('Text' , '<em>%s</em>*' , 'fuzz') , ('aaRole' , '41') ] }]" % key
                        符合条件的群聊Control=WinElement.FindElementByTd(selectorString,nextControl,searchDelay=200,continueOnError=True)
                        if 符合条件的群聊Control:
                            群聊List.append(符合条件的群聊Control.Name)
                        continue
                break
                    
            logger.info('找到群聊个数:%d' % len(群聊List))
            logger.info(群聊List)

            #开始群发
            send(群聊List,value)
        except Exception as e:
            logger.error(traceback.format_exc())

    logger.info('====  结束 ====')
    
def send(groups,msg):
    logger.info('开始群发')
    for group in groups:
        群名字=re.sub(r'<em>(.+?)</em>',r'\1',group)
        logger.info('发送到群：%s' % 群名字)

        #点通讯录
        selectorString = "[  { 'wnd' : [ ('Text' , '微信') , ('aaRole' , '10') , ('App' , 'WeChat.exe') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('Text' , '导航') , ('aaRole' , '22') ] } ,  { 'ctrl' : [ ('Text' , '通讯录') , ('aaRole' , '43') ] }]"
        WinMouse.Action(selectorString)

        #搜索框输入
        selectorString = "[  { 'wnd' : [ ('Text' , '微信') , ('aaRole' , '10') , ('App' , 'WeChat.exe') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('Text' , '搜索') , ('aaRole' , '42') ] }]"
        WinKeyboard.InputText(selectorString,群名字,clickBeforeInput=True,delayAfter=2000)

        #点目标群名字，切换到发送窗口
        selectorString = "[  { 'wnd' : [ ('Text' , '微信') , ('aaRole' , '10') , ('App' , 'WeChat.exe') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('Text' , '@str:IDS_FAV_SEARCH_RESULT:3780') , ('aaRole' , '33') ] } ,  { 'ctrl' : [ ('Text' , '%s') , ('aaRole' , '34') ] }]" % 群名字
        WinMouse.Action(selectorString)

        #输入群发消息
        selectorString = "[  { 'wnd' : [ ('Text' , '微信') , ('aaRole' , '10') , ('App' , 'WeChat.exe') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] }]"
        WinKeyboard.InputText(selectorString,msg)

        #点发送按钮
        selectorString = "[  { 'wnd' : [ ('Text' , '微信') , ('aaRole' , '10') , ('App' , 'WeChat.exe') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '16') ] , 'index' : '2' } ,  { 'ctrl' : [ ('Text' , '发送(S)') , ('aaRole' , '43') ] }]"
        WinMouse.Action(selectorString,delayAfter=3000)
        logger.info('已发送')

    logger.info('群发完毕')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(traceback.format_exc())