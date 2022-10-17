from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Sediu(Base):
    __tablename__ = 'sediu'

    personal_relationship = Table('personal_relationship', Base.metadata,
                                  Column('personal_id', Integer, ForeignKey('personal.id')),
                                  Column('sediu_id', Integer, ForeignKey('sediu.id')),

                                  )
    id = Column(Integer, primary_key=True)
    numarTelefon = Column(Integer)
    emailAddress = Column(String)
    address = relationship("Address", back_populates="sediu")
    address_id = Column(Integer, ForeignKey("address.id"))
    personal = relationship('Personal', secondary=personal_relationship)


    # idPersonal = Column(String)

    def __init__(self, numarTelefon, emailAddress):
        self.numarTelefon = numarTelefon
        self.emailAddress = emailAddress