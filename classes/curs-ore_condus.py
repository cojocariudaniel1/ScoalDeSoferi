from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class CursOreConuds(Base):
    __tablename__ = 'curs_orecondus'

    id = Column(Integer, primary_key=True)
    idInstructor = Column(String)
    idCursant = Column(String)
    idVehicvul = Column(String)
    durata = Column(String)

    def __int__(self, durata):
        self.durata = durata
