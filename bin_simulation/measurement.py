from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, REAL, Date
#from sqlalchemy import Sequence


Base = declarative_base()

class Measurement(Base):
    __tablename__ = "pomair"
    id = Column(Integer, primary_key=True)
    id_czujnik = Column(Integer)
    measurments = Column(REAL)
    czas_pomiaru = Column(Date)

    def __repr__(self):
        return f"<Measurement(id_czujnik='{self.id_czujnik}', measurements='{self.measurments}', czas_pomiaru='{self.czas_pomiaru}')>"
