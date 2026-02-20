from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from database import Base
from datetime import datetime


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


class Bestellung(Base):
    __tablename__ = "bestellungen"
    
    id = Column(Integer, primary_key=True, index=True)
    benutzer_id = Column(Integer, ForeignKey("benutzer.id"))
    produkt_id = Column(Integer, ForeignKey("produkte.id"))
    anzahl = Column(Integer, default=1)
    gesamtpreis = Column(Float)
    status = Column(String, default="offen")  # offen, in_zubereitung, fertig, geliefert
    erstellt_am = Column(DateTime, default=datetime.utcnow)
