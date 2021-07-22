"""delete total

Revision ID: c819cc49d726
Revises: 9dde868af8d1
Create Date: 2021-07-20 22:08:08.731021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c819cc49d726'
down_revision = '9dde868af8d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'total')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('total', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
