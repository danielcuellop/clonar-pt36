"""empty message

Revision ID: 3e191948b19a
Revises: d887d6db9550
Create Date: 2023-06-20 03:36:27.650055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e191948b19a'
down_revision = 'd887d6db9550'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('muestra', schema=None) as batch_op:
        batch_op.add_column(sa.Column('aditional_coments', sa.String(length=90), nullable=False))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.drop_column('aditional_comments')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('muestra', schema=None) as batch_op:
        batch_op.add_column(sa.Column('aditional_comments', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')
        batch_op.drop_column('aditional_coments')

    # ### end Alembic commands ###
