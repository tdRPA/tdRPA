# tdRPA

*Read this in other languages: [中文](./README_cn.md) [English](./README.md)*

<span style="color:red;font-size:18px">Support Python 3.8~3.11 with Windows x64([Except for 3.8.1](https://github.com/yinkaisheng/Python-UIAutomation-for-Windows))</span>

## 1. What is tdRPA
tdRPA is an RPA SDK for software developers. Developers can use their familiar languages and development tools to develop new RPA applications or integrate RPA functionality into existing systems

## 2. tdRPA has three components
- tdSelector: An element picker that visually picks UI elements and generates element lookup expressions
- tdLocator: Element locator, used to locate the corresponding UI element based on the element search expression generated by tdSelector. After locating the UI element, you can freely access and call its properties and methods
- tdBot: Executor management function, including pause, log viewing, etc.

## 3. tdRPA Features
|**Most RPA Suite**   |  **tdRPA** |
| ------------ | ------------ |
|Low-code platform, aimed at business users|SDK, aimed at professional software developers|
|Integrated Development Environment, all-in-one|Focus only on UI automation operations|
|Cannot be packaged as a standalone executable for distribution and deployment|Can be|
|Not easy to integrate as a software module into existing application systems|Easy|
|Proprietary visual designer combined with embedded code functionality|Use familiar programming languages and development tools|
|Code functionality, specific or limited programming languages|Python module, can also be called by other languages|
|Visual programming, low efficiency, chaotic and dizzying|Code-based, precise and flexible|
|Poor version management|Good|
|Local Deployment|Can be remotely called through RPC, convenient for group control|

## 4.Download
- github [https://github.com/tdRPA/tdRPA/releases](https://github.com/tdRPA/tdRPA/releases)
- gitee [https://gitee.com/tdRPA/tdRPA/releases](https://gitee.com/tdRPA/tdRPA/releases)

## 5. Installation
- tdSelector: No installation required, just unzip the file
- tdLocator: `pip install tdrpa.tdcore`
- tdBot: Installed together with tdLocator

## 6. Usage
- tdSelector: Run `selector.exe`, the shortcut key for element picking is `ctrl` and cancel is `esc`
- tdBot: Automatically starts with tdLocator, and its related functions can be operated through the taskbar tray icon
- tdLocator: Python usage demonstration is as follows [Video](https://tdrpa.thingswell.cn/video/usage_en.mp4)


```python
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
```

## 7. Additional idea
- tdRPA is currently in version 1.1 and only supports element operations for Windows native applications. For operating browser applications, please search for "chrome force-renderer-accessibility," which is a way to treat browser web UI elements as native elements for operation. The next plan is to provide better support for browser operations, and automation for mobile applications has not been considered yet
- Whether it is for personal or commercial use, all applications are free with no restrictions
- We welcome suggestions for application requirements and will gradually improve the product based on demand-driven approach

## 8. Similar Products
- Commercial,costly: UiPath,Blue Prism,Automation Anywhere,Pega,Microsoft Power Automation,UiBot,Cyclone
- Open Source,most without visual UI element selector: TagUI,Robot Framework,OpenRPA,UI.Vision,UiAutomation,Playwright

## 9. Milestones
|**Function**   |  **Status** |
| ------------ | ------------ |
|Windows native applications| Completed |
|Browser applications| In progress |
|Java applications| TBD |
|Mobile applications| TBD |
|Linux applications| TBD |

## 10. Technical Topics
- [FAQ](./topic/faq.md)
- [Usage demonstration](./topic/demo.md)
- [Invoked by other languages](./topic/interop.md)
- [Remote invocation, group control](./topic/rpc.md)
- [About chrome force-renderer-accessibility](./topic/chrome.md)
- [Related libraries, tools](./topic/toolset.md)

## 11. Contact
- Email: thingswell@qq.com
- WeChat: haijun-data

## 12. Support me
- [wechat/alipay](./topic/zan.md)<br><br>
- [![ko-fi](https://tdrpa.thingswell.cn/image/ko-fi.png)](https://ko-fi.com/K3K7MFO73)