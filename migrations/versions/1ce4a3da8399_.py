"""empty message

Revision ID: 1ce4a3da8399
Revises: 826c022d5442
Create Date: 2021-03-23 10:37:10.161727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ce4a3da8399'
down_revision = '826c022d5442'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('my_property', sa.Column('bathrooms', sa.String(length=15), nullable=True))
    op.add_column('my_property', sa.Column('description', sa.String(length=500), nullable=True))
    op.add_column('my_property', sa.Column('filename', sa.String(length=120), nullable=True))
    op.add_column('my_property', sa.Column('location', sa.String(length=100), nullable=True))
    op.add_column('my_property', sa.Column('price', sa.String(length=15), nullable=True))
    op.add_column('my_property', sa.Column('ptype', sa.String(length=15), nullable=True))
    op.add_column('my_property', sa.Column('rooms', sa.String(length=15), nullable=True))
    op.add_column('my_property', sa.Column('title', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('my_property', 'title')
    op.drop_column('my_property', 'rooms')
    op.drop_column('my_property', 'ptype')
    op.drop_column('my_property', 'price')
    op.drop_column('my_property', 'location')
    op.drop_column('my_property', 'filename')
    op.drop_column('my_property', 'description')
    op.drop_column('my_property', 'bathrooms')
    # ### end Alembic commands ###
