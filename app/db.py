import os
from sqlalchemy.orm import sessionmaker, declarative_base

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", data.db))
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread" : False},
    echo = False,
    future=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)
Base=declarative_base()


