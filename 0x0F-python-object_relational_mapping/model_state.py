#!/usr/bin/python3
"""azezeaezaee"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_city import City

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column("name", String(128), nullable=False)
