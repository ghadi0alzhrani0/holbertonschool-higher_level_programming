#!/usr/bin/python3
"""Defines the City model using SQLAlchemy."""

from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """Represents the cities table in a MySQL database."""

    __tablename__ = "cities"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
