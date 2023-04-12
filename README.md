# tdRPA

[Chinese](./README.md)
[English](./README_en.md)


大多数RPA应用不能单独打包成可执行文件分发部署，也不容易作为软件模块集成到现有应用系统里。

tdRPA是面向软件开发人员的RPA SDK，开发人员可以用自己熟悉的语言和开发工具，开发新的RPA应用，或把RPA功能集成到现有系统里。

系统有三个组件
- Selector: 元素拾取器，可视化方式拾取UI元素，并生成元素查找表达式
- Bot： 元素操作执行器，根据Selector生成的元素查找表达式，对UI元素进行相应的操作，相关功能以restful API的方式提供
- SDK： Bot的restful API 以SDK的方式提供给不同的开发者，支持Java、Python、C#、Nodejs、Javascript等各种语言
