from datetime import datetime

import pytz
from database import Base
from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String,
                        Table, Text)
from sqlalchemy.orm import relationship

utc_now = datetime.now(pytz.utc)
korea_timezone = pytz.timezone('Asia/Seoul')

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # 관리자 이름
    admin_name = Column(String(50),nullable=False)
    # 항만 위치
    port = Column(String(50),nullable=False)
    # 로그인 토큰
    token = Column(String(50),nullable=True)
    # 추가 날짜
    date = Column(DateTime, nullable=False, default=utc_now.astimezone(korea_timezone))
    # 수정 날짜
    update_date = Column(DateTime, nullable=False, default=utc_now.astimezone(korea_timezone))
    # 삭제 날짜
    delete_date = Column(DateTime, nullable=True)

class Port(Base):
    __tablename__ = "ports"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    port_location = Column(String(50),nullable=False)
    
    port_admin_count = Column(Integer,nullable=False, default=0)
    isAccident = Column(Integer,nullable=False, default=0)
    
    port_date = Column(DateTime, nullable=False, default=utc_now.astimezone(korea_timezone))
    port_update_date = Column(DateTime, nullable=False, default=utc_now.astimezone(korea_timezone))
    port_delete_date = Column(DateTime, nullable=True)
    

class Robots(Base):
    __tablename__ = "robots"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # 위치 정보
    GPS_x = Column(String(50),nullable=False)
    GPS_y = Column(String(50),nullable=False)
    GPS_z = Column(String(50),nullable=False)
    