from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey


class PersonalAdministrativ(Base):
    __tablename__ = 'personaladministrativ'

    id = Column(Integer, primary_key=True)
