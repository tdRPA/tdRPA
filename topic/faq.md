### FAQ

#### 1. What do the aaRole and aaState properties of Windows Native UI elements mean in tdSelector?
These are two properties of the early Windows UI automation technology MSAA (Microsoft Active Accessibility): aaRole represents the element type, and aaState represents the element state. In actual usage, these two values are rarely modified. They are used as element search conditions by selecting or deselecting them. For more information, please refer to the MSAA documentation and the "uiautomation" open-source library.

#### 2. How to double-click a Windows Native UI element?
```python
    aboutElement=tdcore.LocatorWindows.findElement(aboutSelector)
    aboutElement._element.DoubleClick()
```
The properties and methods of "_element" can be found in the "uiautomation" open-source library or by using a programming environment with code completion and intelligent suggestions. 

#### 3. How to get the link of Chrome browser address bar?
```python
    addressElement=tdcore.LocatorWindows.findElement(addressSelector)
    valuePattern=addressElement._element.GetValuePattern()
	address=valuePattern.Value
	address
	'https://github.com/tdRPA/tdRPA'
```
Different UI element types have different properties and methods. For specific usage, please refer to the "UI Automation Control Patterns" documentation and the "uiautomation" open-source library.