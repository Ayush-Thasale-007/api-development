"""add column to post table

Revision ID: 3eda51a9d065
Revises: d8b715d34e08
Create Date: 2021-11-09 12:10:34.748987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3eda51a9d065'
down_revision = 'd8b715d34e08'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("brief", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "brief")
    pass
