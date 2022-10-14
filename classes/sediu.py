from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Sediu(Base):
    __tablename__ = 'sediu'

    id = Column(Integer, primary_key=True)
    idSediu = Column(String)
    numarTelefon = Column(Integer)
    emailAddress = Column(String)

    def __init__(self, idSediu, numarTelefon, emailAddress):
        self.idSediu = idSediu
        self.numarTelefon = numarTelefon
        self.emailAddress = emailAddress