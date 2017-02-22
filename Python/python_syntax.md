#python_syntax
----
目录:   
[输入输出](#1)   
[数据类型](#2)

##<code id="1">输入输出</code>
- 输入   `row_input()`   
参数可以传入提示字符：**eg：row_input('please input your name:')**
运行此语句，python解释器就会输出提示字符：please input your name：       

- 输出 `print`  
1.`print`加上字符串就可以输出指定的文字**eg：print 'my name is code_j_xer'**  
2.`print`语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出。`print`会依次打印每个字符串，遇到逗号“,”会输出一个空格  
3.print也可以打印整数，或者计算结果：`print 300`  `print 100 + 200`   
4.如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''     
#############
	print '''line1          
	line2    
	line3'''
##<code id="2">数据类型</code>
- 整数
- 浮点数
- 字符串  
字符串是以 '' 或" " 括起来的任意文本，比如'abc'，"xyz"等等
如果字符串内部既包含'又包含"可以用转义字符\来标识，比如：
```
'I\'m \"OK\"!'
```  
	- 转义字符    
		- 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\   
		- **如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义**
	```
	print r'\\\t\\'
	```
	就是`\\\t\\`
- 布尔值   
	- 布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，可以直接用True、False表示布尔值（请注意大小写）   
	- 布尔值可以用and、or和not运算
- 空值	
空值是Python里一个特殊的值，用None表示。
- 变量
- 常量