from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, VARBINARY
from sqlalchemy.dialects.mysql import TINYINT, BOOLEAN

SQLALCHEMY_DATABASE_URL = "mysql://root:kea_db_pass@127.0.0.1/keatest"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

session = Session()

class HostIdentifierType(Base):
    __tablename__ = "host_identifier_type"
    type = Column(Integer, primary_key=True)
    name = Column(String)

class HostType(Base):
    __tablename__ = "hosts"
    host_id = Column(Integer, primary_key=True)
    hostname = Column(String)
    dhcp_identifier = Column(VARBINARY(length=128))
    dhcp_identifier_type = Column(TINYINT(4))


for instance in session.query(HostIdentifierType):
    print(instance.type)
    print(instance.name)

print("Hosts:")
id = 0x010203040506
host = HostType(hostname="pepe3", dhcp_identifier=id.to_bytes(128, 'big'), dhcp_identifier_type = 0)
session.add(host)
session.commit()


u = session.query(HostType).filter(HostType.hostname=="pepe2")
u.delete()
session.commit()

for host in session.query(HostType):
    print(host.host_id)
    print(host.hostname)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}