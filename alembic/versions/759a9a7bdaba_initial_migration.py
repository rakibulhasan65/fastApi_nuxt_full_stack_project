"""Initial migration

Revision ID: 759a9a7bdaba
Revises: 51705c6c1107
Create Date: 2025-07-31 10:19:58.346365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '759a9a7bdaba'
down_revision: Union[str, Sequence[str], None] = '51705c6c1107'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('product_code', sa.String(), nullable=True))
    op.create_index(op.f('ix_products_product_code'), 'products', ['product_code'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_product_code'), table_name='products')
    op.drop_column('products', 'product_code')
    # ### end Alembic commands ###
