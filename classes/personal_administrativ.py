from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class PersonalAdministrativ(Base):
    __tablename__ = 'personaladministrativ'

    id = Column(Integer, primary_key=True)
    personal = relationship("Personal", back_populates="personaladministrativ")
    personal_id = Column(Integer, ForeignKey("personal.id"))
    cont = relationship("Cont", back_populates="personaladministrativ")
    cont_id = Column(Integer, ForeignKey("cont.id"))