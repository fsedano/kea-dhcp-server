from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, VARBINARY
from sqlalchemy.dialects.mysql import TINYINT, BOOLEAN

SQLALCHEMY_DATABASE_URL = "mysql://root:kea_db_pass@db/kea"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

