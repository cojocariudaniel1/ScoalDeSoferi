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
from sqlalchemy import update

# Doar un test
def test():
    session = Session()

    cursant = session.query(Cursant).filter(Cursant.id == 1).first()
    pachet_ore = session.query(PachetOre).filter(PachetOre.id == 1).first()

    smt = update(Cursant).where(Cursant.id == cursant.id).values(ore_id=pachet_ore.id)
    smt1 = update(Cursant).where(Cursant.id == cursant.id).values(nr_ore=pachet_ore.durata)
    session.execute(smt)
    session.execute(smt1)
    session.commit()
    session.close()


test()
