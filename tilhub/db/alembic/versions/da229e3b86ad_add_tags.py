"""add tags

Revision ID: da229e3b86ad
Revises: e868c8423bd1
Create Date: 2020-06-21 21:07:41.070777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da229e3b86ad'
down_revision = 'e868c8423bd1'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'tags',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('til_id', sa.Integer, sa.ForeignKey('todayilearned.id')),
        sa.Column('name', sa.String)
    )


def downgrade():
    op.drop_table('tags')
