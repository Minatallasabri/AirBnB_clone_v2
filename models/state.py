#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    # For FileStorage

    @property
    def cities(self):
        """
        Getter attribute that returns the list of City instances
        with state_id equals to the current State.id
        """
        from models import storage
        city_result = []
        for city in storage.all("City").values():
            if city.state_id == self.id:
                city_result.append(city)
        return city_result