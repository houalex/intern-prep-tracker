"""empty message

Revision ID: 82c4e1ff568b
Revises: 6c58c656bacf
Create Date: 2025-05-22 09:19:37.222355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82c4e1ff568b'
down_revision = '6c58c656bacf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('targetdate', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('progressleetcode', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('progressleetcode')
        batch_op.drop_column('targetdate')

    # ### end Alembic commands ###
