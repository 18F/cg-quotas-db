"""empty message

Revision ID: 36faeb18642
Revises: 320bca1fc35
Create Date: 2015-11-02 13:03:13.810978

"""

# revision identifiers, used by Alembic.
revision = '36faeb18642'
down_revision = '320bca1fc35'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service',
    sa.Column('quota', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('guid', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('date_collected', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('label', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('provider', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('instance_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['quota'], ['quota.guid'], name='service_quota_fkey'),
    sa.PrimaryKeyConstraint('quota', 'guid', 'date_collected', name='quota_serviceguid_date')
    )
    ### end Alembic commands ###
