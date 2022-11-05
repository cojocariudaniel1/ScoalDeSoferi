from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from base import Base, Session
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class Sediu(Base):
    __tablename__ = 'sediu'

    # Many To Many
    personal_relationship = Table('personal_relationship', Base.metadata,
                                  Column('personal_id', Integer, ForeignKey('personal.id')),
                                  Column('sediu_id', Integer, ForeignKey('sediu.id')),

                                  )
    id = Column(Integer, primary_key=True)
    numarTelefon = Column(Integer)
    emailAddress = Column(String)
    denumire_sediu = Column(String)
    # Atributul back_populates este folosit pentru ca engine-ul sa inteleaga ca este o relatie si sa
    # populeze automatat clasa copil cand clasa parinte este creata.
    address = relationship("Address", back_populates="sediu")
    address_id = Column(Integer, ForeignKey("address.id"))
    personal = relationship('Personal', secondary=personal_relationship)

    #setare getters & setters
    def __init__(self, numarTelefon, emailAddress, denumire_sediu = "Scoala de soferi"):
        self.numarTelefon = numarTelefon
        self.emailAddress = emailAddress
        self.denumire_sediu = denumire_sediu

    @hybrid_property
    def email(self):
        return self.emailAddress

    @email.setter
    def email(self, email):
        self.emailAddress = email
