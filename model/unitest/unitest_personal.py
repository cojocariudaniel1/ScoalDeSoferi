import unittest
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


class Test(unittest.TestCase):
    personal_nume = []
    personal_prenume = []
    personal_obj = []

    def test_0_set_name(self):
        print("Start set_name, set_prenume test\n")
        """
        Any method which starts with ``test_`` will considered as a test case.
        """
        for i in range(4):
            # initialize a name
            nume = 'nume' + str(i)
            prenume = 'prenume' + str(i)
            # store the name into the list variable
            self.personal_nume.append(nume)
            self.personal_prenume.append(prenume)

            # Set personal
            personal = Personal(nume, prenume)
            self.personal_obj.append(personal)

            # check if the obtained nume, prenume is string or not
            self.assertTrue(self.string_check(self.personal_nume[i]))
            self.assertTrue(self.string_check(self.personal_prenume[i]))
            self.assertIsNotNone(personal)

        print("nume length = ", len(self.personal_nume))
        print(self.personal_nume)
        print("prenume length = ", len(self.personal_prenume))
        print(self.personal_prenume)
        print(self.personal_obj)
        print("\nFinish set_nume, set_prenume test\n")

    def test_1_get_name(self):
        print("\nStart get_nume, get_prenume test\n")
        """
        Any method that starts with ``test_`` will be considered as a test case.
        """
        length = len(self.personal_nume)  # total number of stored user information
        print("personal nume length = ", length)
        print("personal_prenume length = ", len(self.personal_prenume))
        for i in range(6):
            # if i not exceed total length then verify the returned name
            if i < length:
                # if the two name not matches it will fail the test case
                self.assertEqual(self.personal_nume[i], self.personal_obj[i].nume)
            else:
                print("Testing for get_nume, get_prenume no personal test")
                # if length exceeds then check the 'no such user' type message\
                try:
                    nume = self.personal_obj[i].nume
                    prenume = self.personal_obj[i].prenume
                except:
                    nume = "There is no such personal"
                    prenume = "There is no such personal"
                self.assertEqual('There is no such personal', nume)
                self.assertEqual('There is no such personal', prenume)
        print("\nFinish get_nume, get_prenume test\n")

    def string_check(self, var):
        return isinstance(var, str)



