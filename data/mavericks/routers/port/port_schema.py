from pydantic import BaseModel, validator
from sqlalchemy.sql.sqltypes import DateTime

class Port(BaseModel):
    port_location: str
    port_admin_count: int
    isAccident: int
    isRescued: int
    port_date: str
    class Config:
        orm_mode = True

class PortList(BaseModel):
    count: int
    port_list: list[Port]

class PortCreate(BaseModel):
    port_location: str
    port_admin_count: int = 0
    isAccident: int = 0
    isRescued: int = 0 
    
    @validator('port_location')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class PortUpdate(PortCreate):
    port_id : int
    
    @validator('port_id')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class PortDelete(BaseModel):
    port_id : int
    
    @validator('port_id')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v