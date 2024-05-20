### 属性

#### tdcore.loggers: Dict[str, logging.Logger]
当前已经存在的logger，每个logger都有不同的名字，对应不同的log文件；查看log文件，请右键单击任务栏右下角tdBot图标
![查看日志](./png/view_log.png "查看日志")



### 方法

#### tdcore.getLogger(name: str) -> logging.Logger
给定一个名字，获取对应的logger对象；

|  参数 | 说明  |
|---|---|
|  name | 如果相同名字的logger对象已经存在，会给出warning提示；建议避免和其它库用同一个logger  |


#### tdcore.hotkeyPauseHere()
热键暂停断点函数，可以在需要支持热键暂停的地方，插入此函数
```
from tdrpa.tdcore import hotkeyPauseHere

print(123)
hotkeyPauseHere()
print(456)
```


#### tdcore.hotkeyPause
热键暂停断点函数装饰器
```
from tdrpa.tdcore import hotkeyPause

@hotkeyPause
def doSomething():
    print(789)
```