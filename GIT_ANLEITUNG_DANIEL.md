# Git-Anleitung für Daniel

Hier lernst du, wie du am Projekt mitarbeiten kannst.

## 1. Repository das erste Mal herunterladen

Öffne das Terminal und gib ein:

```bash
cd Desktop
git clone https://github.com/danialahmed2207/bella-napoli-backend.git
```

Dann in den Ordner wechseln:

```bash
cd bella-napoli-backend
```

## 2. Neue Änderungen holen (immer vor dem Arbeiten!)

```bash
git pull
```

Das lädt die neuesten Änderungen von den anderen herunter.

## 3. Eine Datei bearbeiten

Öffne die Datei in VS Code oder einem anderen Editor.

Zum Beispiel `main.py` ändern.

## 4. Änderungen speichern (Commit)

Schritt A – Datei zum Commit vormerken:

```bash
git add main.py
```

Oder alle Dateien auf einmal:

```bash
git add .
```

Schritt B – Commit erstellen mit Nachricht:

```bash
git commit -m "feat: Beschreibung was du gemacht hast"
```

## 5. Änderungen hochladen

```bash
git push
```

## 6. Wichtige Commit-Bezeichnungen

| Bezeichnung | Wann benutzen? |
|-------------|----------------|
| feat: | Neue Funktion hinzugefügt |
| fix: | Fehler behoben |
| docs: | README oder Kommentare geändert |
| chore: | Kleinere Aufräumarbeiten |

Beispiele:

```bash
git commit -m "feat: Login-Seite erstellt"
git commit -m "fix: Datenbank-Fehler behoben"
git commit -m "docs: README aktualisiert"
```

## 7. Kommentare im Code schreiben

So schreibst du Kommentare in Python:

```python
# Das ist ein einzeiliger Kommentar

"""
Das ist ein mehrzeiliger Kommentar.
Hier kannst du erklären, was die Funktion macht.
"""

def meine_funktion():
    # Erklärung was passiert
    pass
```

## 8. Status prüfen

```bash
git status
```

Zeigt dir, welche Dateien geändert wurden.

## 9. Deine Änderungen ansehen

```bash
git diff
```

Zeigt dir genau, was du geändert hast.

---

## Checkliste vor jedem Commit

- [ ] `git pull` gemacht?
- [ ] Dateien bearbeitet?
- [ ] `git add .` ausgeführt?
- [ ] `git commit -m "..."` geschrieben?
- [ ] `git push` ausgeführt?

---

Fragen? Einfach im Team fragen!
