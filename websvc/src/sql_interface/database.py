from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, VARBINARY
from sqlalchemy.dialects.mysql import TINYINT, BOOLEAN
from sqlalchemy.types import TypeDecorator
import sqlalchemy.types as types

SQLALCHEMY_DATABASE_URL = "mysql://root:kea_db_pass@127.0.0.1/kea"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class MAC(TypeDecorator):
    impl = types.VARBINARY
    def process_result_value(self, value, dialect):
        if value is None:
            return value
        return value.hex()
    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        return bytes.fromhex(value.decode())

