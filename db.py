import atexit
from sqlalchemy import Column, String, Integer, DateTime, create_engine, func,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
import config
PG_DSN = config.PG_DSN

engine = create_engine(PG_DSN)

Base = declarative_base()
Session = sessionmaker(bind=engine)

atexit.register(engine.dispose)

class Advertisement(Base):

    __tablename__ = 'advertisement'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=40), nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    user_name = Column(String(length=40),nullable=False)

    def __str__(self):
        return f'Advertisement {self.id}: {self.title} by User {self.user_id}'



Base.metadata.create_all(bind=engine)