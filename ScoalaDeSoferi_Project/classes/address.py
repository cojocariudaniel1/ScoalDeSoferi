from sqlalchemy.orm import relationship, validates
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey

#Column (Atribut de tip coloana)
class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    strada = Column(String)
    oras = Column(String)
    tara = Column(String)
    cod_postal = Column(Integer)
    judet = Column(String)

    # One to One relationship
    sediu = relationship("Sediu", back_populates="address", uselist=False)


    #Validare cod postal
    @validates("cod_postal")
    def validate_codPostal(self, key, cod_postal):
        if len(str(cod_postal)) != 6:
            raise ValueError("Codul postal nu este corect")
        return cod_postal

    #setare getters & setters
    def __init__(self, strada, oras, tara, cod_postal, judet):
        self.strada = strada
        self.oras = oras
        self.tara = tara
        self.cod_postal = cod_postal
        self.judet = judet