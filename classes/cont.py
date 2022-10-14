from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Cont(Base):
    __tablename__ = 'cont'

    id = Column(Integer, primary_key=True)
    idCont = Column(String)
    user = Column(String)
    parola = Column(String)

    def __init__(self, idCont, user, parola):
        self.idCont = idCont
        self.user = user
        self.parola = parola
