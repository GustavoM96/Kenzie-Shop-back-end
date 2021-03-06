"""add columns created and update on cart_products table

Revision ID: 6e39379213fd
Revises: 90820461f556
Create Date: 2021-07-18 14:13:33.202305

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6e39379213fd'
down_revision = '90820461f556'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carts_products', sa.Column('created_at', sa.TIMESTAMP(), nullable=True))
    op.add_column('carts_products', sa.Column('updated_at', sa.TIMESTAMP(), nullable=True))
    op.alter_column('products', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('products', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'updated_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('products', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_column('carts_products', 'updated_at')
    op.drop_column('carts_products', 'created_at')
    # ### end Alembic commands ###
