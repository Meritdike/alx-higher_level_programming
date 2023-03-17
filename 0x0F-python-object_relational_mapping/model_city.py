#!/usr/bin/python3
""" contains the class definition of a State and an instance
Base = declarative_base() """

from model_state import State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ City class inheriting from Base """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("State.id"), nullable=False)
