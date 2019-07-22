## Tornado

[Tornado](http://www.tornadoweb.org/)是一个Python Web框架和异步网络库，最初是由[FriendFeed](http://friendfeed.com/)进行开发。通过使用非阻塞网路I/O。Tornado可以扩展到数万个开放连接，使其成为[long polling](http://en.wikipedia.org/wiki/Push_technology#Long_polling)、[websockets](http://en.wikipedia.org/wiki/WebSocket)和其他需要和每个用户建立长期链接的应用程序的理想选择。

#### 快速链接

- 当前版本：6.0.3（[使用PypI下载](https://pypi.python.org/pypi/tornado)，[发布日志](https://www.tornadoweb.org/en/stable/releases.html)）
- 源代码（[Github](https://github.com/tornadoweb/tornado)）
- [Stack Overflow](http://stackoverflow.com/questions/tagged/tornado)

- [维基百科](https://github.com/tornadoweb/tornado/wiki/Links)

#### Hello, world

下面是一个使用Tornado框架"hello, world"web应用简单示例：

```python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

上面的示例并没有使用Tornado异步功能，查看异步示例项目[聊天室](https://github.com/tornadoweb/tornado/tree/stable/demos/chat)。

#### Threads and WSGI

Tornado不同于其他Python web框架，它并没有基于[WSGI](https://wsgi.readthedocs.io/en/latest/)进行开发。通常Tornado运行时每个进程只有一个线程。了解更多Tornado异步编程请异步[用户指导](https://www.tornadoweb.org/en/stable/guide.html)。

在`tornado.wsgi`模块中也提供了对WSGI的一些支持，当然那并不是主要的开发目的，大多数的应用都应该使用Tornado的自有接口代替使用WSGI进行开发（比如`tornado.web`）。

Tornado的代码通常都不是线程安全的。在Tornado框架中调用其他线程的唯一的安全方法是`IOLoop.add_callback`。用户可以使用`IOLoop.run_in_executor`去异步化执行一个在其他线程中被阻塞的功能，但是需要注意传入到`run_in_executor`中的参数应该避免任何一个Tornado中的对象。`run_in_executor`是一个推荐使用的和阻塞代码进行交互的方法。

#### `asyncio` Integration

Tornado集成了Python中的标准库`asyncio`模块可以分享同一个事件循环(event loop)(>= Tornado 5.0)。设计用户`asyncio`的库也可以在Tornado中进行使用。

#### Installation

> pip install tornado

Tornado可以使用`pip`进行安装。

**安装条件**如下：

- Tornado 6.0需要Python 3.5.2以上版本
- 在`tornado.curl_httpclient`中有使用[pycurl](http://pycurl.sourceforge.net/)，需要其7.22以上版本
- [Twisted](http://www.twistedmatrix.com/)可能会被用到`tornado.platform.twisted`中的某些类中
- 在线程阻塞的时候可以选择使用非阻塞DNS解析器[pycares](https://pypi.python.org/pypi/pycares)

**平台需求**：

