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
    
    # 로그인 토큰
    admin_token = Column(String(50),nullable=True)
    
    # 항만 정보 FK ex) 0: 부산항
    admin_port = Column(String(50),nullable=False)
    
    # 추가 날짜
    date = Column(DateTime, nullable=False, default=utc_now.astimezone(korea_timezone))
    
    # 수정 날짜
    update_date = Column(DateTime, nullable=False, default=utc_now.astimezone(korea_timezone))
    
    # 삭제 날짜
    delete_date = Column(DateTime, nullable=True)

class Port(Base):
    __tablename__ = "ports"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # 항만 위치 ex) 부산항
    port_location = Column(String(50),nullable=False)
    
    # 항만 관리자 수 ex) 1명
    port_admin_count = Column(Integer,nullable=False, default=0)
    
    # 항만 사고발생여부 ex) 0: 사고발생X, 1: 사고발생O
    isAccident = Column(Integer,nullable=False, default=0)
    
    # 항만 구조여부 ex) 0: 구조X, 1: 구조O
    isRescued = Column(Integer,nullable=False, default=0)
    
    # 항만 날짜 정보 ex) 2020-01-01
    port_date = Column(DateTime, nullable=False, default=utc_now.astimezone(korea_timezone))
    port_update_date = Column(DateTime, nullable=False, default=utc_now.astimezone(korea_timezone))
    port_delete_date = Column(DateTime, nullable=True)
    

class Robots(Base):
    __tablename__ = "robots"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # 항만
    robots_port = Column(String(50),nullable=False)
    # 위치 정보
    GPS_x = Column(String(50),nullable=False)
    GPS_y = Column(String(50),nullable=False)
    GPS_z = Column(String(50),nullable=False)
    # 구조상태
    # 0 : 구조대기, 1 : 구조중, 2 : 구조완료
    robots_status = Column(Integer,nullable=False, default=0)