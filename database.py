from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite Datenbank-Datei
SQLALCHEMY_DATABASE_URL = "sqlite:///./bella_napoli.db"

# Engine erstellen
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session-Factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Basis-Klasse für Modelle
Base = declarative_base()


# Hilfsfunktion für Datenbank-Sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
