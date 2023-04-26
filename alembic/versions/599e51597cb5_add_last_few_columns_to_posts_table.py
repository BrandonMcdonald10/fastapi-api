"""add last few columns to posts table

Revision ID: 599e51597cb5
Revises: 2e5c44c35d3f
Create Date: 2023-04-25 16:56:12.262493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '599e51597cb5'
down_revision = '2e5c44c35d3f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
