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
- Git-Anleitungen für Teammitglieder hinzugefügt
