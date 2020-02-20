from typing import List
from pydantic import BaseModel


class HostBase(BaseModel):
    dhcp_identifier: bytes
    dhcp_identifier_type: int

class HostDelete(HostBase):
    pass

class HostSearch(HostBase):
    pass

class HostCreate(HostBase):
    hostname: str
    pass

class Host(HostBase):
    host_id: int
    hostname: str

    class Config:
        orm_mode = True
