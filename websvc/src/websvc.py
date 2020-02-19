from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_interface import crud, models, schemas
from sql_interface.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
#print("Hosts:")
#id = 0x010203040506
#host = HostType(hostname="pepe3", dhcp_identifier=id.to_bytes(128, 'big'), dhcp_identifier_type = 0)
#session.add(host)
#session.commit()


#u = session.query(HostType).filter(HostType.hostname=="pepe2")
#u.delete()
#session.commit()

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/hosts/", response_model=List[schemas.Host])
def read_hosts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_hosts(db, skip=skip, limit=limit)
    return users

@app.post("/hosts/", response_model=schemas.Host)
def create_host(host: schemas.HostCreate, db: Session = Depends(get_db)):
    return crud.create_host(db=db, host=host)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/host-reservation")
def get_reservations():
    #return session.query(HostIdentifierType)
    return {'a':'b'}

@app.get("/host-reservation/{reservation_mac}")
def get_reservation(reservation_mac):
    #return session.query(HostIdentifierType)
    return {'a':reservation_mac}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}