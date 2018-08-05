import os

from tornado.options import define, options, parse_command_line, parse_config_file


def initialize(args=None):
    parse_command_line(args)
    if options.config:
        parse_config_file(path=options.config)
    else:
        config_file = "./config/local.conf"
        parse_config_file(path=config_file)
    parse_command_line(args)


# Environment
define('port', default=8080)
define('config', default=None)

# Postgresql
define('db_user', default=os.getenv('DB_USER', 'ciex'))
define('db_pass', default=os.getenv('DB_PASS', 'ciex'))
define('db_name', default=os.getenv('DB_NAME', 'ciex_db'))
define('db_host', default=os.getenv('DB_HOST', '127.0.0.1'))
define('db_port', default=int(os.getenv('DB_PORT', 5432)))

