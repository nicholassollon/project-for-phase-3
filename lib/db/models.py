from sqlalchemy import ForeignKey, Table, Column, Integer, Float, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ClothingArticle:
    __tablename__ = 'clothingarticles'

    id = Column(Integer(), primary_key=True)
    brand = Column(String())
    clothing_type = Column(String())
    sizes = Column(String())
    store_id = Column(Integer, ForeignKey('stores.id'))

    def __repr__(self):
        return f'{self.clothing_type} by {self.brand}'

class Customer:
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    budget = Column(Float())
    closet = Column(Integer(), ForeignKey('closets.id'))

    closet = relationship('Closet', backref=backref('customer'))


class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    max_price = Column(Float)

    def __repr__(self):
        return f'{self.name}'


class Closet:
    __tablename__ = 'closets'

    id = Column(Integer(), primary_key=True)
    clothes = Column(Integer(), ForeignKey('clothingarticles.id'))

    def __repr__(self):
        return f'{self.id}'
