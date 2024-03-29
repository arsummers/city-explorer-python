"""testing full city

Revision ID: 5b54de69c585
Revises: 15a3aa588bef
Create Date: 2019-07-17 17:33:10.812155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b54de69c585'
down_revision = '15a3aa588bef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('locations_model', sa.Column('formatted_query', sa.String(length=256), nullable=True))
    op.add_column('locations_model', sa.Column('latitude', sa.Float(), nullable=True))
    op.add_column('locations_model', sa.Column('longitude', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('locations_model', 'longitude')
    op.drop_column('locations_model', 'latitude')
    op.drop_column('locations_model', 'formatted_query')
    # ### end Alembic commands ###
