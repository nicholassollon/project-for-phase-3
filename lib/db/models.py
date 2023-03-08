from sqlalchemy import ForeignKey, Table, Column, Integer, Float, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ClothingArticle:
    __tablename__ = 'clothingarticles'

    id = Column(Integer(), primary_key=True)
    brand = Column(String())
    clothing_type = Column(String())
    price = Column(Float())
    store_id = Column(Integer, ForeignKey('stores.id'))
    
    customer = relationship('Customer', back_populates = 'clothing_articles')

    def __repr__(self):
        return f'{self.clothing_type} by {self.brand}' 



class Customer:
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    budget = Column(Float())
    
    clothing_articles = relationship('ClothingArticle', back_populates='customer')



class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'{self.name}'


