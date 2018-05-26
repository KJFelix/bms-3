from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
import settings

engine = create_engine(URL(**settings.DATABASE))
Session = sessionmaker(bind=engine)

Base = declarative_base()
