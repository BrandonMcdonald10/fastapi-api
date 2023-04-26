"""add user table

Revision ID: 30bb005423e6
Revises: ea93ad0ee5a2
Create Date: 2023-04-25 16:37:23.505248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30bb005423e6'
down_revision = 'ea93ad0ee5a2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
