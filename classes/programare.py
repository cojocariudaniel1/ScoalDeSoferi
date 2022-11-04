from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Programare(Base):
    __tablename__ = 'programare'

    id = Column(Integer, primary_key=True)
    data = Column(Date)
    ora = Column(Integer)
    cursant = relationship("Cursant", back_populates="programare")
    cursant_id = Column(Integer, ForeignKey("cursant.id"))
    instructor = relationship("Instructor", back_populates="programare")
    instructor_id = Column(Integer, ForeignKey("instructor.id"))

    def __init__(self, data, ora=None):
        self.data = data
        self.ora = ora
