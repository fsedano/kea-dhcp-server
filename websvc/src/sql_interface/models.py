from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, VARBINARY
from sqlalchemy.dialects.mysql import TINYINT, BOOLEAN

from .database import Base, MAC

#session = Session()

class HostIdentifierType(Base):
    __tablename__ = "host_identifier_type"
    type = Column(Integer, primary_key=True)
    name = Column(String)

class HostType(Base):
    __tablename__ = "hosts"
    host_id = Column(Integer, primary_key=True)
    hostname = Column(String)
    dhcp_identifier = Column(MAC())
    dhcp_identifier_type = Column(TINYINT(4))

