#!/usr/bin/python3
"""
a python file that contains the class definition
of a City and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """
    Class with id, name, and state_id attributes of each city
    """
    __tablename__ = 'cities'
    id = Column(
        Integer,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
