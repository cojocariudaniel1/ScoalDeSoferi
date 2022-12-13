from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Vehicul(Base):
    __tablename__ = 'vehicul'

    id = Column(Integer, primary_key=True)
    marca = Column(String)
    model = Column(String)
    anFabricatie = Column(String)
    cutie_de_viteze = Column(String)
    numar_de_inmatriculare = Column(String)
    # Atributul back_populates este folosit pentru ca engine-ul sa inteleaga ca este o relatie si sa
    # populeze automatat clasa copil cand clasa parinte este creata.
    instructor = relationship("Instructor", back_populates="vehicul")

    # setare getters & setters
    def __init__(self, marca, model, anFabricatie, cutie_de_viteze, numar_de_inmatriculare):
        self.marca = marca
        self.model = model
        self.anFabricatie = anFabricatie
        self.cutie_de_viteze = cutie_de_viteze
        self.numar_de_inmatriculare = numar_de_inmatriculare
