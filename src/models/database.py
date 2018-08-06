import functools

from tornado.options import options
from aiopg.sa import SAConnection, create_engine



class DbEngine:
    """Singleton. Main point to acquire db connections from."""
    db = None

    def connection_required(self, func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            engine = await create_engine(get_connection_string())
            async with engine:
                async with engine.acquire() as conn:
                    return await func(conn, *args, **kwargs)
        return wrapper


CiexEngine = DbEngine()


async def init_db(dsn, app):
    engine = await create_engine(dsn)
    app.db = engine
    CiexEngine.db = engine


def get_connection_url():
    host = options.db_host
    port = options.db_port
    user = options.db_user
    password = options.db_pass
    dbname = options.db_name

    return f'postgresql://{user}:{password}@{host}:{port}/{dbname}'


def get_connection_string():
    return ' '.join([
        f'dbname={options.db_name}',
        f'user={options.db_user}',
        f'password={options.db_pass}',
        f'host={options.db_host}',
        f'port={options.db_port}'
    ])
