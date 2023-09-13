from fastapi import APIRouter,Depends
from . import admin_crud,admin_schema
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/v1/admin", tags=["Admin"])

@router.get("/view/list")
async def viewAllPort(db:Session=Depends(get_db)):
    port_list = admin_crud.get_admin_list(db=db)
    return port_list

@router.get("/view/detail/{port_id}")
async def viewAdminDetail(port_id:int,
                         db:Session=Depends(get_db)):
    port_detail = admin_crud.get_admin_detail(db=db,port_id=port_id)
    
    if port_detail == False:
        return {"message":"해당 항만이 존재하지 않습니다."}
    else:
        return port_detail

@router.post("/create")
async def createAdmin(port:admin_schema.AdminCreate,
                     db:Session=Depends(get_db)):
    result = admin_crud.create_admin(db=db,port=port)
    return result

@router.put("/update")
async def updateAdmin(new_port:admin_schema.AdminUpdate,
                     db:Session=Depends(get_db)):
    result = admin_crud.update_admin(db=db,new_port=new_port)
    return result

@router.delete("/delete/{port_id}")
async def deleteAdmin(port_id:int,
                        db:Session=Depends(get_db)):
        result = admin_crud.delete_admin(db=db,port_id=port_id)
        return result