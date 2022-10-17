from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Cursant(Base):
    __tablename__ = 'cursant'

    id = Column(Integer, primary_key=True)
    idCursant = Column(String)
    nume = Column(String)
    prenume = Column(String)
    dataNasterii = Column(Date)


    def __int__(self, idCursant, nume, prenume, dataNasterii):
        self.idCursant = idCursant
        self.nume = nume
        self.prenume = prenume
        self.dataNasterii = dataNasterii
