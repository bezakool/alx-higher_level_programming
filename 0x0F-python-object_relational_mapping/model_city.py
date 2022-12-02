#!/usr/bin/python3
"""
a python file that contains the class definition
of a City and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """
    Class with id, name, and state_id attributes of each city
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
