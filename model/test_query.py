from datetime import date
from sqlalchemy import select

from sqlalchemy import create_engine, table
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from base import Session, Base, engine

from personal import Personal
from sediu import Sediu
from address import Address

def query():
    session = Session()
    result = session.execute(select(Sediu).where(Sediu.id == 1))
    session.commit()
    session.close()
query()