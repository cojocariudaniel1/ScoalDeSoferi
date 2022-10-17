from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class CursOreConuds(Base):
    __tablename__ = 'ore'

    id = Column(Integer, primary_key=True)
    Instructor = Column(String)
    cursant = Column(String)
    durata = Column(String)

    def __int__(self, durata):
        self.durata = durata
