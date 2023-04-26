"""add content column to posts table

Revision ID: ea93ad0ee5a2
Revises: e2f838049203
Create Date: 2023-04-25 16:30:16.411585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea93ad0ee5a2'
down_revision = 'e2f838049203'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
