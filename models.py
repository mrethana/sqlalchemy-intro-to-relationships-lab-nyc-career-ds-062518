from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# write the Role and Actor classes below
class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key = True)
    character = Column(Text)
    actor_id = Column(Integer, ForeignKey("actors.id"))
    actor = relationship("Actor", back_populates = "roles")

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    roles = relationship(Role, order_by = Role.id, back_populates = "actor")



engine = create_engine('sqlite:///actors.db')
Base.metadata.create_all(engine)
