from pydantic import BaseModel
from typing import Optional


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
