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
def read_hosts(skip: int = 0, rnd: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_hosts(db, skip=skip, limit=limit)
    print(f"Users is {users[0].dhcp_identifier}")
    return users

@app.post("/hosts/", response_model=schemas.Host)
def create_host(host: schemas.HostCreate, db: Session = Depends(get_db)):
    host = crud.create_host(db=db, host=host)
    if not host:
        raise HTTPException(status_code=409, detail="Duplicate host")
    return host

@app.delete("/hosts/", response_model=schemas.Host)
def delete_host(host: schemas.HostDelete, db: Session = Depends(get_db)):
    host = crud.delete_host(db=db, host=host)
    if not host:
        raise HTTPException(status_code=404, detail="Host not found")
    return host


@app.get("/host/", response_model=schemas.Host)
def get_host( dhcp_identifier_type: int, dhcp_identifier: str,  db: Session = Depends(get_db)):
    host = crud.search_host(db=db, dhcp_identifier=dhcp_identifier, dhcp_identifier_type=dhcp_identifier_type)
    if not host:
        raise HTTPException(status_code=404, detail="Host not found")
    return host


