from sqlalchemy.orm import relationship
from base import Base
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey

# Pachete 30 ore
# Un singur pachet la cursant / Nu poate sa cumpere alte pachete
#  30 ore obligatorii
#  Pachete de o ora / {multiple pachete}

class PachetOre(Base):
    __tablename__ = 'pachet_ore'
#MANY TO MANY
    instructor_pachet_ore_relationship = Table('instructor_pachet_ore_relationship', Base.metadata,
                                    Column('instructor_id', Integer, ForeignKey('instructor.id')),
                                    Column('pachet_ore_id', Integer, ForeignKey('pachet_ore.id')),

                                    )

    id = Column(Integer, primary_key=True)
    durata = Column(Integer)
    pret = Column(Integer)
    instructor = relationship('Instructor', secondary=instructor_pachet_ore_relationship)

    def __init__(self, durata, pret):
        self.durata = durata
        self.pret = pret