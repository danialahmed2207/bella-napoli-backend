# Bella Napoli Backend

Pizzeria-Verwaltungssystem mit FastAPI und SQLite.

## Projektbeschreibung

Dieses Projekt ist ein Backend für eine Pizzeria. Es verwaltet Produkte (Pizzen, Getränke) und bietet ein einfaches Login-System.

## API-Übersicht

| Methode | Endpunkt | Beschreibung |
|---------|----------|--------------|
| POST | /register | Benutzer registrieren |
| POST | /login | Benutzer einloggen |
| GET | /produkte | Alle Produkte anzeigen |
| GET | /produkte/{id} | Einzelnes Produkt anzeigen |
| POST | /produkte | Neues Produkt erstellen |
| PUT | /produkte/{id} | Produkt aktualisieren |
| DELETE | /produkte/{id} | Produkt löschen |
| POST | /bestellungen | Neue Bestellung erstellen |
| GET | /bestellungen | Alle Bestellungen anzeigen |
| PUT | /bestellungen/{id} | Bestellstatus aktualisieren |

## Installation

```bash
pip install -r requirements.txt
```

## Starten

```bash
uvicorn main:app --reload
```

## Tagesdokumentation

### Tag 1 (17.02.2026)
- Projekt initialisiert
- README erstellt
- requirements.txt erstellt

### Tag 2 (18.02.2026)
- Datenbank erstellt
- Modelle für Produkte und Benutzer
- Schemas mit Pydantic

### Tag 3 (19.02.2026)
- CRUD Endpunkte für Produkte
- Response models vergessen -> nachgeholt

### Tag 4 (20.02.2026)
- Login-System mit JWT
- Passwort-Hashing mit bcrypt
- Register/Login Endpunkte
- E-Mail Prüfung vergessen -> nachgeholt

### Tag 5 (21.02.2026)
- Python Client-Skript erstellt
- Menü zum Testen der API
- Update-Funktion vergessen -> nachgeholt

## Woche 1 Zusammenfassung
- ✅ CRUD-API für Produkte
- ✅ SQLite Datenbank
- ✅ Login-System mit JWT
- ✅ Python Client zum Testen

## Woche 2

### Tag 6 (24.02.2026)
- Tests mit pytest hinzugefügt
- pytest vergessen in requirements -> nachgeholt

### Tag 7 (25.02.2026)
- Bestellungen-System hinzugefügt
- Model, Schema und Endpunkte
- API-Doku vergessen zu aktualisieren -> nachgeholt

### Tag 8 (26.02.2026)
- Client um Bestellungen erweitert
- Doppelte Konvertierung gefixt

## Tests ausführen

```bash
pytest test_api.py -v
```
