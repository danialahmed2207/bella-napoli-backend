import pytest
from fastapi.testclient import TestClient
from main import app
from database import get_db, SessionLocal
from models import Base, Produkt, Benutzer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Test-Datenbank
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


@pytest.fixture(scope="function")
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_root(setup_db):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Willkommen bei Bella Napoli!"}


def test_create_produkt(setup_db):
    response = client.post("/produkte", json={
        "name": "Margherita",
        "beschreibung": "Klassische Pizza",
        "preis": 8.50,
        "kategorie": "Pizza",
        "verfuegbar": True
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Margherita"
    assert data["preis"] == 8.50


def test_get_produkte(setup_db):
    # Erst ein Produkt erstellen
    client.post("/produkte", json={
        "name": "Salami",
        "beschreibung": "Mit Salami",
        "preis": 9.50,
        "kategorie": "Pizza",
        "verfuegbar": True
    })
    
    response = client.get("/produkte")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Salami"


def test_register(setup_db):
    response = client.post("/register", json={
        "username": "testuser",
        "email": "test@test.de",
        "password": "test123"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@test.de"


def test_login(setup_db):
    # Erst registrieren
    client.post("/register", json={
        "username": "loginuser",
        "email": "login@test.de",
        "password": "login123"
    })
    
    # Dann einloggen
    response = client.post("/login", json={
        "username": "loginuser",
        "password": "login123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
