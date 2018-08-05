import sqlalchemy as sa
from sqlalchemy.sql.functions import now

metadata = sa.MetaData()

user = sa.Table('user', metadata,
                sa.Column('user_id', sa.Integer, primary_key=True),
                sa.Column('first_name', sa.String(255)),
                sa.Column('last_name', sa.String(255)),
                sa.Column('phone_number', sa.String(255)),
                sa.Column('create_dttm', sa.DateTime(), server_default=now()),
                sa.Column('update_dttm', sa.DateTime(), nullable=True),
                sa.Column('delete_dttm', sa.DateTime(), nullable=True),
                )
