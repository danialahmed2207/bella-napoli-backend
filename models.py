from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class Produkt(Base):
    __tablename__ = "produkte"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    beschreibung = Column(String)
    preis = Column(Float)
    kategorie = Column(String)  # z.B. "Pizza", "Getränk", "Dessert"
    verfuegbar = Column(Boolean, default=True)


class Benutzer(Base):
    __tablename__ = "benutzer"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    ist_admin = Column(Boolean, default=False)
