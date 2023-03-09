from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Store, Customer, ClothingArticle

from helpers import create_customer_table, create_store_clothing_table, create_customer_clothing_table, create_store_table



if __name__ == "__main__":
    engine = create_engine("sqlite:///db/project-for-phase-3.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Hello and welcome to our store interface")
    customer = session.query(Customer)
    create_customer_table(customer)

    customer = None
    while not customer:
        customer_id = input("If you have a membership, please select your name from the list:")
        customer = session.query(Customer).filter(Customer.id == customer_id).one_or_none()
    
    wallet = customer.budget
    store = None

    while not store:
        store_id = input('Please select the store you would like to shop at by entering the store ID:')
        store = session.query(Store).filter(Store.id == store_id).one_or_none()
    
    print("$"+wallet)
    print(f'Wallet: {customer.budget}')
    print(f'Thank you for choosing ${store}! Please, browse our \'wears\'... get it? wears...? never mind...')
    create_store_clothing_table(store)

    shopping = True
    while shopping:
        clothing_articles_id = input("Please select something you like from our list: ")
        item = session.query(ClothingArticle).filter(ClothingArticle.id == clothing_articles_id).one_or_none()
        wallet -= item.price

    
    
    
    
    

