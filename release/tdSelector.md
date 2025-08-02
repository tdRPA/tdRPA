### 1.2.7
- 修复元素选择红框bug

### 1.2.6
- Windows元素aaState属性调整为位掩码编码(bitmask encoding)，支持模糊/正则匹配

### 1.2.5
- Windows元素aaRole属性由id改成name

### 1.2.4
- Web元素默认顶层body节点不选中
- 解决打开拾取器后导致浏览器打开新tab加载页面卡住的问题

### 1.2.3
- 仅最顶层节点具有 App 属性
- 中间层的独生子节点默认不选中
- 若 AutomationId 属性值为纯数字，默认不选中
- Web元素增加visibility属性，实现为checkVisibility()无参数