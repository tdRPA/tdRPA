### 属性

#### tdcore.loggers: Dict[str, logging.Logger]
logger字典，每个logger都对应不同的log文件；查看log文件，请右键单击任务栏右下角tdBot图标
![查看日志](https://gitee.com/tdRPA/tdRPA/raw/master/doc/tdcore/img/view_log.png)



### 方法

#### tdcore.getLogger(name:str, subFolder:str=None, backupCount:int=365) -> logging.Logger
获取logger对象

|  参数 | 说明  |
|---|---|
|  name | logger名字  |
|  subFolder | log文件存放的子文件夹，默认存放在根目录下,根目录位于: os.path.join(os.getenv('LOCALAPPDATA'),'tdRPA','log')  |
|  backupCount | logger每天备份一个文件，backupCount指定要保留的备份文件个数  |


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