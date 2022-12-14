from base import Session, Base, engine
from cont import Cont
from cursant import Cursant
from instructor import Instructor
from pachet_ore import PachetOre

from personal import Personal
from personal_administrativ import PersonalAdministrativ
from programare import Programare
from sediu import Sediu
from address import Address
from vehicul import Vehicul


def unitest1():
    session = Session()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    print("I. Adaugarea de de date in DB")
    # I. Adaugarea de de date in DB
    adress_alexandru = Address('Sos. Nationala', 'Iasi', 'Romania', 700103, 'Iasi')

    sediu_alexandru = Sediu('0230562526', 'dsrp.alexandru@gmail.com')

    sediu_alexandru.address = adress_alexandru

    personal_alexandru1 = Personal("Ghiata", "Anamaria")
    personal_alexandru2 = Personal("Abaza", "Andreea")
    personal_alexandru1.cont = Cont("personal1", "parola123", 2)
    personal_alexandru2.cont = Cont("personal2", "parola123", 2)
    personal_alexandru3 = Personal("Hongu", "Cosmin")
    personal_alexandru3.cont = Cont("personal3", "parola1", 2)

    sediu_alexandru.personal = [personal_alexandru1, personal_alexandru2, personal_alexandru3]

    # metoda 1
    print("Metoda 1")
    print(f"Sediul {sediu_alexandru.denumire_sediu} "
          f"la adresa: {sediu_alexandru.address.strada} "
          f" {sediu_alexandru.personal[0].nume}"
          f" {sediu_alexandru.personal[0].prenume}",
          f" {sediu_alexandru.personal[1].nume}"
          f" {sediu_alexandru.personal[1].prenume}"
          f" {sediu_alexandru.personal[2].nume}"
          f" {sediu_alexandru.personal[2].prenume}"
          )
    print("\n")

    # Metoda 2
    print("Metoda 2")
    # Deoarece avem mai multi personal intr-un anumit sediu
    # Printare tot personalul dintr-un anumit sediu
    personal_list = []

    for personal in sediu_alexandru.personal:
        personal_list.append(f"{personal.nume} {personal.prenume}")

    print(f"In sediul {sediu_alexandru.denumire_sediu}se afla personalul:",
          f"".join([
              f" {personal.nume + ' ' + personal.prenume},"
              for personal in sediu_alexandru.personal
          ]),
          f"la addresa {adress_alexandru.strada}")
    # Adaugarea datelo in db
    session.add(sediu_alexandru)
    session.commit()
    session.close()


def unitest2():
    print("\n")
    print("II. Editarea unei valori din baza de date:")
    session = Session()
    # II. Editarea unei valori din baza de date:
    # Schimbarea numelui unui personal

    # Folosim .first() petru a selecta primul obiect deoarece o sa avem un singur obiect de tip personal si sa nu mai
    # fie nevoie de a itera asupra unei liste de personal. Initial la un query se returneaza o lista de elemente
    # chiar daca este doar unul singur.
    personal_ghiata = session.query(Personal).where(Personal.nume == "Ghiata", Personal.prenume == "Anamaria").first()
    personal_ghiata.nume = "Lex"
    personal_ghiata.prenume = "Anca"

    # Facem commit la date in baza de date.
    session.commit()

    # Facem print pentru a verifica daca schimbarea a avut loc.

    sediu = session.query(Sediu).first()
    print(
        f"In sediul {sediu.denumire_sediu} se afla personalul",
        f" ".join([f"{personal.nume + ' ' + personal.prenume}," for personal in sediu.personal]),
        f"la adresa {sediu.address.strada}"
    )


def unitest3():
    print("\n")
    print("III. Stergerea unui personal dintr-una numit sediu din baza de date")

    session = Session()

    # Folosim first deoarece avem un singur element intr-o lista de elemente pentru a evita folosirea unei iteratii.
    personal = session.query(Personal).where(Personal.nume == "Lex", Personal.prenume == "Anca").first()
    sediu = session.query(Sediu).first()
    # A fost sters doar din sediu | Un copil a fost sters din claas parinte
    sediu.personal.remove(personal)

    # Deoarece este o relatie many2many este necesar stergerea datelor de tip copil.
    # Personalul a fost sters direct din baza de date
    session.query(Personal).where(Personal.nume == "Lex", Personal.prenume == "Anca").delete()

    session.commit()
    session.close()

    sediu = session.query(Sediu).first()
    print(
        f"In sediul {sediu.denumire_sediu} se afla personalul",
        f" ".join([f"{personal.nume + ' ' + personal.prenume}," for personal in sediu.personal]),
        f"la adresa {sediu.address.strada}"
    )


unitest1()
unitest2()
unitest3()
