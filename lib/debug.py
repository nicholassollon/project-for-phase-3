from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Review

if __name__ == '__main__':
    engine = create_engine("sqlite:///clothes_r_us.db")
    Session = sessionmaker(bind=engine)
    session = Session()