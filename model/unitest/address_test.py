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


def address_test():

    adress_alexandru = Address('Sos. Nationala', 'Iasi', 'Romania', 700103, 'Iasi')

    sediu_alexandru = Sediu('0230562526', 'dsrp.alexandru@gmail.com')

    sediu_alexandru.address = adress_alexandru

    personal_alexandru1 = Personal("Ghiata", "Anamaria")
    personal_alexandru2 = Personal("Ghiata11", "Anamaria11")

    sediu_alexandru.personal = [personal_alexandru1, personal_alexandru2]

    print(f"Sediul {sediu_alexandru.id}, se afla personalul "
          f"{sediu_alexandru.personal[0].nume} {sediu_alexandru.personal[0].prenume} la adresa: {sediu_alexandru.address.strada} ")

    personal_list = []
    for personal in sediu_alexandru.personal:
        personal_list.append(personal.nume)
        personal_list.append(personal.prenume)

    #Functie de transformare a listei in string
    listToStr = ' '.join([str(elem) for elem in personal_list])
    print(personal_list)
    print(f"In sediul: {sediu_alexandru.id} se afla personalul: {str(listToStr)}")

address_test()