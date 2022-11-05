from sqlalchemy.orm import relationship, validates
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey  # Import library sql


class Cont(Base):
    __tablename__ = 'cont'

    id = Column(Integer, primary_key=True)
    user = Column(String)
    parola = Column(String)
    nivel_cont = Column(Integer, nullable=False)  # Nivel 0 - User, 1 - Instructor, 2 - Personal, 3 - Administrator

    # Atributul back_populates este folosit pentru ca engine-ul sa inteleaga ca este o relatie si sa
    # populeze automatat clasa copil cand clasa parinte este creata.
    # One To One
    personal = relationship("Personal", back_populates="cont", uselist=False)
    # One To One
    instructor = relationship("Instructor", back_populates="cont", uselist=False)
    # One To One
    cursant = relationship("Cursant", back_populates="cont", uselist=False)
    # One To One
    personaladministrativ = relationship("PersonalAdministrativ", back_populates="cont", uselist=False)

    # setare getters & setters
    def __init__(self, user, parola, nivel_cont):
        self.user = user
        self.parola = parola
        self.nivel_cont = nivel_cont


    @validates("nivel_cont")
    def validate_ora(self, key, nivel_cont):
        if nivel_cont not in [0, 1, 2, 3]:
            raise ValueError("Nivelul contului nu se incadreaza in ierarhia actuala, eg: \n"
                             "Nivel 0 -> User \n"
                             "Nivel 1 -> Instructor \n"
                             "Nivel 2 -> Personal \n"
                             "Nivel 3 -> Administrator \n" )
        return nivel_cont