#Python网络爬虫与信息提取
-----
##requests库的get()方法

`r = requests.get()`   
其中`requests.get()`是构造一个向服务器请求资源的Request对象     
其中`r`是一个包含服务器资源的Response对象

	# -*- coding=UTF-8 -*-
	# 2017年2月28日17:40:30
	
	import requests
	url = 'http://www.baidu.com'
	r = requests.get(url)
	print type(r)				#打印r的类型
	print r.status_code			#打印http请求返回的状态码
	print r.headers				#打印响应头

运行结果：     

	<class 'requests.models.Response'>
	200
	{'Content-Encoding': 'gzip', 'Transfer-Encoding': 'chunked', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Server': 'bfe/1.0.8.18', 'Last-Modified': 'Mon, 23 Jan 2017 13:28:26 GMT', 'Connection': 'Keep-Alive', 'Pragma': 'no-cache', 'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Date': 'Tue, 28 Feb 2017 09:39:57 GMT', 'Content-Type': 'text/html'}
	
**Response对象的属性**

|属性|说明|
|----------------|
|r.status_code|HTTP请求返回的状态，200表示连接成功，404表示失败|
|r.text|HTTP响应内容的字符串形式。即URL对应的页面内容|
|r.encoding|从HTTP header中猜测的响应内容编码方式|
|r.apparent_encoding|从内容中分析出的相应内容编码方式(备选编码方式)|
|r.content|HTTP响应内容的二进制形式|

一般认为r.apparent_encoding比r.encoding准确

	# -*- coding=UTF-8 -*-
	# 2017-2-28 20:04:57
	
	import requests
	url = 'http://www.baidu.com'
	r = requests.get(url)
	print r.encoding			#输出encoding的格式
	r.encoding = r.apparent_encoding	#转换r.text的编码格式
	print r.text 				#输出返回的页面源码
运行结果：

	ISO-8859-1
	<!DOCTYPE html>
	<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>百度一下，你就知道</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=百度一下 class="bg s_btn"></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>新闻</a> <a href=http://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>地图</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>视频</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>贴吧</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>登录</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">登录</a>');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">更多产品</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>关于百度</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>使用百度前必读</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>意见反馈</a>&nbsp;京ICP证030173号&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>

##爬取网页的通用代码框架
**Requests库的异常：**

|异常|说明|
|----|---|
|requests.ConnectionError|网络连接错误异常，如DNS查询失败、拒绝连接等|
|requesrs.HTTPError|HTTP错误异常|
|requests.URLRequired|URL缺失异常|
|requests.TooManyRedirects|超过最大重定向次数，产生重定向异常|
|requests.ConnectTimeout|连接远程服务器超时异常|
|requests.Timeout|请求URL超时，产生超时异常|

`r.raise_for_status`:如果不是返回状态码不是200，产生异常requests.HTTPError   

	# -*- coding=UTF-8 -*-
	# 2017-2-28 21:01:51
	
	import requests
	def GetHTMLText(url):
		try:
			r = requests.get(url)					#发送HTTP请求
			r.raise_for_status						#抛出异常
			r.encoding = r.apparent_encoding		#改变编码方式
			return r.text							#返回网页内容
		except:
			return '代码异常'
	
	if __name__ == '__main__':
		url = 'http://www.baidu.com'
		print GetHTMLText(url)

##HTTP协议及Requests库方法
**Requests库的7个主要方法**    

|方法|说明|
|----|----|
|requests.request()|构造一个请求，是支撑以下各方法的基础方法|
|requests.get()|获取HTML网页的主要方法，对应于HTTP的GET|
|requests.head()|获取HTML网页头信息的方法，对应与HTTP的HEAD|
|requests.post()|向HTML网页提交POST请求的方法，对应于HTTP的POST|
|requests.put()|向HTML网页提交PUT请求的方法，对应于HTTP的PUT|
|requests.patch()|向HEML网页提交局部修改请求，对应于HTTP的PATCH|
|requests.delete()|向HTML页面提交删除请求，对应于HTTP的DELETE|

**HTTP协议简介**  
URL格式：http://host[:port][path]  
host:合法的Internet主机域名或IP地址  
port:端口号，缺省端口为80  
path:请求资源的路径  

HTTP URL的理解：  
URL是通过HTTP协议存取资源的Internet路径，一个URL对应一个数据资源  

*HTTP协议对资源的操作*  

|方法|说明|
|---|----|
|GET|请求获取URL位置的资源|
|HEAD|请求获取URL位置资源的响应消息报告，即获得该资源的头部信息|
|POST|请求向URL位置的资源后附加新的数据|
|PUT|请求向URL位置存储一个资源，覆盖原URL位置的资源|
|PATCH|请求局部更新URL位置的资源，即改变该出资源的部分内容|
|DELETE|请求删除URL位置存储的资源|

requests库的head()方法

	# -*- coding=UTF-8 -*-
	# 2017-2-28 21:39:41
	
	import requests
	url = 'http://www.baidu.com'
	r = requests.head(url)				#requests库的head()方法
	print r.headers						#打印获取的头部信息
运行结果    

	{'Content-Encoding': 'gzip', 'Server': 'bfe/1.0.8.18', 'Last-Modified': 'Mon, 13 Jun 2016 02:50:34 GMT', 'Connection': 'Keep-Alive', 'Pragma': 'no-cache', 'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Date': 'Tue, 28 Feb 2017 13:38:58 GMT', 'Content-Type': 'text/html'}

requests库的post()方法
	
	# -*- coding=UTF-8 -*-
	# 2017-2-28 21:44:35
	
	import requests
	url = 'http://httpbin.org/post'
	payload = {'key1': 'value1', 'key2': 'value2'}
	r = requests.post(url, data = payload)			#requests库的post()方法
	print r.text									#打印文件内容

运行结果

	{
	  "args": {},
	  "data": "",
	  "files": {},
	  "form": {
	    "key1": "value1",
	    "key2": "value2"
	  },
	  "headers": {
	    "Accept": "*/*",
	    "Accept-Encoding": "gzip, deflate",
	    "Content-Length": "23",
	    "Content-Type": "application/x-www-form-urlencoded",
	    "Host": "httpbin.org",
	    "User-Agent": "python-requests/2.13.0"
	  },
	  "json": null,
	  "origin": "27.18.150.95",
	  "url": "http://httpbin.org/post"
	}

新增了

	  "form": {
	    "key1": "value1",
	    "key2": "value2"
	  },

##Requests库主要方法解析
**Requests库的7个主要方法**    

|方法|说明|
|----|----|
|requests.request()|构造一个请求，是支撑以下各方法的基础方法|
|requests.get()|获取HTML网页的主要方法，对应于HTTP的GET|
|requests.head()|获取HTML网页头信息的方法，对应与HTTP的HEAD|
|requests.post()|向HTML网页提交POST请求的方法，对应于HTTP的POST|
|requests.put()|向HTML网页提交PUT请求的方法，对应于HTTP的PUT|
|requests.patch()|向HEML网页提交局部修改请求，对应于HTTP的PATCH|
|requests.delete()|向HTML页面提交删除请求，对应于HTTP的DELETE|

- requests.request(method, url, **kwars)
	- method:请求方式，对应get/put/post等七种
		- r.requests.request('GET', url, **kmargs)
		- r.requests.request('HEAD', url, **kmargs)
		- r.requests.request('POST', url, **kmargs)
		- r.requests.request('PUT', url, **kmargs)
		- r.requests.request('PATCH', url, **kmargs)
		- r.requests.request('delete', url, **kmargs)
		- r.requests.request('OPTIONS', url, **kmargs)
	- url:拟获取页面的URL链接
	- **kwargs:控制访问的参数，共13个
		- params:字典或字节序列，作为参数增加到url中   
		
				# -*- coding=UTF-8 -*-
				# 2017-2-28 21:56:50
				
				import requests
				url = 'http://httpbin.org/post'
				payload = {'key1': 'value1', 'key2': 'value2'}
				r = requests.request('GET', url, params = payload)		#request方法的params参数
				print r.url												#打印url
			
			运行结果  

				http://httpbin.org/post?key2=value2&key1=value1
		- data:字典、字节序列或文件对象，作为Requests的内容

				# -*- coding=UTF-8 -*-
				# 2017-2-28 22:06:00
				
				import requests
				url = 'http://httpbin.org/post'
				kv = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
				r = requests.request('POST', url, data = kv)		#request方法的data参数
				print r.text										#输出对应资源
		运行结果

				{
				  "args": {},
				  "data": "",
				  "files": {},
				  "form": {
				    "key1": "value1",
				    "key2": "value2",
				    "key3": "value3"
				  },
				  "headers": {
				    "Accept": "*/*",
				    "Accept-Encoding": "gzip, deflate",
				    "Content-Length": "35",
				    "Content-Type": "application/x-www-form-urlencoded",
				    "Host": "httpbin.org",
				    "User-Agent": "python-requests/2.13.0"
				  },
				  "json": null,
				  "origin": "27.18.150.95",
				  "url": "http://httpbin.org/post"
				}
			
		- json：JSON格式的数据，作为Request的内容

				# -*- coding=UTF-8 -*-
				# 2017-2-28 22:08:57
				
				import requests
				url = 'http://httpbin.org/post'
				kv = {'key1': 'value1'}
				r = requests.request('POST', url, json = kv)		#request方法的json参数
				print r.text										#输出对应资源
			运行结果

				{
				  "args": {},
				  "data": "{\"key1\": \"value1\"}",
				  "files": {},
				  "form": {},
				  "headers": {
				    "Accept": "*/*",
				    "Accept-Encoding": "gzip, deflate",
				    "Content-Length": "18",
				    "Content-Type": "application/json",
				    "Host": "httpbin.org",
				    "User-Agent": "python-requests/2.13.0"
				  },
				  "json": {
				    "key1": "value1"
				  },
				  "origin": "27.18.150.95",
				  "url": "http://httpbin.org/post"
				}

		- header：字典，HTTP定制头
		
				# -*- coding=UTF-8 -*-
				# 2017-2-28 22:13:23
				
				import requests
				url = 'http://httpbin.org/post'
				hd = {'user-agent': 'Chrome/10'}
				r = requests.request('POST', url, headers = hd)		#request方法的header参数
				print r.headers										#输出对应资源

			运行结果

				{'Content-Length': '316', 'Server': 'nginx', 'Connection': 'keep-alive', 'Access-Control-Allow-Credentials': 'true', 'Date': 'Tue, 28 Feb 2017 14:11:55 GMT', 'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json'}

		- cookies:字典或CookieJar,Request中的cookie
		- auth:元组，支持HTTP认证功能
		- files:字典类型，传输文件
	
				# -*- coding=UTF-8 -*-
				# 2017-2-28 22:51:51
				
				import requests
				url = 'http://httpbin.org/post'
				fs = {'files': open('stdin.txt', 'rb')}
				r = requests.request('POST', url, files = fs)		#request方法的files参数
				r.encoding = r.apparent_encoding
				print r.text										#输出对应资源

			运行结果

				{
				  "args": {},
				  "data": "",
				  "files": {
				    "files": "just some test\r\nanother"
				  },
				  "form": {},
				  "headers": {
				    "Accept": "*/*",
				    "Accept-Encoding": "gzip, deflate",
				    "Content-Length": "169",
				    "Content-Type": "multipart/form-data; boundary=76d625c06e9245209af4d8a44efd9210",
				    "Host": "httpbin.org",
				    "User-Agent": "python-requests/2.13.0"
				  },
				  "json": null,
				  "origin": "27.18.150.95",
				  "url": "http://httpbin.org/post"
				}
		- timeout: 设定超时时间，秒为单位

				r = requests.request('GET', url, timeout = 10)
		- proxies:字典类型，设定访问代理服务器，可以增加登录认证

				pxs = {'http': 'http://user:pass@10.10.10.1:1234',
					   'https': 'https://10.10.10.1:4321'}
				r = requests.request('GET', 'http://www.baidu.com', proxies=pxs)

		- allow_redirects: True/False，默认为True，重定向开关
		- stream:True/False, 默认为True，获取内容立即下载开关
		- verify:True/False, 默认为True，认证SSL证书开关
		- cert:本地SSL证书路径
- requests.get(url, params=None, **kwargs)
	- url:拟获取页面的URL
	- params:url中的额外参数，字典或字节流格式，可选
	- **kwargs：12个控制访问的参数(除了params)
	
- requests.head(url, **kwargs)
	- url:拟获取页面的URL
	- **kwargs：13个控制访问的参数

- requests.post(url, data=None, json=None, **kwargs)
	- url:拟获取页面的URL
	- data:字典、字节序列或文件，Request的内容
	- json：JSON格式的数据，Request的内容
	- **kwargs：11个控制访问的参数

- requests.put(url, data=None, **kwargs)
	- url:拟获取页面的URL
	- data:字典、字节序列或文件，Request的内容
	- **kwargs：12个控制访问的参数

- requests.patch(url, data=None, **kwargs)
	- url:拟获取页面的URL
	- data:字典、字节序列或文件，Request的内容
	- **kwargs：12个控制访问的参数

- requests.delete(url, **kwargs)
	- url:拟获取页面的URL
	- **kwargs：13个控制访问的参数

##Robots协议
作用：网站告知网络爬虫哪些页面可以抓取，哪些不行    
形式：在网站根目录下的robots.txt文件

##Requests库的网络爬虫实战

###实例1：京东商品页面的爬取

	# -*- coding=UTF-8 -*-
	# 2017-3-1 10:33:03
	
	import requests
	
	def getHTML(url):
		try:
			r = requests.get(url)				#发送HTML请求
			r.raise_for_status()				#抛出异常
			r.encoding = r.apparent_encoding	#改变编码
			return r.text[:1000]				#返回前1000个字符
		except:
			return '程序异常'					
	
	if __name__ == '__main__':					#执行脚本
		url = 'https://item.jd.com/2967929.html'
		print getHTML(url)

运行结果

	<!DOCTYPE HTML>
	<html lang="zh-CN">
	<head>
	    <meta http-equiv="Content-Type" content="text/html; charset=gbk" />
	    <title>【华为荣耀8】荣耀8 4GB+64GB 全网通4G手机 魅海蓝【行情 报价 价格 评测】-京东</title>
	    <meta name="keywords" content="HUAWEI荣耀8,华为荣耀8,华为荣耀8报价,HUAWEI荣耀8报价"/>
	    <meta name="description" content="【华为荣耀8】京东JD.COM提供华为荣耀8正品行货，全国价格最低，并包括HUAWEI荣耀8网购 指南，以及华为荣耀8图片、荣耀8参数、荣耀8评论、荣耀8心得、荣耀8技巧等信息，网购华为荣耀8上京东,放心又轻松" />
	    <meta name="format-detection" content="telephone=no">
	    <meta http-equiv="mobile-agent" content="format=xhtml; url=//item.m.jd.com/product/2967929.html">
	    <meta http-equiv="mobile-agent" content="format=html5; url=//item.m.jd.com/product/2967929.html">
	    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
	    <link rel="canonical" href="//item.jd.com/2967929.html"/>
	        <link rel="dns-prefetch" href="//misc.360buyimg.com"/>
	    <link rel="dns-prefetch" href="//static.360buyimg.com"/>
	    <link rel="dns-prefetch" href="//img10.360buyimg.com"/>
	    <link rel="dns-prefetch" hr

###实例2：亚马逊商品页面的爬取
