# tdRPA

[Chinese](./README.md)
[English](./README_en.md)

## 1. tdRPA是什么
tdRPA是面向软件开发人员的RPA SDK，开发人员可以用自己熟悉的语言和开发工具，开发新的RPA应用，或把RPA功能集成到现有系统里

## 2. 系统有三个组件
- tdSelector： 元素拾取器，可视化方式拾取UI元素，并生成元素查找表达式
- tdBot： 元素操作执行器，根据tdSelector生成的元素查找表达式，对UI元素进行相应的操作，相关功能以restful API的方式提供
- tdSDK： tdBot的restful API以SDK的方式提供给不同的开发者，支持Java、Python、C#、Nodejs、Javascript等各种语言

## 3. tdRPA的特点
|****大多数RPA应用****   |  ****tdRPA**** |
| ------------ | ------------ |
|低代码平台、面向业务人员|SDK、面向专业软件开发者|
|不能单独打包成可执行文件分发部署|可以|
|不容易作为软件模块集成到现有应用系统里|方便|
|专有可视化设计器结合嵌入代码功能|用自己熟悉的语言和开发工具|
|代码功能、特定或有限的编程语言|大多数语言、基于[swagger-codegen](https://github.com/swagger-api/swagger-codegen "swagger-codegen")|
|可视化操作、效率低、手忙脚乱眼昏花|代码方式、精准灵活|
|版本管理不方便|方便|
|本机应用|机器人通过restful API方式调用，可远程控制，方便群控|

## 4. 安装
- tdSelector： 无需安装解压即可
- tdBot： 无需安装解压即可
- tdSDK： 目前只提供了python SDK，在命令行下进入`setup.py`所在目录，运行 `python setup.py install`

## 5. 使用
- tdSelector： 运行`selector.exe`，元素拾取快捷键是`ctrl`
- tdBot： 运行`tdbot.exe`，执行器restful API默认地址`127.0.0.1:8864`，可通过命令行方式启动修改，参数格式为 `tdbot.exe [ip] [port]`
- tdSDK： python SDK使用演示如下，其它语言类似


```python
    #导入tdbot包
    import tdbot
    
    #设置调用的restful API，执行器运行地址
    config=tdbot.Configuration()
    config.host='http://127.0.0.1:8864'
    
    #创建客户端
    client=tdbot.ApiClient(config)
    
    #创建鼠标api对象
    mouseApi=tdbot.MouseApi(client)
    #创建目标对象，selector字符串从tdSelector元素抓取copy按钮来
    target=tdbot.Target(selector="[  { 'wnd' : [ ('Text' , 'tdbot') , ('aaRole' , '10') , ('App' , 'explorer.exe') ] } ,  { 'ctrl' : [ ('Text' , 'UIRibbonDockTop') , ('aaRole' , '10') ] } ,  { 'ctrl' : [ ('Text' , 'Ribbon') , ('aaRole' , '10') ] } ,  { 'ctrl' : [ ('Text' , 'Ribbon') , ('aaRole' , '10') ] } ,  { 'ctrl' : [ ('aaRole' , '10') ] } ,  { 'ctrl' : [ ('Text' , 'Ribbon') , ('aaRole' , '38') ] } ,  { 'ctrl' : [ ('Text' , '下层功能区') , ('aaRole' , '16') ] } ,  { 'ctrl' : [ ('aaRole' , '10') ] } ,  { 'ctrl' : [ ('Text' , '主页') , ('aaRole' , '38') ] } ,  { 'ctrl' : [ ('Text' , '新建') , ('aaRole' , '22') ] } ,  { 'ctrl' : [ ('Text' , '新建文件夹') , ('aaRole' , '43') ] }]")
    #调用鼠标点击命令
    mouseApi.mouse_click_target(body=target)
    {'id': '8a8fe04c-0461-11ee-9cad-9cc6b1b7ea87'}
```

## 6. 说明
- tdRPA目前是v1.0beta版本，主要实现了selector元素表达式的生成和解析查找功能，UI元素的操作只实现了两个鼠标操作(点击、悬停)，后续会陆续把其它操作加上，欢迎提供应用需求，用需求驱动方式完善UI元素操作功能
- tdRPA目前只实现了windows native应用的元素操作功能，操作浏览器应用请搜索`chrome force-renderer-accessibility`，是一种把浏览器网页UI元素当做native元素操作的方式。下一步计划是对浏览器操作更好的支持，对手机应用的自动化尚未考虑
- 初步计划是对个人应用免费，商业应用少量收费的模式；当然如果捐助和赞赏方式能够支持开发工作继续下去，将全免费

## 7. 联系
- mail: thingswell@qq.com
- 微信: haijun-data