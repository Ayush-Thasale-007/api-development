"""add column to post table

Revision ID: 6db3639a8dc3
Revises: 3eda51a9d065
Create Date: 2021-11-09 12:26:39.814707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6db3639a8dc3'
down_revision = '3eda51a9d065'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("category", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "category")

    pass
