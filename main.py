from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database
import models
import schemas

app = FastAPI(title="Bella Napoli API")

# Datenbank-Tabellen erstellen
models.Base.metadata.create_all(bind=database.engine)


@app.get("/")
def root():
    return {"message": "Willkommen bei Bella Napoli!"}


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
    return {"message": "Produkt gelöscht"}
