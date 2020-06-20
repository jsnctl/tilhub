"""baseline

Revision ID: e868c8423bd1
Revises: 
Create Date: 2020-06-18 22:28:25.055176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e868c8423bd1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'todayilearned',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('added', sa.DateTime(), default=sa.func.now()),
        sa.Column('user', sa.String()),
        sa.Column('til', sa.String())
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(100), nullable=False, unique=True),
        sa.Column('password', sa.String(200), nullable=False),
        sa.Column('email', sa.String(200), nullable=False),
        sa.Column('date_created', sa.DateTime, default=sa.func.now())
    )


def downgrade():
    op.drop_table('todayilearned')
    op.drop_table('users')
