from base import Session
from sqlalchemy import select

from cont import Cont
from personal import Personal
from cont import Cont
from instructor import Instructor
from personal import Personal
from sediu import Sediu
from address import Address
from cursant import Cursant
from vehicul import Vehicul
from pachet_ore import PachetOre


def get_info(username):
    session = Session()
    query = session.query(Cont).filter(Cont.user == username)
    for cont in query:
        if cont.nivel_cont == 0:
            cursant_query = session.query(Cursant).filter(Cursant.cont_id == cont.id)
            for item in cursant_query:
                return [item.nume, item.prenume, item.dataNasterii]
        elif cont.nivel_cont == 1:
            pass
        elif cont.nivel_cont == 2:
            pass


