#!/usr/bin/python3
"""Script prints the first State obj from db"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    st = session.query(State).order_by(State.id).first()

    if st:
        print("{}: {}".format(st.id, st.name))
    else:
        print("Nothing")
    session.close()
