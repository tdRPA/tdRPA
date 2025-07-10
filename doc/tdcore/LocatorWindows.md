# LocatorWindows
Windows元素定位



### 属性

#### timeout: int = None
查找元素超时设置，单位秒；默认值None，表示永不超时



### 方法

#### findElement(selectorString:str=None, fromElement:uiautomation.Control=None, timeout:int=None) -> Union[uiautomation.Control,None]
查找元素；当selectorString和fromElement都为None时，返回desktop根元素

|  参数 | 说明  |
|---|---|
|  selectorString | 元素查找表达式，由tdSelector元素拾取器生成  |
|  fromElement | 查找起始元素；默认值为None，表示从根元素即desktop元素开始查找  |
|  timeout | 超时秒数；默认值为None，表示用LocatorWindows模块变量timeout值作为本次查找的超时值  |
