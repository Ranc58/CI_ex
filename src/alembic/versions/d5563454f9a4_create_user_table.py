"""create user table

Revision ID: d5563454f9a4
Revises: 
Create Date: 2018-08-05 16:57:10.854995

"""
from sqlalchemy.sql.functions import now
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5563454f9a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('user_id', sa.Integer, primary_key=True),
                    sa.Column('first_name', sa.String(255)),
                    sa.Column('last_name', sa.String(255)),
                    sa.Column('phone_number', sa.String(255)),
                    sa.Column('create_dttm', sa.DateTime(), server_default=now()),
                    sa.Column('update_dttm', sa.DateTime(), nullable=True),
                    sa.Column('delete_dttm', sa.DateTime(), nullable=True),
    )

def downgrade():
    op.drop_table('user')
