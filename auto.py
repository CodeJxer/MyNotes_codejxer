# -*- coding=UTF-8 -*-

rawtext = '''"urlopen", "URLopener", "FancyURLopener", "urlretrieve",
           "urlcleanup", "quote", "quote_plus", "unquote", "unquote_plus",
           "urlencode", "url2pathname", "pathname2url", "splittag",
           "localhost", "thishost", "ftperrors", "basejoin", "unwrap",
           "splittype", "splithost", "splituser", "splitpasswd", "splitport",
           "splitnport", "splitquery", "splitattr", "splitvalue",
           "getproxies"'''											#文本
text = ''.join(rawtext.split()).split(',')							#去掉字符串中的所有空格和换行符并以逗号分隔
func_name = [strr.split('"')[1] for strr in text]					#去掉双引号：函数名
func_name_pane =  ['[' + strr + ']' for strr in func_name]			#函数名就上方括号
func_pane_number = [func_name_pane[i] + '(#' + str(i + 1) + ')' for i in range(0, len(func_name))]#函数名加上方括号加上编号

func_id = ['###<code id="' + str(i + 1) + '">' + func_name[i] + u'():</code>\n源码:\n\n\n' for i in range(0, len(func_name))]#函数名加上id号

for strr in func_pane_number:
	print strr

for strr in func_id:
	print strr