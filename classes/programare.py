from sqlalchemy.orm import relationship, validates
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

    @validates("ora")
    def validate_ora(self, key, ora):
        if ora is not None:
            if ora > 16:
                raise ValueError("Ora programata este peste program")
            if (ora % 2) != 0:
                raise ValueError("Ora programata este gresita")
            return ora
