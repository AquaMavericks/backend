from fastapi import APIRouter,Depends
from . import robot_schema,robot_crud
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/v1/robot", tags=["Robot"])

# 로봇 전체 조회
@router.get("/view/list")
async def getAllRobot(db: Session=Depends(get_db)):
    robot_list = robot_crud.getAllRobot(db=db)
    return robot_list
# 특정 로봇 조회
@router.get("/view/detail/{robot_id}")
async def getOneRobot(robot_id:int,
                      db:Session=Depends(get_db)):
    robot = robot_crud.getOneRobot(db=db,robot_id=robot_id)
    return robot
# 로봇 생성
@router.post("/create")
async def createRobot(create_robot:robot_schema.RobotCreate,
                      db:Session=Depends(get_db)):
    result = robot_crud.createRobot(db=db,create_robot=create_robot)
    return result
# 로봇 수정
@router.put("/update")
async def updateRobot(update_robot:robot_schema.RobotUpdate,
                      db:Session=Depends(get_db)):
    result = robot_crud.modifyRobot(db=db,update_robot=update_robot)
    return result
# 로봇 삭제
@router.delete("/delete/{robot_id}")
async def deleteRobot(robot_id:int,
                      db:Session=Depends(get_db)):
    result = robot_crud.deleteRobot(db=db,delete_id=robot_id)
    return result

# 로봇 상태 변경
@router.get("/status/{robot_id}/{status}")
async def changeRobotStatus(robot_id:int,status:int,
                        db:Session=Depends(get_db)):
        result = robot_crud.changeRobotStatus(db=db,robot_id=robot_id,status=status)
        return result
# 로봇 GPS 변경
@router.get("/location/{robot_id}")
async def changeRobotLocation(robot_id:int,
                            GPS_info:robot_schema.GPSInfo,
                            db:Session=Depends(get_db)):
        result = robot_crud.changeRobotLocation(db=db,robot_id=robot_id,GPS_info=GPS_info)
        return result