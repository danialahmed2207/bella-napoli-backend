from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database
import models
import schemas
import auth

app = FastAPI(title="Bella Napoli API")

# Datenbank-Tabellen erstellen
models.Base.metadata.create_all(bind=database.engine)


@app.get("/")
def root():
    return {"message": "Willkommen bei Bella Napoli!"}


# Benutzer registrieren
@app.post("/register", response_model=schemas.Benutzer)
def register(benutzer: schemas.BenutzerCreate, db: Session = Depends(database.get_db)):
    # Prüfen ob Username schon existiert
    db_user = db.query(models.Benutzer).filter(models.Benutzer.username == benutzer.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username schon vergeben")
    
    # Prüfen ob E-Mail schon existiert
    db_email = db.query(models.Benutzer).filter(models.Benutzer.email == benutzer.email).first()
    if db_email:
        raise HTTPException(status_code=400, detail="E-Mail schon vergeben")
    
    # Passwort hashen
    hashed_pw = auth.hash_password(benutzer.password)
    
    # Neuen Benutzer erstellen
    db_benutzer = models.Benutzer(
        username=benutzer.username,
        email=benutzer.email,
        password_hash=hashed_pw
    )
    db.add(db_benutzer)
    db.commit()
    db.refresh(db_benutzer)
    return db_benutzer


# Login
@app.post("/login")
def login(login_data: schemas.LoginRequest, db: Session = Depends(database.get_db)):
    user = auth.authenticate_user(db, login_data.username, login_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Falscher Username oder Passwort")
    
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# Alle Produkte anzeigen
@app.get("/produkte", response_model=list[schemas.Produkt])
def get_produkte(db: Session = Depends(database.get_db)):
    produkte = db.query(models.Produkt).all()
    return produkte


# Einzelnes Produkt anzeigen
@app.get("/produkte/{produkt_id}", response_model=schemas.Produkt)
def get_produkt(produkt_id: int, db: Session = Depends(database.get_db)):
    produkt = db.query(models.Produkt).filter(models.Produkt.id == produkt_id).first()
    if not produkt:
        raise HTTPException(status_code=404, detail="Produkt nicht gefunden")
    return produkt


# Neues Produkt erstellen
@app.post("/produkte", response_model=schemas.Produkt)
def create_produkt(produkt: schemas.ProduktCreate, db: Session = Depends(database.get_db)):
    db_produkt = models.Produkt(**produkt.dict())
    db.add(db_produkt)
    db.commit()
    db.refresh(db_produkt)
    return db_produkt


# Produkt aktualisieren
@app.put("/produkte/{produkt_id}", response_model=schemas.Produkt)
def update_produkt(produkt_id: int, produkt: schemas.ProduktCreate, db: Session = Depends(database.get_db)):
    db_produkt = db.query(models.Produkt).filter(models.Produkt.id == produkt_id).first()
    if not db_produkt:
        raise HTTPException(status_code=404, detail="Produkt nicht gefunden")
    
    for key, value in produkt.dict().items():
        setattr(db_produkt, key, value)
    
    db.commit()
    db.refresh(db_produkt)
    return db_produkt


# Produkt löschen
@app.delete("/produkte/{produkt_id}")
def delete_produkt(produkt_id: int, db: Session = Depends(database.get_db)):
    db_produkt = db.query(models.Produkt).filter(models.Produkt.id == produkt_id).first()
    if not db_produkt:
        raise HTTPException(status_code=404, detail="Produkt nicht gefunden")
    
    db.delete(db_produkt)
    db.commit()
    return {"message": f"Produkt {produkt_id} wurde erfolgreich gelöscht"}


# Bestellung erstellen
@app.post("/bestellungen", response_model=schemas.Bestellung)
def create_bestellung(bestellung: schemas.BestellungCreate, benutzer_id: int, db: Session = Depends(database.get_db)):
    # Produkt finden für Preis
    produkt = db.query(models.Produkt).filter(models.Produkt.id == bestellung.produkt_id).first()
    if not produkt:
        raise HTTPException(status_code=404, detail="Produkt nicht gefunden")
    
    gesamtpreis = produkt.preis * bestellung.anzahl
    
    db_bestellung = models.Bestellung(
        benutzer_id=benutzer_id,
        produkt_id=bestellung.produkt_id,
        anzahl=bestellung.anzahl,
        gesamtpreis=gesamtpreis
    )
    db.add(db_bestellung)
    db.commit()
    db.refresh(db_bestellung)
    return db_bestellung


# Alle Bestellungen anzeigen
@app.get("/bestellungen", response_model=list[schemas.Bestellung])
def get_bestellungen(db: Session = Depends(database.get_db)):
    bestellungen = db.query(models.Bestellung).all()
    return bestellungen


# Bestellung aktualisieren (Status ändern)
@app.put("/bestellungen/{bestellung_id}", response_model=schemas.Bestellung)
def update_bestellung(bestellung_id: int, status: str, db: Session = Depends(database.get_db)):
    db_bestellung = db.query(models.Bestellung).filter(models.Bestellung.id == bestellung_id).first()
    if not db_bestellung:
        raise HTTPException(status_code=404, detail="Bestellung nicht gefunden")
    
    db_bestellung.status = status
    db.commit()
    db.refresh(db_bestellung)
    return db_bestellung
