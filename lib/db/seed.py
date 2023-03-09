from random import random, randint, choice as rc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import ClothingArticle, Customer, Store

# Initialize faker
# fake = Faker()
engine = create_engine("sqlite:///project-for-phase-3.db")
session = sessionmaker(bind=engine)()

clothing_type = ["shirts", "pants", "underwear", "sweaters", ]
brand = ["Nike", "Louis Vuitton", "Gucci", "Chanel",
         "Adidas", "Hermès", "Zara", "H&M", "Cartier", "UNIQLO"]
store_names = ["Macy\'s", "Kohls", "Gabe\'s", "JC Penny"]


def make_clothing(id):

    print("Making clothes...")
    clothing = ClothingArticle(
        brand=brand[randint(0, len(brand)-1)],
        clothing_type=clothing_type[randint(0, len(clothing_type)-1)],
        store_id=id,
        price=randint(0, 75))
    session.add(clothing)
    session.commit()
    return clothing


def make_store():

    print("Building Store...")
    
    for id in range(1,len(store_names)):
        store = Store(
            name=store_names[id]
        )
        for i in range(20):
            make_clothing(id)
        session.add(store)
        session.commit()


def make_customer():
    print("Welcoming Customers...")
    customer = Customer(
        name="Tyler",
        budget=randint(200, 500)
    )
    session.add(customer)
    customer2 = Customer(
        name="Eleanor",
        budget=randint(200, 500)
    )
    session.add(customer2)
    customer3 = Customer(
        name="Gehrig",
        budget=randint(20000, 50000)
    )
    session.add(customer3)
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
    make_store()
    make_customer()


if __name__ == '__main__':
    refresh_all_data()
