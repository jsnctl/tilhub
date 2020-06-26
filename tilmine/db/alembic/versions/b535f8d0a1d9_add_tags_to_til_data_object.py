"""add tags to til data object

Revision ID: b535f8d0a1d9
Revises: da229e3b86ad
Create Date: 2020-06-26 23:02:25.237204

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY


# revision identifiers, used by Alembic.
revision = 'b535f8d0a1d9'
down_revision = 'da229e3b86ad'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("todayilearned",
                  sa.Column("display_tags", ARRAY(sa.String)))


def downgrade():
    op.drop_column("todayilearned", "display_tags")
