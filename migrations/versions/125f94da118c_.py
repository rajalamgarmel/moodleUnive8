"""empty message

Revision ID: 125f94da118c
Revises: 0da2290338d7
Create Date: 2020-10-30 22:16:00.342258

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '125f94da118c'
down_revision = '0da2290338d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('administrateur', sa.Column('is_admin', sa.Boolean(), nullable=True))
    op.drop_column('administrateur', 'is_superadmin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('administrateur', sa.Column('is_superadmin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('administrateur', 'is_admin')
    # ### end Alembic commands ###
