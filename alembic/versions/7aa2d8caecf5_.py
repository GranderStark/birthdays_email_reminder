"""empty message

Revision ID: 7aa2d8caecf5
Revises: bf782fe21a00
Create Date: 2019-03-17 16:02:59.853855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7aa2d8caecf5'
down_revision = 'bf782fe21a00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fio', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'fio')
    # ### end Alembic commands ###
