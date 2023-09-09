from sqlalchemy import create_engine, MetaData,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import dotenv
import os
# .env
dotenv.load_dotenv()
IP = os.getenv('IP')
PORT = os.getenv('PORT')
MYSQL_PORT = os.getenv('MYSQL_PORT')
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def reset_auto_increment():
    import pymysql
    conn = pymysql.connect(
            host= IP,
            port=int(MYSQL_PORT),
            user=USER,
            password=PASSWORD,
            db=DATABASE,
            charset="utf8"
        )
    db = conn.cursor()

    # 테이블 목록 가져오기
    script = "SHOW TABLES;"
    db.execute(script)
    tables = db.fetchall()

    try:
        # 각 테이블에 대해 Auto Increment 초기화 및 재정렬
        for table in tables:
            table_name = table[0]
            if table_name == "alembic_version":
                continue
            script1 = f"ALTER TABLE {table_name} AUTO_INCREMENT=1;"
            script2=f"SET @COUNT = 0;"
            script3=f"UPDATE {table_name} SET id = @COUNT:=@COUNT+1;"
            db.execute(script1)
            db.execute(script2)
            db.execute(script3)
        conn.commit()
        db.close()
        conn.close()
        print("Auto Increment Reset Complete")
    except Exception as e:
        print(e)
        db.close()
        conn.close()
    finally:
        print("Close()")
