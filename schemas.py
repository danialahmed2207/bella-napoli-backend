from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Produkt-Schemas
class ProduktBase(BaseModel):
    name: str
    beschreibung: Optional[str] = None
    preis: float
    kategorie: str
    verfuegbar: bool = True


class ProduktCreate(ProduktBase):
    pass


class Produkt(ProduktBase):
    id: int
    
    class Config:
        from_attributes = True


# Benutzer-Schemas
class BenutzerBase(BaseModel):
    username: str
    email: str


class BenutzerCreate(BenutzerBase):
    password: str


class Benutzer(BenutzerBase):
    id: int
    ist_admin: bool
    
    class Config:
        from_attributes = True


# Login-Schema
class LoginRequest(BaseModel):
    username: str
    password: str


# Bestellung-Schemas
class BestellungBase(BaseModel):
    produkt_id: int
    anzahl: int = 1


class BestellungCreate(BestellungBase):
    pass


class Bestellung(BestellungBase):
    id: int
    benutzer_id: int
    gesamtpreis: float
    status: str
    erstellt_am: datetime
    
    class Config:
        from_attributes = True
