from faker import Faker
from random import random, randint, choice as rc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import ClothingArticle, Customer, Store

# Initialize faker
fake = Faker()
engine = create_engine("sqlite:///clothes_r_us.db")
session = sessionmaker(bind=engine)()

clothing_type = ["shirts", "pants", "underwear", "sweaters", ]
brand = ["Nike", "Louis Vuitton", "Gucci", "Chanel", "Adidas", "Hermès", "Zara", "H&M", "Cartier","UNIQLO"]
store_name = ["Macy\'s", "Kohls", "Gabe\'s", "JC Penny"]




def make_clothing():

    print("Making clothes...")
    clothing = ClothingArticle(
        brand= brand[randint(0, len(brand))],
        clothing_type=clothing_type[randint(0, len(clothing_type)-1)],
        store_id=None,
        price= randint(0, 75))
    session.add(clothing)
    session.commit()
    return clothing

def make_store():

    print("Building Store...")
    stores = Store (
        id = None,
        name = store_name[randint(0,len(store_name)-1)]
        )
    session.add(stores)
    session.commit()
    return stores

def make_customer():
    print ("Welcoming Customer...")
    customer = Customer (
    name = fake.name(),
    budget = randint(200, 500)
    ) 
    session.add(customer)
    session.commit()
    return customer


def clear_all_data(): 
    print("Clearing Data...")
    session.query(ClothingArticle).delete()
    session.query(Store).delete()
    session.query(Customer).delete()
    session.commit()
    

def refresh_all_data():
    clear_all_data()
    for i in range(20):
        make_clothing()*i
    for i in range(5):
        make_store()*i
    for i in range (3):
        make_customer()*i
        
if __name__ == '__main__':
    refresh_all_data()

