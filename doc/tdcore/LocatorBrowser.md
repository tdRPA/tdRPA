# LocatorBrowser
Browser元素定位



### 变量

#### timeout: int = None
查找元素超时设置，单位秒；默认值None，表示永不超时



### 方法

#### findElement(selectorString:str, fromElement:Union[playwright.sync_api._generated.Page,playwright.sync_api._generated.ElementHandle], timeout:int=None) -> Union[playwright.sync_api._generated.ElementHandle,None]
查找元素

|  参数 | 说明  |
|---|---|
|  selectorString | 元素查找表达式，由tdSelector元素拾取器生成  |
|  fromElement | 查找起始元素  |
|  timeout | 超时秒数；默认值为None，表示用LocatorBrowser模块变量timeout值作为本次查找的超时值  |
