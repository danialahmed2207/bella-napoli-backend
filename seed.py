import requests

BASE_URL = "http://localhost:8000"


def main():
    print("=== Demo-Daten erstellen ===\n")
    
    # Produkte anlegen
    produkte = [
        {
            "name": "Margherita",
            "beschreibung": "Klassisch mit Tomate und Mozzarella",
            "preis": 8.50,
            "kategorie": "Pizza",
            "verfuegbar": True
        },
        {
            "name": "Salami",
            "beschreibung": "Mit würziger Salami",
            "preis": 9.50,
            "kategorie": "Pizza",
            "verfuegbar": True
        },
        {
            "name": "Funghi",
            "beschreibung": "Mit frischen Champignons",
            "preis": 9.00,
            "kategorie": "Pizza",
            "verfuegbar": True
        },
        {
            "name": "Cola",
            "beschreibung": "0,5l Flasche",
            "preis": 3.00,
            "kategorie": "Getränk",
            "verfuegbar": True
        },
        {
            "name": "Tiramisu",
            "beschreibung": "Hausgemacht",
            "preis": 5.50,
            "kategorie": "Dessert",
            "verfuegbar": True
        }
    ]
    
    print("Lege Produkte an...")
    for p in produkte:
        try:
            response = requests.post(f"{BASE_URL}/produkte", json=p)
            if response.status_code == 200:
                print(f"  ✓ {p['name']} erstellt")
            else:
                print(f"  ✗ {p['name']} fehlgeschlagen")
        except Exception as e:
            print(f"  ✗ Fehler: {e}")
    
    # Test-Benutzer anlegen
    print("\nLege Test-Benutzer an...")
    benutzer = {
        "username": "testuser",
        "email": "test@pizza.de",
        "password": "test123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/register", json=benutzer)
        if response.status_code == 200:
            print(f"  ✓ Benutzer '{benutzer['username']}' erstellt")
        else:
            print(f"  ✗ Benutzer konnte nicht erstellt werden")
    except Exception as e:
        print(f"  ✗ Fehler: {e}")
    
    print("\n=== Fertig! ===")
    print("Starte jetzt den Client mit: python client.py")


if __name__ == "__main__":
    main()
