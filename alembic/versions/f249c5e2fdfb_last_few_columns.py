"""last few Columns

Revision ID: f249c5e2fdfb
Revises: 227e7cb49081
Create Date: 2021-11-09 12:38:04.820976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f249c5e2fdfb'
down_revision = '227e7cb49081'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'is_free', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'is_free')
    op.drop_column('posts', 'created_at')
    pass
