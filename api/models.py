from sqlalchemy import Column, Integer, String, Date, Float
from database import Base

class Prisionero(Base):
    __tablename__ = "prisioneros"

    id = Column(Integer, primary_key=True, index=True)
    fecha_publicacion = Column(Date, index=True)
    pais_prision = Column(String, index=True)
    consulado = Column(String)
    delito = Column(String, index=True)
    extraditado = Column(String)
    situacion_juridica = Column(String)
    genero = Column(String)
    grupo_edad = Column(String)
    cantidad = Column(Integer)
    latitud = Column(Float, index=True)
    longitud = Column(Float, index=True)
