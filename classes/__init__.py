from sqlalchemy.orm import sessionmaker

from base import Base, engine

Session = sessionmaker(bind=engine)
