#python urllib模块源码学习
----
*  所有方法:    
[urlopen](#1)  
[URLopener](#2)  
[FancyURLopener](#3)  
[urlretrieve](#4)  
[urlcleanup](#5)  
[quote](#6)  
[quote_plus](#7)  
[unquote](#8)  
[unquote_plus](#9)  
[urlencode](#10)  
[url2pathname](#11)  
[pathname2url](#12)  
[splittag](#13)  
[localhost](#14)  
[thishost](#15)  
[ftperrors](#16)   
[basejoin](#17)  
[unwrap](#18)  
[splittype](#19)   
[splithost](#20)   
[splituser](#21)   
[splitpasswd](#22)   
[splitport](#23)  
[splitnport](#24)  
[splitquery](#25)  
[splitattr](#26)   
[splitvalue](#27)   
[getproxies](#28)   
     

*  版本   
	`1.17`

----
方法详解
----

###<code id="1">urlopen():</code>     
源码：  

	_urlopener = None  
	def urlopen(url, data=None, proxies=None, context=None):
    """Create a file-like object for the specified URL to read from."""
    from warnings import warnpy3k
    warnpy3k("urllib.urlopen() has been removed in Python 3.0 in "
             "favor of urllib2.urlopen()", stacklevel=2)

    global _urlopener
    if proxies is not None or context is not None:
        opener = FancyURLopener(proxies=proxies, context=context)
    elif not _urlopener:
        opener = FancyURLopener()
        _urlopener = opener
    else:
        opener = _urlopener
    if data is None:
        return opener.open(url)
    else:
        return opener.open(url, data)

打开一个url的方法，返回一个文件对象，然后可以进行类似文件对象的操作。  
urlopen返回对象提供方法：  

- read() , readline() ,readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样
- info()：返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
- getcode()：返回Http状态码。如果是http请求，200请求成功完成;404网址未找到
- geturl()：返回请求的url

###<code id="4">urlretrieve():</code>
源码：

	def urlretrieve(url, filename=None, reporthook=None, data=None, context=None):
	    global _urlopener
	    if context is not None:
	        opener = FancyURLopener(context=context)
	    elif not _urlopener:
	        _urlopener = opener = FancyURLopener()
	    else:
	        opener = _urlopener
	    return opener.retrieve(url, filename, reporthook, data)

urlretrieve方法将url定位到的html文件下载到你本地的硬盘中。如果不指定filename，则会存为临时文件。   
urlretrieve()返回一个二元组(filename,mine_hdrs)
