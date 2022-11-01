from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Personal(Base):
    __tablename__ = 'personal'

    id = Column(Integer, primary_key=True)
    nume = Column(String)
    prenume = Column(String)
    cont = relationship("Cont", back_populates="personal")
    cont_id = Column(Integer, ForeignKey("cont.id"))
    instructor = relationship("Instructor", back_populates="personal", uselist = False)
    personaladministrativ = relationship("PersonalAdministrativ", back_populates="personal", uselist = False)

    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume