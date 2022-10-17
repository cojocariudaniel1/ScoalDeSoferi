from datetime import date

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
from vehicul import Vehicul


def create_all():
    session = Session()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    personal1 = Personal("TEST1", "TEST1")

    x = Instructor()

    x.cont = Cont("instructor_user", "parola1", 2)
    x.vehicul = Vehicul("marca1", "model", '10/10/2022')
    x.personal = personal1
    # sediu1 = Sediu(7123211, "email@email.test")
    # sediu2 = Sediu(7123211, "email@email.test")
    # adress1 = Address('Strada1', 'Oras1', 'Tara1,', 123, 'JUdet1')
    # sediu1.address = adress1

    personal2 = Personal("TEST2", "TEST2")
    personal3 = Personal("TEST3", "TEST3")

    personal1.cont = Cont("user1", "parola1", 3)

    # sediu1.personal = [personal1, personal3]
    # sediu2.personal = [personal2]

    session.add(personal3)
    session.add(personal1)
    session.add(personal2)
    session.add(x)

    # session.add(sediu1)
    # session.add(sediu2)

    session.commit()
    session.close()


def drop_table(table_name, engine=engine):
    Base = declarative_base()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables[table_name]
    if table is not None:
        Base.metadata.drop_all(engine, [table], checkfirst=True)


# drop_table(Address)
create_all()
