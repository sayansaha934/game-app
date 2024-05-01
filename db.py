from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE_URL = "postgresql://postgres.isxrijcipltylpemessl:OSA2awuUjCQTpICq@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"

engine = create_engine(DATABASE_URL)
SESSION: Session = sessionmaker(bind=engine)()


#OSA2awuUjCQTpICq