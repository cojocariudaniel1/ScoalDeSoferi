from datetime import date

from sqlalchemy import create_engine, table
from sqlalchemy.orm import sessionmaker

from base import Session, Base, engine

from cont import Cont



def create_all():
    session = Session()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # creare cont
    cont1 = Cont("1001", "Daniel", "parola123")

    session.add(cont1)

    session.commit()
    session.close()

create_all()