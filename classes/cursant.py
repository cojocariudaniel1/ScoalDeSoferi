from sqlalchemy.orm import relationship, validates
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Cursant(Base):
    __tablename__ = 'cursant'

    id = Column(Integer, primary_key=True)
    nume = Column(String)
    prenume = Column(String)
    dataNasterii = Column(Date)
    pachet_ore = relationship("PachetOre")
    pachet_ore_id = Column(Integer, ForeignKey("pachet_ore.id"))
    instructor = relationship("Instructor")
    instructor_id = Column(Integer, ForeignKey("instructor.id"))
    nr_ore = Column(Integer)
    ore_finalizate = Column(Integer)

    programare = relationship("Programare")
    # Atributul back_populates este folosit pentru ca engine-ul sa inteleaga ca este o relatie si sa
    # populeze automatat clasa copil cand clasa parinte este creata.
    # One To One
    cont = relationship("Cont", back_populates="cursant")
    cont_id = Column(Integer, ForeignKey("cont.id"))

    #setare getters & setters
    def __init__(self, nume, prenume, dataNasterii, nr_ore=0, ore_finalizate=0):
        self.nume = nume
        self.prenume = prenume
        self.dataNasterii = dataNasterii
        self.ore_finalizate = ore_finalizate
        self.nr_ore = nr_ore


