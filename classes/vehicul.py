from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey

class Vehicul(Base):
    __tablename__ = 'vehicul'

    id = Column(Integer, primary_key=True)
    marca = Column(String)
    model = Column(String)
    anFabricatie = Column(String)
    instructor = relationship("Instructor", back_populates="vehicul")

    def __init__(self, marca, model, anFabricatie):
        self.marca = marca
        self.model = model
        self.anFabricatie = anFabricatie
