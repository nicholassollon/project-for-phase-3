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
        custid = input(
            "If you have a membership, please select your name from the list:")
        customer = session.query(Customer).filter(
            Customer.id == custid).one_or_none()

    store = None

    create_store_table(session.query(Store))

    while not store:
        store_id = input(
            'Please select the store by its ID, type \'closet\' to see your clothes, or type \'funds\' to add funds:')
        if (store_id == 'closet'):
            print("Here is your drippy closet: ")
            create_customer_clothing_table(session.query(ClothingArticle).filter(ClothingArticle.customer_id==custid))
            pass
        elif (store_id == 'funds'):
            funds = input("Please enter the amount you wish to add: ")
            customer.budget += float(funds)
            session.commit()
            print(f'You now have ${customer.budget} in your wallet')
            pass
        else:
            store = session.query(Store).filter(
                Store.id == store_id).one_or_none()

    print(f'Wallet: ${customer.budget}')
    print(
        f'Thank you for choosing {store}! Please, browse our \'wears\'... get it? wears...? never mind...')

    create_store_clothing_table(session.query(
        ClothingArticle).filter(ClothingArticle.store_id == store.id))

    clothing_articles_id = input(
        "Please select something you like from our list or type back to finish shopping: ")
    item = session.query(ClothingArticle).filter(
        ClothingArticle.id == clothing_articles_id).one_or_none()
    if item == "back" or item == "Back":
        print("Thank you for browsing! Have a nice day!")
    else:
        customer.budget -= item.price
        item.custid = customer.id
        session.commit()
        print(
            f"Thank you for your purchase! You now have ${customer.budget - item.price}")
        print("Have a nice day!")
        session.close()
