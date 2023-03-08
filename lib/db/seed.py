from faker import Faker
from random import random, randint, choice as rc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import ClothingArticle, Customer, Store, Closet

# Initialize faker
fake = Faker()
engine = create_engine("sqlite:///clothes_r_us.db")
session = sessionmaker(bind=engine)()

location = ["New York", "Pennsylvania", "DC"]
clothing_type = ["shirts", "pants", "underwear", "sweaters", ]
size = ["x-small", "small", "medium", "large", "x-large"]
brand = ["Nike", "Louis Vuitton", "Gucci", "Chanel", "Adidas", "Hermès", "Zara", "H&M", "Cartier","UNIQLO"]
store_name = ["Macy\'s", "Kohls", "Gabe\'s", "JC Penny"]
user_name = []
store_ids = [1, 2, 3, 4] #append store ids into this list?

all_stores = []
all_clothing = []


def make_clothing(stock_count):
    print("Clearing Stock...")
    session.query(ClothingArticle).delete()
    session.commit()
    
    print("Making clothes...")
    clothing = [ClothingArticle(
        id=None,
        brand= brand[randint(0, len(brand))],
        clothing_type=clothing_type[randint(0, len(clothing_type)-1)],
        sizes= size[randint(0,len(size)-1)],
        store_id=store_ids[randint(0,len(store_ids)-1)],
        price= randint(0, 75))
        for i in range(stock_count)]
    session.add(clothing)
    session.commit()
    all_clothing.append(clothing)
    return clothing

def make_store(store_count):
    print("Demolishing Stores....")
    session.query(Store).delete()
    session.commit()

    print("Building Store...")
    stores = [Store (
        id = None,
        name = store_name[randint(0,len(store_name)-1)],
        location = location[randint(0,len(location)-1)],
        max_price = handle_max_price() # need to write this function
        ) for i in range(store_count)]
    session.add(stores)
    session.commit()
    all_stores.append(stores)
    return stores

make_clothing(10)
make_store(10)


print(all_stores)
print(all_clothing)
