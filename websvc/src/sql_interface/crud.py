from sqlalchemy.orm import Session

from . import models, schemas

def get_hosts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.HostType).offset(skip).limit(limit).all()

def create_host(db: Session, host: schemas.HostCreate):
    db_host = models.HostType(
        hostname=host.hostname,
        dhcp_identifier_type=host.dhcp_identifier_type,
        dhcp_identifier=bytes.fromhex(host.dhcp_identifier))
    db.add(db_host)
    db.commit()
    db.refresh(db_host)
    return db_host