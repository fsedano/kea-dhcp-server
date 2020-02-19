from typing import List
from pydantic import BaseModel


class HostBase(BaseModel):
    dhcp_identifier: str
    dhcp_identifier_type: int
    hostname: str

class HostCreate(HostBase):
    pass

class Host(HostBase):
    host_id: int
    class Config:
        orm_mode = True
