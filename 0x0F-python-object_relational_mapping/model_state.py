#!/usr/bin/python3
"""Module that contains the clasand an instance"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """LOOOOL"""
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column("name", String(128), nullable=False)
