from pydantic import BaseModel, Field, validator
from models import Port
class Robot(BaseModel):
    robots_port: int
    
    GPS_x: str
    GPS_y: str
    GPS_z: str
    
    robots_status: int
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "robots_port": 1,
                "GPS_x": "1",
                "GPS_y": "1",
                "GPS_z": "1",
                "robots_status": 0,
            },
        }

class RobotList(BaseModel):
    count : int
    robots : list[Robot]

class RobotCreate(BaseModel):
    robots_port : int
    GPS_x : str
    GPS_y : str
    GPS_z : str
    robots_status : int

class RobotUpdate(RobotCreate):
    robot_id:int
    updated_robot:Robot
    
class RobotDelete(BaseModel):
    robot_id:int
    
class GPSInfo(BaseModel):
    GPS_X:str
    GPS_Y:str
    GPS_Z:str