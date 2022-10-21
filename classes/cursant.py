from sqlalchemy.orm import relationship
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
    nr_ore = Column(Integer)
    cont = relationship("Cont", back_populates="cursant")
    cont_id = Column(Integer, ForeignKey("cont.id"))

    def __init__(self, nume, prenume, dataNasterii):
        self.nume = nume
        self.prenume = prenume
        self.dataNasterii = dataNasterii
