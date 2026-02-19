# Git-Anleitung für Meikel

Hier lernst du Schritt für Schritt, wie du am Projekt mitarbeitest.

## Schritt 1: Repository herunterladen (nur einmalig)

Terminal öffnen und eingeben:

```bash
cd Documents
git clone https://github.com/danialahmed2207/bella-napoli-backend.git
```

Dann wechseln in den Projektordner:

```bash
cd bella-napoli-backend
```

## Schritt 2: Aktuelle Version holen

**Wichtig:** Das machst du immer ZUERST, bevor du anfängst zu arbeiten:

```bash
git pull
```

## Schritt 3: Datei bearbeiten

Öffne z. B. `models.py` in deinem Editor.

Mache deine Änderungen.

Speichern mit Strg+S (oder Cmd+S auf Mac).

## Schritt 4: Änderungen vorbereiten

Sage Git, welche Dateien du committen möchtest:

```bash
git add models.py
```

Oder für alle geänderten Dateien:

```bash
git add .
```

## Schritt 5: Commit erstellen

Schreibe eine kurze Nachricht, was du gemacht hast:

```bash
git commit -m "feat: neue Tabelle für Bestellungen erstellt"
```

## Schritt 6: Hochladen

```bash
git push
```

Fertig! Deine Änderungen sind jetzt online.

---

## Commit-Bezeichnungen (immer klein schreiben)

| Bezeichnung | Bedeutung | Beispiel |
|-------------|-----------|----------|
| feat: | Feature / Neue Funktion | `feat: Login hinzugefügt` |
| fix: | Fehler behoben | `fix: Passwort-Check korrigiert` |
| docs: | Dokumentation | `docs: Kommentare ergänzt` |
| chore: | Aufräumen | `chore: alte Dateien gelöscht` |

## Kommentare im Code

Kommentare helfen anderen zu verstehen, was der Code macht.

**Einzeilig:**

```python
# Hier wird das Passwort geprüft
if password == "123":
    pass
```

**Mehrzeilig:**

```python
def berechne_preis(pizza, extras):
    """
    Berechnet den Gesamtpreis einer Pizza.
    
    Parameter:
        pizza: Der Pizza-Name
        extras: Liste der Zusatzstoffe
    
    Rückgabe:
        Der Preis als Zahl
    """
    return preis
```

## Nützliche Befehle

**Status checken:**

```bash
git status
```

**Was habe ich geändert?**

```bash
git diff
```

**Commit-Verlauf ansehen:**

```bash
git log --oneline
```

---

## Beispiel-Ablauf für einen Tag

```bash
# 1. Aktuelle Version holen
git pull

# 2. Arbeiten (Dateien bearbeiten)

# 3. Änderungen anzeigen lassen
git status

# 4. Dateien zum Commit hinzufügen
git add .

# 5. Commit mit Nachricht
git commit -m "feat: neue Route für Getränke"

# 6. Hochladen
git push
```

---

## Falls etwas schiefgeht

**Fehler: "Please tell me who you are"**

Dann einmalig deinen Namen und E-Mail setzen:

```bash
git config --global user.name "Meikel"
git config --global user.email "meikel@beispiel.de"
```

**Fehler: "Merge conflict"**

Frag im Team nach – das lösen wir gemeinsam.

---

Viel Erfolg! 🍕
