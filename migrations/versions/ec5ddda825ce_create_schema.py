"""create schema

Revision ID: ec5ddda825ce
Revises:
Create Date: 2023-01-22 15:43:12.663404

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ec5ddda825ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'requests',
        sa.Column('request_id', sa.Integer, primary_key=True),
        sa.Column('phone_number', sa.String(64), nullable=False),
        sa.Column(
            'date_created',
            sa.DateTime(timezone=True),
            server_default=sa.text('CURRENT_TIMESTAMP'),
        ),
        sqlite_autoincrement=True,
    )


def downgrade() -> None:
    op.drop_table('requests')
