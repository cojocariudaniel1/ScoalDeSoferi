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
from programare import Programare
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


def query2():
    data = []
    session = Session()
    pachet_ore = session.query(PachetOre)
    for row in pachet_ore:
        items = []
        items.append(row.durata)
        print(items)
        instructor = session.query(Instructor).filter(Instructor.id == row.instructor_id)
        for row in instructor:
            personal = session.query(Personal).filter(Personal.id == row.personal_id)
            for row in personal:
                personal_name = f"{personal.nume} {personal.prenume}"
                items.append(personal_name)
            vehicul = session.query(Vehicul).filter(Vehicul.id == row.vehicul_id)
            for row in vehicul:
                items.append(row.marca)
        data.append(items)
    print(data)

def query3():
    session = Session()
    data = []
    pachet_ore_relation = session.query(PachetOre.instructor_pachet_ore_relationship)
    for row in pachet_ore_relation:
        items = []
        pachet_ore = session.query(PachetOre).filter(PachetOre.id == row[1])
        instructor = session.query(Instructor).filter(Instructor.id == row[0])
        for k in pachet_ore:
            items.append(k.durata)
        for k in instructor:
            personal = session.query(Personal).filter(Personal.id == k.personal_id)
            for row in personal:
                personal_name = f"{row.nume} {row.prenume}"
                items.append(personal_name)
            vehicul = session.query(Vehicul).filter(Vehicul.id == k.vehicul_id)
            for row in vehicul:
                items.append(row.marca)
        data.append(items)
    print(data)


def test():
    another_list = []
    list = [[30, 200, 'Hongu Cosmin', 'Audi', 'AER 424', 'Manual'], [30, 200, 'Abaza Bianca', 'BMW', 'KJL 947', 'Manual'], [15, 100, 'Socolenco Natalia', 'Renault', 'TTR 884', 'Automat'], [15, 100, 'Macaru Iraida', 'Volkswagen', 'OPP 231', 'Automat']]
    for row in list:
        if row[5] == "Manual":
            another_list.append(row)
    print(another_list)

def test4():
    session = Session()
    query = session.query(Sediu)
    for i in query:
        print(i.email)
    session.commit()
    session.close()


test4()
