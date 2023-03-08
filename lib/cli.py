from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Store



if __name__ == "__main__":
    engine = create_engine("sqlite:///project-for-phase-3.db")
    Session = sessionmaker(bind=engine)
    session = Session()