from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    strada = Column(String)
    oras = Column(String)
    tara = Column(String)
    cod_postal = Column(Integer)
    judet = Column(String)

    # One to One
    sediu = relationship("Sediu", back_populates="address", uselist=False)

    def __init__(self, strada, oras, tara, cod_postal, judet):
        self.strada = strada
        self.oras = oras
        self.tara = tara
        self.cod_postal = cod_postal
        self.judet = judet