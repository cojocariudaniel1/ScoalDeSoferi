from datetime import date
from sqlalchemy import select
from personal_administrativ import PersonalAdministrativ

from sqlalchemy import create_engine, table
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from base import Session, Base, engine
from cont import Cont
from instructor import Instructor
from personal import Personal
from sediu import Sediu
from address import Address
from cursant import Cursant
from vehicul import Vehicul
from pachet_ore import PachetOre

def query():
    session = Session()
    query = session.query(Cont)
    for row in query:
        print(f"Username : {row.user}, Parola: {row.parola}")
    session.commit()
    session.close()

query()