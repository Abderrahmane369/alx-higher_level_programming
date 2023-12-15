#!/usr/bin/env python3
"""Module that contains the clasand an instance"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """LOOOOL"""
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column("name", String(128), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name
