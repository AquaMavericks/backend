from models import Port
from . import port_schema
from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

# 항만 리스트 조회
def get_port_list(db:Session) -> port_schema.PortList:
    
    port_list = db.query(Port).all()
    port_count = len(port_list)
    
    return_port_list = {
        "count": port_count,
        "port_list": list(port_list)
    }
    
    return return_port_list

# 특정 항만 조회
def get_port_detail(db:Session, port_id:int) -> Port | bool:
    try:
        port_detail = db.query(Port).filter(Port.id == port_id).first()
    except:
        return False
    else:
        return port_detail

# 항만 생성
def create_port(db:Session, port:port_schema.PortCreate) -> bool:
    try:
        port_list = get_port_list(db=db)["port_list"]
        
        # 항만 이름 중복 제거
        for port_ in port_list:
            if port_.port_location == port.port_location:
                return False
            
        db_port = Port(
            port_location = port.port_location,
            port_admin_count = port.port_admin_count,
            isAccident = port.isAccident,
            isRescued = port.isRescued
        )
        db.add(db_port)
        db.commit()
    except:
        return False
    else:
        return True

# 항만 수정
def update_port(db:Session,new_port:port_schema.PortUpdate)->Port | bool:
    try:
        old_port = db.query(Port).get(new_port.port_id)
        
        old_port.port_location = new_port.port_location
        old_port.port_admin_count = new_port.port_admin_count
        old_port.isAccident = new_port.isAccident
        old_port.isRescued = new_port.isRescued
        
        db.commit()
        db.refresh(old_port)
        
    except:
        return False
    else:
        return old_port

# 항만 삭제
def delete_port(db:Session,port_id:int) -> bool:
    try:
        deleted_port = db.query(Port).get(port_id)
        db.delete(deleted_port)
    except:
        return False
    else:
        db.commit()
        return True
    