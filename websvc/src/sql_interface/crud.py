from sqlalchemy.orm import Session

from . import models, schemas

def get_hosts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.HostType).offset(skip).limit(limit).all()

def create_host(db: Session, host: schemas.HostCreate):
    db_host = models.HostType(
        hostname=host.hostname,
        dhcp_identifier_type=host.dhcp_identifier_type,
        dhcp_identifier=host.dhcp_identifier)
    host = db.query(models.HostType).filter(
        models.HostType.dhcp_identifier == host.dhcp_identifier,
        models.HostType.dhcp_identifier_type == host.dhcp_identifier_type).first()
    if host:
        return None
    db.add(db_host)
    db.commit()
    db.refresh(db_host)
    return db_host

def delete_host(db: Session, host: schemas.HostDelete):
    host = db.query(models.HostType).filter(
        models.HostType.dhcp_identifier == host.dhcp_identifier,
        models.HostType.dhcp_identifier_type == host.dhcp_identifier_type).first()
    if host:
        db.delete(host)
        db.commit()
    return host

def search_host(db: Session, dhcp_identifier: str, dhcp_identifier_type: int):
    host = db.query(models.HostType).filter(
        models.HostType.dhcp_identifier == dhcp_identifier,
        models.HostType.dhcp_identifier_type == dhcp_identifier_type).first()
    return host
