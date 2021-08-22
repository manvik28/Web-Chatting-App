from pywebio.platform.tornado import webio_handler
from tornado.ioloop
from tornado.web
from tornado.options import define,options

# 127.0.0.0:8080
define('port',default=8080, help = "Run on the given port", type = int)
define('debug',default = False, help = "Run on thne debug mode", type = bool)

if __name__ == '__main__':
  tornado.options.parse_comand_line()
  tornado_setting = {'debug' : options.debug}