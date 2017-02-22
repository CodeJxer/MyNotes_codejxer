#http请求头
----
目录：    
- [请求方法](#1)         
- [状态码](#2) 
- [通用](#3)   
- [通用头域](#4)   
- [请求头(Requests Headers)](#5)   
- [响应头(Response)](#6)   

##<code id="1">请求方法</code>

请求方法有以下这些，常用的是GET,POST  

- GET：向指定的资源发出“显示”请求。使用GET方法应该只用在读取数据，而不应当被用于产生“副作用”的操作中，例如在Web Application中。其中一个原因是GET可能会被网络蜘蛛等随意访问。参见安全方法
- POST：向指定资源提交数据，请求服务器进行处理（例如提交表单或者上传文件）。数据被包含在请求本文中。这个请求可能会创建新的资源或修改现有资源，或二者皆有。
- OPTIONS：这个方法可使服务器传回该资源所支持的所有HTTP请求方法。用'*'来代替资源名称，向Web服务器发送OPTIONS请求，可以测试服务器功能是否正常运作。
- HEAD：与GET方法一样，都是向服务器发出指定资源的请求。只不过服务器将不传回资源的本文部分。它的好处在于，使用这个方法可以在不必传输全部内容的情况下，就可以获取其中“关于该资源的信息”（元信息或称元数据）。
- PUT：向指定资源位置上传其最新内容。
- DELETE：请求服务器删除Request-URI所标识的资源。
- TRACE：回显服务器收到的请求，主要用于测试或诊断。
- CONNECT：HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。通常用于SSL加密服务器的链接（经由非加密的HTTP代理服务器）。

##<code id="2">状态码</code>
>所有HTTP响应的第一行都是状态行，依次是当前HTTP版本号，3位数字组成的状态代码，以及描述状态 >的短语，彼此由空格分隔。 状态代码的第一个数字代表当前响应的类型：

- 1xx消息——请求已被服务器接收，继续处理
- 2xx成功——请求已成功被服务器接收、理解、并接受
- 3xx重定向——需要后续操作才能完成这一请求
- 4xx请求错误——请求含有词法错误或者无法被执行
- 5xx服务器错误——服务器在处理某个正确请求时发生错误

常见状态代码、状态描述、说明：  

- 200 OK //请求成功  
- 400 Bad Request //客户端请求有语法错误，不能被服务器所理解  
- 401 Unauthorized //请求未经授权，这个状态代码必须和WWW-Authenticate报头域一起使用  
- 403 Forbidden //服务器收到请求，但是拒绝提供服务    
- 404 Not Found //请求资源不存在，eg：输入了错误的URL  
- 500 Internal Server Error //服务器发生不可预期的错误
- 503 Server Unavailable //服务器当前不能处理客户端的请求，一段时间后可能恢复正常

##<code id="3">通用</code>
- `Request URL:https://zhuanlan.zhihu.com/p/25296437`    
请求网址：这个对应HTTP协议中的统一资源定位符也就是我们打开的网址

- `Request Method:GET`     
请求方法：这个对应HTTP协议中的请求方法

- `Status Code:200 OK`    
状态码：这个对应HTTP协议中的状态码

##<code id="4">通用头域</code>
通用头域包含请求和响应消息都支持的头域，通用头域包含Cache-Control、 Connection、Date、Pragma、Transfer-Encoding、Upgrade、Via。对通用头域的扩展要求通讯双方都支持此扩展，如果存在不支持的通用头域，一般将会作为实体头域处理。下面简单介绍几个在UPnP消息中使用的通用头域。

- `Cache-Control头域 `   
	Cache- Control指定请求和响应遵循的缓存机制。在请求消息或响应消息中设置 Cache-Control并不会修改另一个消息处理过程中的缓存处理过程。请求时的缓存指令包括no-cache、no-store、max-age、 max-stale、min-fresh、only-if-cached，响应消息中的指令包括public、private、no-cache、no- store、no-transform、must-revalidate、proxy-revalidate、max-age。各个消息中的指令含义如下：
	- Public指示响应可被任何缓存区缓存。 
	- Private指示对于单个用户的整个或部分响应消息，不能被共享缓存处理。这允许服务器仅仅描述当用户的部分响应消息，此响应消息对于其他用户的请求无效。 
	- no-cache指示请求或响应消息不能缓存 
	- no-store用于防止重要的信息被无意的发布。在请求消息中发送将使得请求和响应消息都不使用缓存。 
	- max-age指示客户机可以接收生存期不大于指定时间（以秒为单位）的响应。
	- min-fresh指示客户机可以接收响应时间小于当前时间加上指定时间的响应。 
	- max-stale指示客户机可以接收超出超时期间的响应消息。如果指定max-stale消息的值，那么客户机可以接收超出超时期指定值之内的响应消息。      
	
- `Connection:keep-alive`   
	HTTP持久连接（HTTP persistent connection，也称作HTTP keep-alive或HTTP connection reuse）是使用同一个TCP连接来发送和接收多个HTTP请求/应答，而不是为每一个新的请求/应答打开新的连接的方法。

- `Content-Encoding`        
	Accept-Encoding 和 Content-Encoding 是 HTTP 中用来对「采用何种编码格式传输正文」进行协定的一对头部字段。它的工作原理是这样：浏览器发送请求时，通过 Accept-Encoding 带上自己支持的内容编码格式列表；服务端从中挑选一种用来对正文进行编码，并通过 Content-Encoding 响应头指明选定的格式；浏览器拿到响应正文后，依据 Content-Encoding 进行解压。当然，服务端也可以返回未压缩的正文，但这种情况不允许返回 Content-Encoding。这个过程就是 HTTP 的内容编码机制。

- `Content-Type`          
	用于定义网络文件的类型和网页的编码，决定文件接收方将以什么形式、什么编码读取这个文件，这就是经常看到一些Asp网页点击的结果却是下载到的一个文件或一张图片的原因。      
	
	如果未指定 ContentType，默认为TEXT/HTML。

- `Date头域 `   
	Date头域表示消息发送的时间，时间的描述格式由rfc822定义。例如，Date:Mon,31Dec200104:25:57GMT。Date描述的时间表示世界标准时，换算成本地时间，需要知道用户所在的时区。

- `Expires（过期时间）HTTP头信息`

	Expires（过期时间） 属性是HTTP控制缓存的基本手段，这个属性告诉缓存器：相关副本在多长时间内是新鲜的。过了这个时间，缓存器就会向源服务器发送请求，检查文档是否被修 改。

	Expires 头信息：对于设置静态图片文件（例如导航栏和图片按钮）可缓存特别有用；因为这些图片修改很少，你可以给它们设置一个特别长的过期时间，这会使你的网站对 用户变得相应非常快；他们对于控制有规律改变的网页也很有用，例如：你每天早上6点更新新闻页，你可以设置副本的过期时间也是这个时间，这样缓存 服务器就知道什么时候去取一个更新版本，而不必让用户去按浏览器的“刷新”按钮。

- `Pragma头域 `    
	Pragma头域用来包含实现特定的指令，最常用的是Pragma:no-cache。在HTTP/1.1协议中，它的含义和Cache-Control:no-cache相同。	

- `Server响应头 `    
	Server响应头包含处理请求的原始服务器的软件信息。此域能包含多个产品标识和注释，产品标识一般按照重要性排序。

- `Host头域 `   
	Host头域指定请求资源的Intenet主机和端口号，必须表示请求url的原始服务器或网关的位置。HTTP/1.1请求必须包含主机头域，否则系统会以400状态码返回。

- `Referer头域 `     
	Referer 头域允许客户端指定请求uri的源资源地址，这可以允许服务器生成回退链表，可用来登陆、优化cache等。他也允许废除的或错误的连接由于维护的目的被追踪。如果请求的uri没有自己的uri地址，Referer不能被发送。如果指定的是部分uri地址，则此地址应该是一个相对地址。

- `Range头域 `   
	Range头域可以请求实体的一个或者多个子范围。例如，  
	表示头500个字节：bytes=0-499     
	表示第二个500字节：bytes=500-999     
	表示最后500个字节：bytes=-500     
	表示500字节以后的范围：bytes=500-     
	第一个和最后一个字节：bytes=0-0,-1     
	同时指定几个范围：bytes=500-600,601-999        
	但是服务器可以忽略此请求头，如果无条件GET包含Range请求头，响应会以状态码206（PartialContent）返回而不是以200 （OK）。 
	

	
##<code id="5">请求头(Requests Headers)</code>
- `Host头域 `     

	Host头域指定请求资源的Intenet主机和端口号，必须表示请求url的原始服务器或网关的位置。HTTP/1.1请求必须包含主机头域，否则系统会以400状态码返回。      
	当前请求网址的请求域

- `User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36`

	用户是通过什么工具来请求的     
	User-Agent头域的内容包含发出请求的用户信息。 

- `Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8`            
 
	Accept请求报头域用于指定客户端接受哪些类型的信息。eg：Accept：image/gif，表明客户端希望接受GIF图象格式的资源；Accept：text/html，表明客户端希望接受html文本。

- `Accept-Language:zh-CN,zh;q=0.8`
	
	Accept-Language请求报头域类似于Accept，但是它是用于指定一种自然语言。eg：Accept-Language:zh-cn.如果请求消息中没有设置这个报头域，服务器假定客户端对各种语言都可以接受

- `Accept-Encoding:gzip, deflate, sdch, br`     
	
	Accept-Encoding请求报头域类似于Accept，但是它是用于指定可接受的内容编码。eg：Accept-Encoding:gzip.deflate.如果请求消息中没有设置这个域服务器假定客户端对各种内容编码都可以接受。

- `Content-Type`   

	用于定义网络文件的类型和网页的编码，决定文件接收方将以什么形式、什么编码读取这个文件，这就是经常看到一些Asp网页点击的结果却是下载到的一个文件或一张图片的原因。      
	
	如果未指定 ContentType，默认为TEXT/HTML。
	
	在Http协议消息头中，使用Content-Type来表示具体请求中的媒体类型信息。       
	**例如**： Content-Type: text/html;charset:utf-8;

	 常见的媒体格式类型如下：
	
	- text/html ： HTML格式
	- text/plain ：纯文本格式     
	- text/xml ：  XML格式
	- image/gif ：gif图片格式   
	- image/jpeg ：jpg图片格式
	- image/png：png图片格式
	
	   以application开头的媒体格式类型：
	
	- application/xhtml+xml ：XHTML格式
	- application/xml     ： XML数据格式
	- application/atom+xml  ：Atom XML聚合格式   
	- application/json    ： JSON数据格式
	- application/pdf       ：pdf格式 
	- application/msword  ： Word文档格式
	- application/octet-stream ： 二进制流数据（如常见的文件下载）
	- application/x-www-form-urlencoded ： <form encType=””>中默认的encType，form表单数据被编码为key/value格式发送到服务器（表单默认的提交数据的格式）
	
	   另外一种常见的媒体格式是上传文件之时使用的：
	
	- multipart/form-data ： 需要在表单中进行文件上传时，就需要使用该格式
		
	   以上就是我们在日常的开发中，经常会用到的若干content-type的内容格式。

- `Content-Encoding`

	Accept-Encoding 和 Content-Encoding 是 HTTP 中用来对「采用何种编码格式传输正文」进行协定的一对头部字段。它的工作原理是这样：浏览器发送请求时，通过 Accept-Encoding 带上自己支持的内容编码格式列表；服务端从中挑选一种用来对正文进行编码，并通过 Content-Encoding 响应头指明选定的格式；浏览器拿到响应正文后，依据 Content-Encoding 进行解压。当然，服务端也可以返回未压缩的正文，但这种情况不允许返回 Content-Encoding。这个过程就是 HTTP 的内容编码机制。

	内容编码目的是优化传输内容大小，通俗地讲就是进行压缩。一般经过 gzip 压缩过的文本响应，只有原始大小的 1/4。对于文本类响应是否开启了内容压缩，是我们做性能优化时首先要检查的重要项目；而对于 JPG / PNG 这类本身已经高度压缩过的二进制文件，不推荐开启内容压缩，效果微乎其微还浪费 CPU。

- `Referer:https://www.zhihu.com/people/pa-chong-21/activities`

	是通过哪个页面到当前页面的（也就是上一个页面是什么？）
	举个例子，当我是通过百度搜索页面点到当前页面的，那么Referer就是百度搜索页
	
- `Content-Length`

	用于描述HTTP消息实体的传输长度。
	
    消息实体长度：即Entity-length，压缩之前的message-body的长度       
    消息实体的传输长度：Content-length，压缩后的message-body的长度。

- `Origin`	

	origin主要是用来说明最初请求是从哪里发起的；    
	origin只用于Post请求，而Referer则用于所有类型的请求；    
	origin的方式比Referer更安全点吧。 

- `Cookie:d_c0="AACAWNtZswqPTnJ8dFXqaygiq82ekPD5_-xxxx`
	
	举个例子，当我登录知乎后，知乎会给我一个cookie，然后我在以后的一段时间内，每次打开知乎，都不需要重新登录。这是因为浏览器每次都会把我之前存储的cookie带上。

- `Connection:keep-alive`
	
	HTTP持久连接（HTTP persistent connection，也称作HTTP keep-alive或HTTP connection reuse）是使用同一个TCP连接来发送和接收多个HTTP请求/应答，而不是为每一个新的请求/应答打开新的连接的方法。

- `Upgrade Insecure Requests`

	我们的页面是 https 的，而这个页面中包含了大量的 http 资源（图片、iframe等），页面一旦发现存在上述响应头，会在加载 http 资源时自动替换成 https 请求。

- `Cache-Control:no-cache`

	Cache-Control 是用来控制网页的缓存


- `If-Modified-Since:Wed, 15 Feb 2017 09:14:13 GMT`(缓存时间) 
- `If-None-Match:W/"58a41be5-190aa" `
- `Last-Modified:Wed, 15 Feb 2017 09:14:13 GMT` 
- `ETag:"58a41be5-190aa"`       
	这4个一般静态页面会用到 If-Modified-Since,If-None-Match这两个是请求头，ETag,Last-Modified是返回头（服务器返回的）   
	如果If-Modified-Since的值和Last-Modified相等 则表明当前请求的内容没有变动，服务器返回,If-None-Match和ETag 同理


##<code id="6">响应头(Response)</code>








来自：
>http://blog.csdn.net/mm2223/article/details/8089645/       
>http://fex.baidu.com/blog/2014/05/what-happen/      (计算机网络)
>http://blog.csdn.net/blueheart20/article/details/45174399    (请求头、响应头)
>http://www.tuicool.com/articles/b6BNNfN       (Accept-Encoding 和 Content-Encoding)
>