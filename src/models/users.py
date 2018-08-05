from datetime import datetime


from models.database import CiexEngine
from models.models import user


@CiexEngine.connection_required
async def create_user(conn, data):
    res = await conn.execute(user.insert().returning(*user.c).values(
        create_dttm=datetime.now(),
        **data)
    )
    return await res.fetchone()


@CiexEngine.connection_required
async def get_all_users(conn):
    res = await conn.execute(user.select().where(
        user.c.delete_dttm.is_(None)
    ))
    return await res.fetchall()


@CiexEngine.connection_required
async def update_user(conn, user_id, data):
    res = await conn.execute(
        user.update().where(user.c.user_id == user_id).values(
            update_dttm=datetime.now(),
            **data).returning(*user.c)
    )
    return await res.first()


@CiexEngine.connection_required
async def delete_user(conn, user_id):
    res = await conn.execute(
        user.update().where(user.c.user_id == user_id).values(
            update_dttm=datetime.now(),
            delete_dttm=datetime.now()
        ).returning(*user.c)
    )
    return await res.fetchone()


@CiexEngine.connection_required
async def get_user_by_id(conn, user_id):
    res = await conn.execute(
        user.select().where(user_id == user_id)
    )
    return await res.first()
