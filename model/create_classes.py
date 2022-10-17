from datetime import date

from sqlalchemy import create_engine, table
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from base import Session, Base, engine
from cont import Cont
from cursant import Cursant
from instructor import Instructor
from pachet_ore import PachetOre

from personal import Personal
from sediu import Sediu
from address import Address
from vehicul import Vehicul
from delete_database import delete_db


def adaugare_instructor(instructor, cont, vehicul, personal):
    instructor.cont = cont
    instructor.vehicul = vehicul
    instructor.personal = personal
    return instructor


def create_all():
    session = Session()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # Sediu | Numar telefon, Email address
    sediu1 = Sediu(1234, "xxxx@gmail.com")
    sediu2 = Sediu(1234, "xxxx@gmail.com")
    sediu3 = Sediu(1234, "xxxx@gmail.com")
    sediu4 = Sediu(1234, "xxxx@gmail.com")
    sediu5 = Sediu(1234, "xxxx@gmail.com")

    # Address | Strada, oras, tara, cod postal, Judet
    adress1 = Address('Strada1', 'Oras1', 'Tara1,', 1231, 'Judet1')
    adress2 = Address('Strada2', 'Oras2', 'Tara1,', 1232, 'Judet1')
    adress3 = Address('Strada3', 'Oras3', 'Tara1,', 1233, 'Judet2')
    adress4 = Address('Strada4', 'Oras4', 'Tara1,', 1234, 'Judet2')
    adress5 = Address('Strada5', 'Oras5', 'Tara1,', 1235, 'Judet3')

    # Personal | Nume, prenume
    personal1 = Personal("Nume1", "Prenume1")
    personal2 = Personal("Nume2", "Prenume2")
    personal3 = Personal("Nume3", "Prenume3")
    personal4 = Personal("Nume4", "Prenume4")
    personal5 = Personal("Nume5", "Prenume5")

    # Vehicul | Marca, model, anFabricatie, instructor.
    vehicul1 = Vehicul("Audi", "Model1", "2022")
    vehicul2 = Vehicul("BMW", "Model2", "2010")
    vehicul3 = Vehicul("Skoda", "Model3", "2010")
    vehicul4 = Vehicul("Golf", "Model4", "2000")
    vehicul5 = Vehicul("Smart", "Model5", "2005")

    # Instructori
    # Creare cont pentru instructori
    instructor_cont1 = Cont("user_inst1", "parola1", 1)
    instructor_cont2 = Cont("user_inst2", "parola2", 1)
    instructor_cont3 = Cont("user_inst3", "parola3", 1)

    # Creare instructori respectivi | Cont instructor, Vehicul, Personal respectiv
    instructor1 = Instructor()
    instructor1 = adaugare_instructor(instructor1, instructor_cont1, vehicul1, personal1)
    instructor2 = adaugare_instructor(Instructor(), instructor_cont2, vehicul2, personal2)
    instructor3 = adaugare_instructor(Instructor(), instructor_cont3, vehicul3, personal3)

    # Creare pachet_ore
    pachet_ore1 = PachetOre("30")
    pachet_ore1.instructor_id = 1

    # Creare Cursant:
    cursant1 = Cursant("Nume1", "Prenume1", "10/10/2001")
    cursant1.cont = Cont("user1", "parola1", 0)

    # Adaugare personal in sediu.
    sediu1.personal = [personal1, personal3]
    sediu2.personal = [personal2]

    # Adaugare adresa
    sediu1.address = adress1
    sediu2.address = adress2
    sediu3.address = adress3
    sediu4.address = adress4
    sediu5.address = adress5

    # Commit values:
    session.add_all([
        sediu1, sediu2, sediu4, sediu5, sediu3,

        personal1, personal2, personal4, personal5, personal3,

        vehicul1, vehicul2, vehicul3, vehicul5, vehicul4,

        instructor1, instructor3, instructor2,

        pachet_ore1,

        cursant1]

    )

    session.commit()
    session.close()


create_all()
