import os
import time
from datetime import datetime

from tdrpa.tdworker import *

from config import config

import shutil

from tenacity import *


@retry(reraise=True,stop=stop_after_attempt(int(config['business']['retry'])),wait=wait_fixed(3))
def process():
    os.makedirs(r'c:\!!!tdRPA_temp',exist_ok=True)

    App.Kill('IvyOfdReader.exe')
    App.Run(config['system']['ofdReader'])

    inbox=config['data']['inbox']

    for root, dirs, files in os.walk(inbox):
        for file in files:
            file=os.path.join(os.path.abspath(root),file).lower()
            path, ext = os.path.splitext(file)
            if ext=='.ofd':
                ofdFile=file
                pdfFile=path+'.pdf'
                if not os.path.exists(pdfFile):
                    convert(ofdFile,pdfFile)
                    timestamp= datetime.now().strftime('%Y-%m-%d_%H-%M-%S_')
                    moveFile(ofdFile,config['data']['ofd'],timestamp)
                    #检查文件下载是否成功
                    if not os.path.exists(pdfFile):
                        raise FileExistsError('convert failed')
                    
    time.sleep(3)
    App.Kill('IvyOfdReader.exe')

def moveFile(filePath,newFolder,timestamp):
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)
    fileName = timestamp + os.path.basename(filePath)
    newfilePath = os.path.join(newFolder,fileName)
    shutil.move(filePath,newfilePath)

