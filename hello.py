import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class IndexHander(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'hello')
        self.write(greeting + ', friendly user!')


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHander)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


"""
步骤解析：
    1.使用tornado.options模块解析命令行
    2.创建tornado的Allication类的实例
    3.handlers参数可以按需要指定任意多个元组()
        - 元组中包括HTTP请求的路径和一个RequestHandler类
        - 字符串"/"被看作为"^/$"
"""