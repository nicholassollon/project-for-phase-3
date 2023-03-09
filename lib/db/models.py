from sqlalchemy import ForeignKey, Table, Column, Integer, Float, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# clothing_stores = Table(
#     'clothing_stores',
#     Base.metadata,
#     Column('clothing_articles_id', ForeignKey('clothing_articles.id'), primary_key=True),
#     Column('store_id', ForeignKey('stores.id'), primary_key=True),
# )

# customers = Table(
#     'Customers',
#     Base.metadata,
#     Column('Customer_id', ForeignKey('customers.id'), primary_key=True),
#     Column('clothing_articles_id', ForeignKey('clothing_articles.id'), primary_key=True),
# )


class ClothingArticle(Base):
    __tablename__ = 'clothingarticles'

    id = Column(Integer(), primary_key=True)
    brand = Column(String())
    clothing_type = Column(String())
    price = Column(Float())
    store_id = Column(Integer, ForeignKey('stores.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    customer = relationship('Customer', back_populates='clothing_articles')

    def __repr__(self):
        return f'{self.clothing_type} by {self.brand}'


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    budget = Column(Float())

    clothing_articles = relationship(
        'ClothingArticle', back_populates='customer')


class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'{self.name}'