def convert(ofdFile,pdfFile):
    #点PDF菜单
    selector="[  { 'wnd' : [ ('AutomationId' , 'frmMain') , ('App' , 'IvyOfdReader.exe') ] } ,  { 'ctrl' : [ ('AutomationId' , 'mainToolBar1') ] } ,  { 'ctrl' : [ ('AutomationId' , 'jButtonPdf') ] }]"
    WinMouse.Action(selector,delayAfter=1000)

    #选定ofd文件转换为pdf
    selector="[  { 'wnd' : [ ('AutomationId' , 'frmMain') , ('App' , 'IvyOfdReader.exe') ] } ,  { 'wnd' : [ ('Text' , 'DropDown') , ('aaRole' , '11') ] } ,  { 'ctrl' : [ ('Text' , '选定ofd文件转换为pdf') , ('aaRole' , '12') ] }]"
    WinMouse.Action(selector,delayAfter=1000)

    #输入文件路径
    selector="[  { 'wnd' : [ ('AutomationId' , 'frmMain') , ('App' , 'IvyOfdReader.exe') ] } ,  { 'wnd' : [ ('Text' , '请选择要转换的ofd文件') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('ControlType' , 'Pane') ] , 'index' : '1' } ,  { 'ctrl' : [ ('ControlType' , 'ComboBox') , ('Text' , '文件名(N):') ] } ,  { 'ctrl' : [ ('ControlType' , 'Edit') , ('Text' , '文件名(N):') ] }]"
    WinKeyboard.InputText(selector,content=ofdFile)

    #点打开
    selector="[  { 'wnd' : [ ('AutomationId' , 'frmMain') , ('App' , 'IvyOfdReader.exe') ] } ,  { 'wnd' : [ ('Text' , '请选择要转换的ofd文件') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('Text' , '打开(O)') ] }]"
    WinMouse.Action(selector,delayAfter=1000)

    #点恢复缺省参数
    selector="[  { 'wnd' : [ ('AutomationId' , 'frmMain') , ('App' , 'IvyOfdReader.exe') ] } ,  { 'wnd' : [ ('AutomationId' , 'frmPdfVx') , ('Text' , 'ofd文件转换为Pdf文件') ] } ,  { 'ctrl' : [ ('AutomationId' , 'groupBox5') , ('Text' , '发票章参数') ] } ,  { 'ctrl' : [ ('AutomationId' , 'button11') , ('Text' , '恢复缺省参数') ] }]"
    WinMouse.Action(selector,delayAfter=1000)

    #点转为Pdf
    selector="[  { 'wnd' : [ ('AutomationId' , 'frmMain') , ('App' , 'IvyOfdReader.exe') ] } ,  { 'wnd' : [ ('AutomationId' , 'frmPdfVx') , ('Text' , 'ofd文件转换为Pdf文件') ] } ,  { 'ctrl' : [ ('AutomationId' , 'button1') , ('Text' , '转为Pdf') ] }]"
    WinMouse.Action(selector,delayAfter=1000)

    #点C:盘
    selector="[  { 'wnd' : [ ('AutomationId' , 'frmMain') , ('App' , 'IvyOfdReader.exe') ] } ,  { 'wnd' : [ ('AutomationId' , 'frmPdfVx') , ('Text' , 'ofd文件转换为Pdf文件') ] } ,  { 'wnd' : [ ('Text' , '浏览文件夹') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('Text' , '请选择输出pdf文件的路径') , ('aaRole' , '10') ] } ,  { 'ctrl' : [ ('Text' , '请选择输出pdf文件的路径') ] } ,  { 'ctrl' : [ ('Text' , '桌面') , ('aaRole' , '36') ] } ,  { 'ctrl' : [ ('Text' , '此电脑') , ('aaRole' , '36') ] } ,  { 'ctrl' : [ ('Text' , '本地磁盘 (C:)') , ('aaRole' , '36') ] }]"
    WinMouse.Action(selector,delayAfter=1000)

    #键盘pagedown
    WinKeyboard.Press('PageDown')

    #点tdRPA_temp目录
    selector="[  { 'wnd' : [ ('AutomationId' , 'frmMain') , ('App' , 'IvyOfdReader.exe') ] } ,  { 'wnd' : [ ('AutomationId' , 'frmPdfVx') , ('Text' , 'ofd文件转换为Pdf文件') ] } ,  { 'wnd' : [ ('Text' , '浏览文件夹') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('Text' , '请选择输出pdf文件的路径') , ('aaRole' , '10') ] } ,  { 'ctrl' : [ ('Text' , '请选择输出pdf文件的路径') ] } ,  { 'ctrl' : [ ('Text' , '桌面') , ('aaRole' , '36') ] } ,  { 'ctrl' : [ ('Text' , '此电脑') , ('aaRole' , '36') ] } ,  { 'ctrl' : [ ('Text' , '本地磁盘 (C:)') , ('aaRole' , '36') ] } ,  { 'ctrl' : [ ('Text' , '!!!tdRPA_temp') , ('aaRole' , '36') ] }]"
    WinMouse.Action(selector,delayAfter=1000)

    #点确定
    selector="[  { 'wnd' : [ ('AutomationId' , 'frmMain') , ('App' , 'IvyOfdReader.exe') ] } ,  { 'wnd' : [ ('AutomationId' , 'frmPdfVx') , ('Text' , 'ofd文件转换为Pdf文件') ] } ,  { 'wnd' : [ ('Text' , '浏览文件夹') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('Text' , '确定') ] }]"
    WinMouse.Action(selector,delayAfter=1000)

    #再点确定
    selector="[  { 'wnd' : [ ('AutomationId' , 'frmMain') , ('App' , 'IvyOfdReader.exe') ] } ,  { 'wnd' : [ ('AutomationId' , 'frmPdfVx') , ('Text' , 'ofd文件转换为Pdf文件') ] } ,  { 'wnd' : [ ('Text' , '提示') , ('aaRole' , '18') ] } ,  { 'ctrl' : [ ('Text' , '确定') ] }]"
    WinMouse.Action(selector,delayAfter=2000)

    #移动文件
    baseFile=os.path.basename(pdfFile)
    savedFile=os.path.join(r'c:\!!!tdRPA_temp',baseFile)
    shutil.move(savedFile,pdfFile)


if __name__ == '__main__':
    process()