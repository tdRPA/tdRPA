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
    
    f=open(r'result.txt','w',encoding='utf8')
    f.write(str(text))
    f.close()