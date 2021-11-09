"""create posts table

Revision ID: d8b715d34e08
Revises: 
Create Date: 2021-11-09 11:45:02.246770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8b715d34e08'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('name', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
