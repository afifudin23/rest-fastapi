# import uuid
#
# from sqlalchemy import Column, Integer, String, Boolean
# from sqlalchemy.dialects.postgresql import UUID
#
# from db import Base
#
#
# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
#     name = Column(String, index=True)
#     age = Column(Integer)
#     is_married = Column(Boolean, default=False)
    

# op.create_table(
#         "user_posts",
#         sa.Column("id", sa.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
#         sa.Column("user_id", sa.UUID(as_uuid=True), sa.ForeignKey("users.id")),
#         sa.Column("title", sa.String(255), nullable=False),
#         sa.Column("content", sa.TEXT, nullable=False)
#     )
