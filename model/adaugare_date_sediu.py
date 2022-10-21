from base import Session, Base, engine
from cont import Cont
from cursant import Cursant
from instructor import Instructor
from pachet_ore import PachetOre

from personal import Personal
from personal_administrativ import PersonalAdministrativ
from sediu import Sediu
from address import Address
from vehicul import Vehicul


def adaugare_date_sediu():
    session = Session()
    sediu1 = Sediu(1234, "xxxx@gmail.com")
    sediu2 = Sediu(1234, "xxxx@gmail.com")
    sediu3 = Sediu(1234, "xxxx@gmail.com")
    sediu4 = Sediu(1234, "xxxx@gmail.com")
    sediu5 = Sediu(1234, "xxxx@gmail.com")
    sediu6 = Sediu(1232, "xxxx@")

    sediu5.address()

    session.add_all(
        [
            sediu6, sediu5, sediu1, sediu4, sediu3, sediu2
        ]
    )
    session.commit()
    session.close()
