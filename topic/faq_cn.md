### FAQ

#### 1. tdSelector里Windows Native UI元素的aaRole和aaState属性什么意思？
这是早期Windows UI自动化技术MSAA(Microsoft Active Accessibility)的两个属性:aaRole代表元素类型，aaState代表元素状态。在实际使用中，基本不用修改这两个值，只选中或不选中，作为元素查找条件使用。更多信息见MSAA文档和uiautomation开源库

#### 2. 如何双击Windows Native UI元素？
```python
    aboutElement=tdcore.LocatorWindows.findElement(aboutSelector)
    aboutElement._element.DoubleClick()
```
"_element"的属性和方法，见uiautomation开源库，或使用带代码补全和智能提示的编程环境

#### 3. 如何获取Chrome浏览器地址栏内容？
```python
    addressElement=tdcore.LocatorWindows.findElement(addressSelector)
    valuePattern=addressElement._element.GetValuePattern()
	address=valuePattern.Value
	address
	'https://github.com/tdRPA/tdRPA'
```
不同的UI元素类型具有不同的属性和方法，具体用法见UI Automation Control Patterns文档和uiautomation开源库