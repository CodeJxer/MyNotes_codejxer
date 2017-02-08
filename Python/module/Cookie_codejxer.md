#python Cookie模块源码学习
----
*  所有方法(可点击函数名跳转):    

[CookieError](#1)  
[BaseCookie](#2)  
[SimpleCookie](#3)  
[SerialCookie](#4)  
[SmartCookie](#5)  
[Cookie](#6)  

###<code id="1">CookieError():</code>
源码:  

	#
	# Define an exception visible to External modules
	#
	class CookieError(Exception):
    pass


###<code id="2">BaseCookie():</code>
源码:

	# At long last, here is the cookie class.
	#   Using this class is almost just like using a dictionary.
	# See this module's docstring for example usage.
	#
	class BaseCookie(dict):
	    # A container class for a set of Morsels
	    #
	
	    def value_decode(self, val):
	        """real_value, coded_value = value_decode(STRING)
	        Called prior to setting a cookie's value from the network
	        representation.  The VALUE is the value read from HTTP
	        header.
	        Override this function to modify the behavior of cookies.
	        """
	        return val, val
	    # end value_encode
	
	    def value_encode(self, val):
	        """real_value, coded_value = value_encode(VALUE)
	        Called prior to setting a cookie's value from the dictionary
	        representation.  The VALUE is the value being assigned.
	        Override this function to modify the behavior of cookies.
	        """
	        strval = str(val)
	        return strval, strval
	    # end value_encode
	
	    def __init__(self, input=None):
	        if input: self.load(input)
	    # end __init__
	
	    def __set(self, key, real_value, coded_value):
	        """Private method for setting a cookie's value"""
	        M = self.get(key, Morsel())
	        M.set(key, real_value, coded_value)
	        dict.__setitem__(self, key, M)
	    # end __set
	
	    def __setitem__(self, key, value):
	        """Dictionary style assignment."""
	        if isinstance(value, Morsel):
	            # allow assignment of constructed Morsels (e.g. for pickling)
	            dict.__setitem__(self, key, value)
	        else:
	            rval, cval = self.value_encode(value)
	            self.__set(key, rval, cval)
	    # end __setitem__
	
	    def output(self, attrs=None, header="Set-Cookie:", sep="\015\012"):
	        """Return a string suitable for HTTP."""
	        result = []
	        items = self.items()
	        items.sort()
	        for K,V in items:
	            result.append( V.output(attrs, header) )
	        return sep.join(result)
	    # end output
	
	    __str__ = output
	
	    def __repr__(self):
	        L = []
	        items = self.items()
	        items.sort()
	        for K,V in items:
	            L.append( '%s=%s' % (K,repr(V.value) ) )
	        return '<%s: %s>' % (self.__class__.__name__, _spacejoin(L))
	
	    def js_output(self, attrs=None):
	        """Return a string suitable for JavaScript."""
	        result = []
	        items = self.items()
	        items.sort()
	        for K,V in items:
	            result.append( V.js_output(attrs) )
	        return _nulljoin(result)
	    # end js_output
	
	    def load(self, rawdata):
	        """Load cookies from a string (presumably HTTP_COOKIE) or
	        from a dictionary.  Loading cookies from a dictionary 'd'
	        is equivalent to calling:
	            map(Cookie.__setitem__, d.keys(), d.values())
	        """
	        if type(rawdata) == type(""):
	            self.__ParseString(rawdata)
	        else:
	            # self.update() wouldn't call our custom __setitem__
	            for k, v in rawdata.items():
	                self[k] = v
	        return
	    # end load()
	
	    def __ParseString(self, str, patt=_CookiePattern):
	        i = 0            # Our starting point
	        n = len(str)     # Length of string
	        M = None         # current morsel
	
	        while 0 <= i < n:
	            # Start looking for a cookie
	            match = patt.match(str, i)
	            if not match: break          # No more cookies
	
	            K,V = match.group("key"), match.group("val")
	            i = match.end(0)
	
	            # Parse the key, value in case it's metainfo
	            if K[0] == "$":
	                # We ignore attributes which pertain to the cookie
	                # mechanism as a whole.  See RFC 2109.
	                # (Does anyone care?)
	                if M:
	                    M[ K[1:] ] = V
	            elif K.lower() in Morsel._reserved:
	                if M:
	                    if V is None:
	                        if K.lower() in Morsel._flags:
	                            M[K] = True
	                    else:
	                        M[K] = _unquote(V)
	            elif V is not None:
	                rval, cval = self.value_decode(V)
	                self.__set(K, rval, cval)
	                M = self[K]
	    # end __ParseString
	# end BaseCookie class

**BaseCookie基类：** BaseCookies的行为非常像dict，可以用键/值对的形式来操作它，但是kye必须是字符串，value是Morsel对象 （下面会讲到Morsel）。   
 
- BaseCookies定义了编码/解码，输入/输出操作的公共规范：

- BaseCookie.value_encode(val)：对数据进行序列化/反序列化。这些方法都返回字符串，以便通过Http传输。

- BaseCookie.output()：返回字符串，该字符串可以作为Http响应头发往客户端。

- BaseCookie.js_output()：返回嵌入js脚本的字符串，浏览器通过执行该脚本，就可以得到cooke数据。

- BaseCookie.load(newdata)：解析字符串为Cookie数据。


**Morsel类 ：** 用于表示Cookie中每一项数据的属性而抽象的类。这些属性包括：expires, path, comment, domain, max-age, secure, version等等。

- Morsel.key，Morsel.value：Cookie数据项的key/value(value可以是二进制数据)；

- Morsel.coded_value：数据编码后得到的字符串。Http协议是基于文本的协议，Server无法直接向Client发送二进制数据，只有序列化成字符串后，才能发往Client；

- Morsel.set(key, value, coded_value)：设置Cookie数据项的key、value、coded_value；

- Morsel.isReversvedKey(key)：如果key是expires, path, comment, domain, max-age, secure, version, httponly中的一个，返回True，否则返回False；

- Morsel.output()：返回型如“Set-Cookie: …”的字符串，表示一个Cookie数据项；

- Morsel.js_output()：返回Cookie数据项的脚本字符串；

- Morsel.OutputString(): 返回Morsel的字符串表示；

###<code id="3">SimpleCookie():</code>
源码:
	
	class SimpleCookie(BaseCookie):
	    """SimpleCookie
	    SimpleCookie supports strings as cookie values.  When setting
	    the value using the dictionary assignment notation, SimpleCookie
	    calls the builtin str() to convert the value to a string.  Values
	    received from HTTP are kept as strings.
	    """
	    def value_decode(self, val):
	        return _unquote( val ), val
	    def value_encode(self, val):
	        strval = str(val)
	        return strval, _quote( strval )
	# end SimpleCookie

 **SimpleCookie**继承自BaseCookie，对 BaseCookie的value_decode, value_encode进行了重写并实现自己的序列化/反序列化策略:**SimpleCookie内部使用str()来对数据进行序列化；**

###<code id="4">SerialCookie():</code>
源码:

	class SerialCookie(BaseCookie):
	    """SerialCookie
	    SerialCookie supports arbitrary objects as cookie values. All
	    values are serialized (using cPickle) before being sent to the
	    client.  All incoming values are assumed to be valid Pickle
	    representations.  IF AN INCOMING VALUE IS NOT IN A VALID PICKLE
	    FORMAT, THEN AN EXCEPTION WILL BE RAISED.
	
	    Note: Large cookie values add overhead because they must be
	    retransmitted on every HTTP transaction.
	
	    Note: HTTP has a 2k limit on the size of a cookie.  This class
	    does not check for this limit, so be careful!!!
	    """
	    def __init__(self, input=None):
	        warnings.warn("SerialCookie class is insecure; do not use it",
	                      DeprecationWarning)
	        BaseCookie.__init__(self, input)
	    # end __init__
	    def value_decode(self, val):
	        # This could raise an exception!
	        return loads( _unquote(val) ), val
	    def value_encode(self, val):
	        return val, _quote( dumps(val) )
	# end SerialCookie


###<code id="5">SmartCookie():</code>
源码:



###<code id="6">Cookie():</code>
源码:



