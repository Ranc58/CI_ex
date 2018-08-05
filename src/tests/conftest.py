import os

from aiopg.sa import create_engine
from sqlalchemy.orm import sessionmaker
from tornado.testing import AsyncHTTPTestCase
from aiopg.sa.connection import SAConnection
from alembic import command
from alembic.config import Config
import config

config.initialize()

from models.database import CiexEngine, get_connection_url

APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ALEMBIC_INI_PATH = os.path.join(APP_ROOT, 'alembic.ini')
ALEMBIC_DIRECTORY = os.path.join(APP_ROOT, 'alembic')

DB_CONN_URL = get_connection_url()


def get_alembic_config():
    alembic_config = Config(ALEMBIC_INI_PATH)
    alembic_config.set_main_option("url", DB_CONN_URL)
    alembic_config.set_main_option('script_location', ALEMBIC_DIRECTORY)
    return alembic_config


class BaseTestCase(AsyncHTTPTestCase):
    app = None

    def get_app(self):
        import main
        self.app = main.app
        return self.app

    def setUp(self):
        command.downgrade(get_alembic_config(), 'base')
        command.upgrade(get_alembic_config(), 'head')
        return super().setUp()

    def tearDown(self):
        command.downgrade(get_alembic_config(), 'base')
        return super().tearDown()
