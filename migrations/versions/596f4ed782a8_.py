"""empty message

Revision ID: 596f4ed782a8
Revises: a35953628a34
Create Date: 2025-05-23 09:17:27.604920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '596f4ed782a8'
down_revision = 'a35953628a34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('target', schema=None) as batch_op:
        batch_op.add_column(sa.Column('startdate', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('target', schema=None) as batch_op:
        batch_op.drop_column('startdate')

    # ### end Alembic commands ###
