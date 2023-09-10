from pydantic import BaseModel, validator
from sqlalchemy import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

class Admin(BaseModel):
    admin_name :str
    admin_token : str
    admin_port : int
    class Config:
        orm_mode = True

class AdminList(BaseModel):
    count: int
    admin_list: list[Admin]

class AdminCreate(BaseModel):
    admin_name : str
    admin_port : int
    @validator('admin_name','admin_port')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class AdminUpdate(AdminCreate):
    admin_id : int
    
    @validator('admin_id')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class AdminDelete(BaseModel):
    admin_id : int
    
    @validator('admin_id')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v