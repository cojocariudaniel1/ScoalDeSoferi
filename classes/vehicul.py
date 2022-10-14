from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey

class Vehicul(Base):
    __tablename__ = 'vehicul'

    id = Column(Integer, primary_key=True)
    id_vehicul = Column(String)
    marca = Column(String)
    model = Column(String)
    anFabricatie = Column(Date)

    def __init__(self, id_vehicul, marca, model, anFabricatie):
        self.id_vehicul = id_vehicul
        self.marca = marca
        self.model = model
        self.anFabricatie = anFabricatie
