from fastapi import APIRouter,Depends
from . import port_crud,port_schema
from database import get_db
from sqlalchemy.orm import Session
router = APIRouter(prefix="/v1/port", tags=["Port"])

# 항만 리스트 조회
@router.get("/view/list")
async def viewAllPort(db:Session=Depends(get_db)):
    port_list = port_crud.get_port_list(db=db)
    return port_list

# 특정 항만 조회
@router.get("/view/detail/{port_id}")
async def viewPortDetail(port_id:int,
                         db:Session=Depends(get_db)):
    port_detail = port_crud.get_port_detail(db=db,port_id=port_id)
    
    if port_detail == False:
        return {"message":"해당 항만이 존재하지 않습니다."}
    else:
        return port_detail

# 항만 생성
@router.post("/create")
async def createPort(port:port_schema.PortCreate,
                     db:Session=Depends(get_db)):
    result = port_crud.create_port(db=db,port=port)
    return result

# 항만 수정
@router.put("/update")
async def updatePort(new_port:port_schema.PortUpdate,
                     db:Session=Depends(get_db)):
    result = port_crud.update_port(db=db,new_port=new_port)
    return result

# 항만 삭제
@router.delete("/delete/{port_id}")
async def deletePort(port_id:int,
                     db:Session=Depends(get_db)):
    result = port_crud.delete_port(db=db,port_id=port_id)
    return result

# 항만 사고 발생 여부 변경
@router.get("/accident/{port_id}/{status}")
async def changeAccidentStatus(port_id:int,status:int,
                            db:Session=Depends(get_db)):
        result = port_crud.changeAccidentStatus(db=db,port_id=port_id,status=status)
        return result
    
# 항만 구조 여부 변경
@router.get("/rescue/{port_id}/{status}")
async def changeRescueStatus(port_id:int,status:int,
                            db:Session=Depends(get_db)):
        result = port_crud.changeRescueStatus(db=db,port_id=port_id,status=status)
        return result