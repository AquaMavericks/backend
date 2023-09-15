from models import Robots
from . import robot_schema
from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_

# 전체 리스트 조회
def getAllRobot(db: Session)-> robot_schema.RobotList:
    robot_list = db.query(Robots).all()
    response_robot_list = {
        "count": len(robot_list),
        "robots": robot_list
    }
    return response_robot_list

# 특정 로봇 조회
def getOneRobot(db: Session, robot_id: int)-> robot_schema.Robot:
    robot = db.query(Robots).get(robot_id)
    return robot

# 로봇 생성
def createRobot(db:Session, create_robot:robot_schema.RobotCreate) -> bool:
    created_robot = Robots(
            robots_port = create_robot.robots_port,
            GPS_x = create_robot.GPS_x,
            GPS_y = create_robot.GPS_y,
            GPS_z = create_robot.GPS_z,
            robots_status = create_robot.robots_status
        )
    print(created_robot.robots_port)
    print(created_robot.GPS_x)
    print(created_robot.GPS_y)
    print(created_robot.GPS_z)
    print(created_robot.robots_status)
    
    db.add(created_robot)
    db.commit()
    db.refresh(created_robot)
    return True
    
# 로봇 수정
def modifyRobot(db:Session, update_robot:robot_schema.RobotUpdate) -> bool:
    try:
        updated_robot = db.query(Robots).get(update_robot.robot_id)
        updated_robot.robot_port = update_robot.updated_robot.robot_port
        updated_robot.GPS_x = update_robot.updated_robot.GPS_x
        updated_robot.GPS_y = update_robot.updated_robot.GPS_y
        updated_robot.GPS_z = update_robot.updated_robot.GPS_z
        updated_robot.robots_status = update_robot.updated_robot.robots_status
        db.commit()
        db.refresh(updated_robot)
    except:
        return False
    else:
        return True

# 로봇 삭제
def deleteRobot(db:Session, delete_id : robot_schema.RobotDelete) -> bool:
    try:
        deleted_robot = db.query(Robots).get(delete_id.robot_id)
        db.delete(deleted_robot)
        db.commit()
    except:
        return False
    else:
        return True
    
# 로봇 상태 변경
def changeRobotStatus(db:Session, robot_id:int, status:int) -> bool:
    try:
        robot = db.query(Robots).get(robot_id)
        robot.robots_status = status
        db.commit()
        db.refresh(robot)
    except:
        return False
    else:
        return True

# 로봇 GPS 변경
def changeRobotLocation(db:Session,robot_id:int,GPS_info:robot_schema.GPSInfo)->bool:
    try:
        robot = db.query(Robots).get(robot_id)
        robot.GPS_x = GPS_info.GPS_x
        robot.GPS_y = GPS_info.GPS_y
        robot.GPS_z = GPS_info.GPS_z
        db.commit()
        db.refresh(robot)
    except:
        return False
    else:
        return True