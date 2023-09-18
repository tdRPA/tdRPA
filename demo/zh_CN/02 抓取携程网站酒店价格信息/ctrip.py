'''
***** tdrpa.tdcore结合 --force-renderer-accessibility 参数，抓取携程网酒店价格数据*****
1. 启用chrome的accessibility功能，有两种方式
  1) 关闭所有的chrome窗口，并查看任务管理器，确保没有遗留的chrome进程，在命令行运行 "C:\Program Files\Google\Chrome\Application\chrome.exe" --force-renderer-accessibility
  2. 或者在chrome地址栏输入 chrome://accessibility/ 把"Accessibility modes:"下面的选择框都选中
2. 在chrome中用自己的账号登录携程网 https://ctrip.com/
3. 找到一家酒店的页面，比如 https://hotels.ctrip.com/hotels/detail/?hotelId=425206
4. 等待几秒，等酒店页面的房型和价格信息加载完毕
5. 确认酒店页面是chrome的当前页面
6. 确认python环境已成功安装tdrpa.tdcore库
7. 用python执行此文件，命令行输出房型数目，并把详细信息保存到当前文件夹result.txt
'''
from tdrpa import tdcore


def getText(element):
	text=[element.Name,[]]
	for item in element.GetChildren():
		text[1].append(getText(item))
	return text



if __name__ == '__main__':
    locator=tdcore.LocatorWindows
    selector="[  { 'wnd' : [ ('aaRole' , '16') , ('App' , 'chrome.exe') ] } ,  { 'ctrl' : [ ('aaRole' , '15') ] } ,  { 'ctrl' : [ ('aaRole' , '20') ] } ,  { 'ctrl' : [ ('aaRole' , '20') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '20') ] , 'index' : '1' } ,  { 'ctrl' : [ ('aaRole' , '20') ] } ,  { 'ctrl' : [ ('aaRole' , '20') ] , 'index' : '3' } ,  { 'ctrl' : [ ('aaRole' , '20') ] , 'index' : '1' }]"
    rooms=locator.findElement(selector)
    text=getText(rooms._element)
    print(len(text[1]))
    
    f=open(r'result.txt','w',encoding='utf8')
    f.write(str(text))
    f.close()