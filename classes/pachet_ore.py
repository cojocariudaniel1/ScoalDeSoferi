from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey

# Pachete 30 ore
# Un singur pachet la cursant / Nu poate sa cumpere alte pachete
#  30 ore obligatorii
#  Pachete de o ora / {multiple pachete}


class PachetOre(Base):
    __tablename__ = 'pachet_ore'

    id = Column(Integer, primary_key=True)
    durata = Column(Integer)
    instructor_id = Column(Integer, ForeignKey("instructor.id"))
    instructor = relationship("Instructor", back_populates="pachet_ore")

    def __init__(self, durata):
        self.durata = durata
