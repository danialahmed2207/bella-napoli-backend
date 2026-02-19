import requests
import json

BASE_URL = "http://localhost:8000"


def main():
    print("=== Bella Napoli API Client ===\n")
    
    while True:
        print("1. Alle Produkte anzeigen")
        print("2. Einzelnes Produkt anzeigen")
        print("3. Neues Produkt erstellen")
        print("4. Produkt löschen")
        print("5. Login")
        print("6. Register")
        print("0. Beenden")
        
        choice = input("\nWahl: ")
        
        if choice == "1":
            get_all_products()
        elif choice == "2":
            get_single_product()
        elif choice == "3":
            create_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            login()
        elif choice == "6":
            register()
        elif choice == "0":
            break
        else:
            print("Ungültige Eingabe!\n")


def get_all_products():
    try:
        response = requests.get(f"{BASE_URL}/produkte")
        if response.status_code == 200:
            products = response.json()
            print("\n--- Produkte ---")
            for p in products:
                print(f"{p['id']}: {p['name']} - {p['preis']}€")
            print()
        else:
            print(f"Fehler: {response.status_code}\n")
    except Exception as e:
        print(f"Fehler: {e}\n")


def get_single_product():
    try:
        product_id = input("Produkt-ID: ")
        response = requests.get(f"{BASE_URL}/produkte/{product_id}")
        if response.status_code == 200:
            p = response.json()
            print(f"\nName: {p['name']}")
            print(f"Beschreibung: {p['beschreibung']}")
            print(f"Preis: {p['preis']}€")
            print(f"Kategorie: {p['kategorie']}")
            print(f"Verfügbar: {p['verfuegbar']}\n")
        else:
            print(f"Fehler: {response.status_code}\n")
    except Exception as e:
        print(f"Fehler: {e}\n")


def create_product():
    try:
        print("\nNeues Produkt:")
        name = input("Name: ")
        beschreibung = input("Beschreibung: ")
        preis = float(input("Preis: "))
        kategorie = input("Kategorie (Pizza/Getränk/Dessert): ")
        
        data = {
            "name": name,
            "beschreibung": beschreibung,
            "preis": preis,
            "kategorie": kategorie,
            "verfuegbar": True
        }
        
        response = requests.post(f"{BASE_URL}/produkte", json=data)
        if response.status_code == 200:
            print("Produkt erstellt!\n")
        else:
            print(f"Fehler: {response.status_code}\n")
    except Exception as e:
        print(f"Fehler: {e}\n")


def delete_product():
    try:
        product_id = input("Produkt-ID zum Löschen: ")
        response = requests.delete(f"{BASE_URL}/produkte/{product_id}")
        if response.status_code == 200:
            print("Produkt gelöscht!\n")
        else:
            print(f"Fehler: {response.status_code}\n")
    except Exception as e:
        print(f"Fehler: {e}\n")


def login():
    try:
        print("\nLogin:")
        username = input("Username: ")
        password = input("Passwort: ")
        
        data = {
            "username": username,
            "password": password
        }
        
        response = requests.post(f"{BASE_URL}/login", json=data)
        if response.status_code == 200:
            result = response.json()
            print(f"Login erfolgreich! Token: {result['access_token'][:20]}...\n")
        else:
            print(f"Fehler: {response.status_code}\n")
    except Exception as e:
        print(f"Fehler: {e}\n")


def register():
    try:
        print("\nRegister:")
        username = input("Username: ")
        email = input("E-Mail: ")
        password = input("Passwort: ")
        
        data = {
            "username": username,
            "email": email,
            "password": password
        }
        
        response = requests.post(f"{BASE_URL}/register", json=data)
        if response.status_code == 200:
            print("Registrierung erfolgreich!\n")
        else:
            print(f"Fehler: {response.status_code}\n")
    except Exception as e:
        print(f"Fehler: {e}\n")


if __name__ == "__main__":
    main()
