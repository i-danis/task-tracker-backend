"""create user table

Revision ID: 6e6233c47a99
Revises:
Create Date: 2023-02-26 13:53:48.677175

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "6e6233c47a99"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_model",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("email", sa.String(length=254), nullable=False),
        sa.Column("hashed_password", sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_model_email"), "user_model", ["email"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_model_email"), table_name="user_model")
    op.drop_table("user_model")
    # ### end Alembic commands ###
