import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

#Leer variables de entorno
load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_DIALECT = os.getenv('DB_DIALECT')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')

#tipo de bd, mediante modulo pymysql, usuario, contraseña, host, nombre bd
#mysql+pymysql://root:12345@GlobalPartsDB/GlobalPartsDB
URL_CONNECTION = '{}://{}:{}@{}/{}'.format(DB_DIALECT, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

engine = create_engine(URL_CONNECTION)

#autoflush no actualiza bd despues de commit, autocommit no hace commit automatico
localsesion = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

#dependencia para obtener la sesion de la bd y cerrarla
def get_db():
    db = localsesion()
    try:
        yield db
    finally:
        db.close()