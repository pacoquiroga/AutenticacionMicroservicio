import time
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = f"{os.getenv('DB_DIALECT')}://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Intentar conectarse a la base de datos con reintentos
while True:
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        print("Connected to the database")
        connection.close()
        break
    except Exception as e:
        print(f"Database connection failed: {e}")
        print("Retrying in 5 seconds...")
        time.sleep(5)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de la bd y cerrarla
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
