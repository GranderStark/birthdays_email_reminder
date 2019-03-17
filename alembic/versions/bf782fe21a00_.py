"""empty message

Revision ID: bf782fe21a00
Revises: 
Create Date: 2019-03-17 15:51:36.491798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf782fe21a00'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('is_supervisor', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###