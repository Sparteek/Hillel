from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = (
    "postgresql+psycopg://"
    "teacher:super_password@localhost:5432/education_platform"
)

engine = create_engine(DATABASE_URL)

Base = declarative_base()
Session = sessionmaker(bind=engine)
