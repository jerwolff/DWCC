"""Adding LKUPHp table

Revision ID: 0472a421e095
Revises: 394b8ecae90b
Create Date: 2019-07-08 17:11:16.207094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0472a421e095'
down_revision = '394b8ecae90b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lkup_hp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_name', sa.String(length=4096), nullable=True),
    sa.Column('base_hp', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lkup_hp')
    # ### end Alembic commands ###
