"""empty message

Revision ID: 4b91d6e7af41
Revises: 
Create Date: 2022-10-27 17:49:02.225393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b91d6e7af41'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('catch_pokemon',
    sa.Column('poke_id', sa.Integer(), nullable=False),
    sa.Column('pokemon', sa.String(length=50), nullable=False),
    sa.Column('ability', sa.String(length=50), nullable=False),
    sa.Column('hp', sa.Integer(), nullable=False),
    sa.Column('attack', sa.Integer(), nullable=False),
    sa.Column('defense', sa.Integer(), nullable=False),
    sa.Column('baseXP', sa.Integer(), nullable=False),
    sa.Column('sprite', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('poke_id'),
    sa.UniqueConstraint('pokemon')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('catch_pokemon')
    # ### end Alembic commands ###
