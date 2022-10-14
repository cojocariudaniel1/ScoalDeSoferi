from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Personal(Base):
    __tablename__ = 'personal'

    id = Column(Integer, primary_key=True)
    idPersonal = Column(String)
    nume = Column(String)
    prenume = Column(String)

    def __init__(self, idPersonal, nume, prenume):
        self.idPersonal = idPersonal
        self.nume = nume
        self.prenume = prenume
