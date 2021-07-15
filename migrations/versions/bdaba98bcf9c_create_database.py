"""create database

Revision ID: bdaba98bcf9c
Revises: 
Create Date: 2021-07-14 23:39:11.517964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bdaba98bcf9c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=126), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(length=522), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_empty', sa.Boolean(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=126), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('current_price', sa.Float(), nullable=False),
    sa.Column('discount', sa.Integer(), nullable=True),
    sa.Column('amount_products', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('image_url', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('carts_products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity_product', sa.Integer(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['carts.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=126), nullable=True),
    sa.Column('last_name', sa.String(length=126), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(length=126), nullable=True),
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('update_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['carts.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cart_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=126), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('complement', sa.String(length=50), nullable=True),
    sa.Column('zipcode', sa.String(length=9), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('state', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('addresses')
    op.drop_table('customers')
    op.drop_table('carts_products')
    op.drop_table('products')
    op.drop_table('carts')
    op.drop_table('admin')
    # ### end Alembic commands ###
