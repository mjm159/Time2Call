import os
import sys
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
    '''
    Defines the 'person' table for each person who is being tracked in Time2Call
    
    rows:
    =============
    id: primary, string (uuid), generated, not Null
    name: string, not Null
    phone: string, not Null
    last_called: Date,
    call_freq: number, not Null
    '''
    __tablename__ = 'person'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    last_called = Column(Date, nullable=True)
    call_freq = Column(Integer, nullable=False)

# Create an engine that staores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

