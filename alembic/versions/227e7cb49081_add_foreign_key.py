"""add foreign key

Revision ID: 227e7cb49081
Revises: 49e8b8ad5319
Create Date: 2021-11-09 12:32:33.421032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '227e7cb49081'
down_revision = '49e8b8ad5319'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
