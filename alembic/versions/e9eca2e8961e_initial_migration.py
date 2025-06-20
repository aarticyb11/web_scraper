"""Initial migration

Revision ID: e9eca2e8961e
Revises: 
Create Date: 2025-06-05 15:59:38.741791

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9eca2e8961e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('run_id', sa.UUID(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('status', sa.Enum('SCHEDULED', 'STARTED', 'FAILED', 'FINISHED', name='status_enum'), nullable=False),
    sa.Column('error', sa.Text(), nullable=True),
    sa.Column('started_at', sa.DateTime(), nullable=True),
    sa.Column('finished_at', sa.DateTime(), nullable=True),
    sa.Column('failed_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('run_id')
    )
    op.create_table('legitimate_sellers',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('site', sa.String(length=100), nullable=False),
    sa.Column('ssp_domain_name', sa.String(length=200), nullable=False),
    sa.Column('publisher_id', sa.String(length=200), nullable=False),
    sa.Column('relationship', sa.String(length=50), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('run_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['run_id'], ['tasks.run_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('legitimate_sellers')
    op.drop_table('tasks')
    # ### end Alembic commands ###
