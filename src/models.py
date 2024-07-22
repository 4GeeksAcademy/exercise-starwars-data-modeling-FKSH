import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

    character_favs = relationship('character_fav', back_populates='user')
    planet_favs = relationship('planet_fav', back_populates='user')
    starship_favs = relationship('starship_fav', back_populates='user')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Float, nullable=False)
    mass = Column(Float, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

    character_favs = relationship('character_fav', back_populates='character')

class Character_Fav(Base):
    __tablename__ = 'character_fav'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

    user = relationship('user', back_populates='character_favs')
    character = relationship('character', back_populates='character_favs')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    gravity = Column(Float, nullable=False)
    diameter = Column(Float, nullable=False)
    surface_water = Column(Float, nullable=False)
    rotation_period = Column(Float, nullable=False)

    planet_favs = relationship('planet_fav', back_populates='planet')

class Planet_Fav(Base):
    __tablename__ = 'planet_fav'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

    user = relationship('user', back_populates='planet_favs')
    planet = relationship('planet', back_populates='planet_favs')

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    length = Column(Float, nullable=False)
    crew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(Float, nullable=False)
    hyperdrive_rating = Column(Float, nullable=False)

    starship_favs = relationship('starship_fav', back_populates='starship')

class Starship_Fav(Base):
    __tablename__ = 'starship_fav'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))

    user = relationship('user', back_populates='starship_favs')
    starship = relationship('starship', back_populates='starship_favs')

def to_dict(self):
    return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
