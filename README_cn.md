## 重大更新! tdworker - 基于tdcore的命令库，强大方便，说明文档：https://www.showdoc.com.cn/tdworker

## <span style="color:red">版本1.2发布！已经集成了playwright支持Web应用自动化，此处文档稍后更新~</span>
--------------

# tdRPA

*Read this in other languages: [中文](./README_cn.md) [English](./README.md)*

<span style="color:red;font-size:18px">支持Python 3.8~3.11 with Windows x64([3.8.1除外](https://github.com/yinkaisheng/Python-UIAutomation-for-Windows))</span>

## 1. tdRPA是什么
tdRPA是面向软件开发人员的RPA SDK，开发人员可以用自己熟悉的语言和开发工具，开发新的RPA应用，或把RPA功能集成到现有系统里

## 2. 系统有三个组件
- tdSelector： 元素拾取器，可视化方式拾取UI元素，并生成元素查找表达式
- tdLocator： 元素定位器，根据tdSelector生成的元素查找表达式，定位到对应的UI元素，随后就可以随意访问调用UI元素的属性和方法
- tdBot： 执行器管理功能，包括暂停、日志查看等

## 3. tdRPA的特点
|**大多数RPA应用**   |  **tdRPA** |
| ------------ | ------------ |
|低代码平台、面向业务人员|SDK、面向专业软件开发者|
|集成开发环境、大而全|只聚焦UI自动化操作|
|不能单独打包成可执行文件分发部署|可以|
|不容易作为软件模块集成到现有应用系统里|方便|
|专有可视化设计器结合嵌入代码功能|用自己熟悉的语言和开发工具|
|代码功能、特定或有限的编程语言|Python模块，也可被其它语言调用|
|可视化编程、效率低、手忙脚乱眼昏花|代码方式、精准灵活|
|版本管理不方便|方便|
|本地部署|通过RPC方式，可远程调用，方便群控|

## 4.下载
- github [https://github.com/tdRPA/tdRPA/releases](https://github.com/tdRPA/tdRPA/releases)
- gitee [https://gitee.com/tdRPA/tdRPA/releases](https://gitee.com/tdRPA/tdRPA/releases)

## 5. 安装
- tdSelector： 无需安装解压即可
- tdLocator： `pip install tdrpa.tdcore`
- tdBot： 随tdLocator一起安装

## 6. 使用
- tdSelector： 运行`selector.exe`，元素拾取快捷键是`ctrl`取消`esc`
- tdBot： 随tdLocator自动启动，相关功能可通过任务栏托盘图标操作
- tdLocator： python 使用演示如下 [录屏](https://tdrpa.thingswell.cn/video/usage_cn.mp4)


```python
    #导入tdcore包
    from tdrpa import tdcore
    
    #获取'Desktop'根元素
    desktop=tdcore.LocatorWindows.findElement()
    #输出元素Name属性
    print(desktop._element.Name)
    
    #打开notepad.exe
    import os
    os.popen('notepad.exe')
    
    #等待1秒
    import time
    time.sleep(1)
    
    #点击'帮助'菜单栏
    helpSelector="[  { 'wnd' : [ ('Text' , '无标题 - 记事本') , ('aaRole' , '10') , ('App' , 'notepad.exe') ] } ,  { 'ctrl' : [ ('AutomationId' , 'MenuBar') , ('Text' , '应用程序') ] } ,  { 'ctrl' : [ ('Text' , '帮助(H)') , ('aaRole' , '12') ] }]"
    helpElement=tdcore.LocatorWindows.findElement(helpSelector)
    helpElement._element.Click()

    #点击'关于'菜单项
    aboutSelector="[  { 'wnd' : [ ('Text' , '无标题 - 记事本') , ('aaRole' , '10') , ('App' , 'notepad.exe') ] } ,  { 'wnd' : [ ('Text' , '帮助(H)') , ('aaRole' , '11') ] } ,  { 'ctrl' : [ ('AutomationId' , '65') , ('Text' , '关于记事本(A)') ] }]"
    aboutElement=tdcore.LocatorWindows.findElement(aboutSelector)
    aboutElement._element.Click()

    #"_element"的属性和方法，见"uiautomation" https://pypi.org/project/uiautomation/ 开源库，或使用带代码补全和智能提示的编程环境
```

## 7. 说明
- tdRPA目前是v1.1版本，只实现了windows native应用的元素操作功能，操作浏览器应用请搜索`chrome force-renderer-accessibility`，是一种把浏览器网页UI元素当做native元素操作的方式。下一步计划是对浏览器操作更好的支持，对手机应用的自动化尚未考虑
- 不论个人应用还是商业应用，全部免费，无任何限制
- 欢迎提供应用需求，用需求驱动方式逐步完善产品

## 8. 类似产品
- 商业、价格高: UiPath、Blue Prism、Automation Anywhere、Pega、微软Power Automation、来也UiBot、影刀、金智维、艺赛旗、弘玑、Cyclone弘玑
- 开源、大多没有可视化元素拾取: TagUI、Robot Framework、OpenRPA、UI.Vision、UiAutomation、Playwright

## 9. 里程碑
|**功能**   |  **状态** |
| ------------ | ------------ |
|Windows本地应用| 已完成 |
|浏览器应用| 开发中 |
|Java应用| 待定 |
|移动应用| 待定 |
|Linux应用| 待定 |

## 10. 技术问题
- [FAQ](./topic/faq_cn.md)
- [使用演示](./topic/demo_cn.md)
- [被其它语言调用](./topic/interop_cn.md)
- [远程调用、群控](./topic/rpc_cn.md)
- [关于chrome force-renderer-accessibility](./topic/chrome_cn.md)
- [相关类库、工具](./topic/toolset_cn.md)

## 11. 联系
- mail: thingswell@qq.com
- 微信: haijun-data，加好友后可进tdRPA群交流

## 12. 捐赠
[微信/支付宝](./topic/zan.md)