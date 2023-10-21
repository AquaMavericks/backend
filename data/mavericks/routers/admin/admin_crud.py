from models import Admin,Port
from . import admin_schema
from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

# 관리자 리스트 조회
def get_admin_list(db:Session) -> admin_schema.AdminList:
        
        admin_list = db.query(Admin).all()
        admin_count = len(admin_list)
        
        return_admin_list = {
            "count": admin_count,
            "admin_list": list(admin_list)
        }
        
        return return_admin_list
    
# 특정 관리자 조회
def get_admin_detail(db:Session, admin_id:int) -> Admin | bool:
    try:
        admin_detail = db.query(Admin).filter(Admin.id == admin_id).first()
    except:
        return False
    else:
        return admin_detail

# 관리자 생성
def create_admin(db:Session, admin:admin_schema.AdminCreate) -> bool:
    try:
        admin_list = get_admin_list(db=db)["admin_list"]
        
        # 관리자 Token 생성
        admin_port = db.query(Port).filter(Port.id == admin.admin_port).first()
        admin_name = admin.admin_name
        admin_token = admin_port.port_location + "_" + admin_name + "_token"
        
        for _admin in admin_list:
            if _admin.admin_name == admin_name:
                return False
            
        db_admin = Admin(
            admin_name = admin.admin_name,
            admin_token = admin_token,
            admin_port = admin.admin_port,
        )
        db.add(db_admin)
        db.commit()
    except:
        return False
    else:
        return True

# 관리자 수정
def update_admin(db:Session,
                 new_admin:admin_schema.AdminUpdate)->Admin | bool:
    try:
        old_admin = db.query(Admin).get(new_admin.admin_id)
        
        old_admin.admin_name = new_admin.admin_name
       
        old_admin.admin_port_id = new_admin.admin_port_id
        old_admin.admin_is_active = new_admin.admin_is_active
        
        db.commit()
        db.refresh(old_admin)
    except:
        return False
    else:
        return old_admin

# 관리자 삭제
def delete_admin(db:Session,port_id:int) -> bool:
    try:
        db.query(Admin).filter(Admin.admin_port_id == port_id).delete()
        db.commit()
    except:
        return False
    else:
        return True
    
# 로그인
def login(db:Session,admin_token :str):
    try:
        admin_info = db.query(Admin).filter(Admin.admin_token == admin_token).first()
    except:
        return False
    else:
        return admin_info