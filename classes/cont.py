from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey  # Import library sql


class Cont(Base):
    __tablename__ = 'cont'

    id = Column(Integer, primary_key=True)
    user = Column(String)
    parola = Column(String)
    nivel_cont = Column(Integer)  # Nivel 1 - User, 2 - Instructor, 3 - Administrator
    personal = relationship("Personal", back_populates="cont")
    instructor = relationship("Instructor", back_populates="cont")
    cursant = relationship("Cursant", back_populates="cont")

    def __init__(self, user, parola, nivel_cont):
        self.user = user
        self.parola = parola
        self.nivel_cont = nivel_cont
