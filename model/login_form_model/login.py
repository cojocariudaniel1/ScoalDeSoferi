from base import Session
from sqlalchemy import select

from cont import Cont
from personal import Personal
from instructor import Instructor
from sediu import Sediu
from address import Address
from cursant import Cursant
from vehicul import Vehicul
from pachet_ore import PachetOre


def login_check(username, password):
    session = Session()
    try:
        query = session.query(Cont).filter(Cont.user == username, Cont.parola == password)
        count = 0
        for row in query:
            if row.user:
                count += 1
        if count == 1:
            print("Login succesful")
            return True
        else:
            print("Failed")

    except Exception as e:
        print(e)
    session.commit()
    session.close()


