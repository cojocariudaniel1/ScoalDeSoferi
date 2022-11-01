from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Instructor(Base):
    __tablename__ = 'instructor'

    id = Column(Integer, primary_key=True)

    #One to One toate
    personal = relationship("Personal", back_populates="instructor")
    personal_id = Column(Integer, ForeignKey("personal.id"))
    vehicul = relationship("Vehicul", back_populates="instructor")
    vehicul_id = Column(Integer, ForeignKey("vehicul.id"))
    cont = relationship("Cont", back_populates="instructor")
    cont_id = Column(Integer, ForeignKey("cont.id"))
