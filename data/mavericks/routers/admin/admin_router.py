from fastapi import APIRouter,Depends
from . import admin_crud,admin_schema
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/v1/admin", tags=["Admin"])

@router.get("/view/list")
async def viewAllPort(db:Session=Depends(get_db)):
    port_list = admin_crud.get_admin_list(db=db)
    return port_list

@router.get("/view/detail/{admin_id}")
async def viewAdminDetail(admin_id:int,
                         db:Session=Depends(get_db)):
    port_detail = admin_crud.get_admin_detail(db=db,admin_id=admin_id)
    
    if port_detail == False:
        return {"message":"해당 항만이 존재하지 않습니다."}
    else:
        return port_detail
    
@router.post("/login")
async def login(admin_token: str,
                db:Session=Depends(get_db)):
    admin = admin_crud.login(db=db, admin_token=admin_token)
    if admin == False:
        return "로그인 실패"
    return f"로그인 성공. 환영합니다. {admin.admin_port}"

@router.post("/create")
async def createAdmin(admin:admin_schema.AdminCreate,
                     db:Session=Depends(get_db)):
    result = admin_crud.create_admin(db=db,admin=admin)
    return result

@router.put("/update")
async def updateAdmin(new_port:admin_schema.AdminUpdate,
                     db:Session=Depends(get_db)):
    result = admin_crud.update_admin(db=db,new_port=new_port)
    return result

@router.delete("/delete/{admin_id}")
async def deleteAdmin(admin_id:int,
                        db:Session=Depends(get_db)):
        result = admin_crud.delete_admin(db=db,admin_id=admin_id)
        return result