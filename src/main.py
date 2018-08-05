import logging

from models.database import init_db, get_connection_string
from tornado.ioloop import IOLoop
from tornado.options import options
import tornado.httpserver

import config

config.initialize()

from routes import url_list

app = tornado.web.Application(url_list)


if __name__ == '__main__':
    loop = IOLoop.instance()
    db_connection_string = get_connection_string()
    http_server = tornado.httpserver.HTTPServer(app)
    logging.info("Listing on http://localhost:{}".format(options.port))
    http_server.listen(options.port)
    loop.add_callback(init_db, db_connection_string, app)
    loop.start()
