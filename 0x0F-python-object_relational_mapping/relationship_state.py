#!/usr/bin/python3
"""
a python file that contains the class definition
of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

my_metadata = MetaData()
Base = declarative_base(metadata=my_metadata)


class State(Base):
    """
    Class with id, name, and state_id attributes of each city
    """
    __tablename__ = 'states'
    id = Column(
        Integer,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(128),
        nullable=False
    )
    cities = relationship('City', backref='states')
