#!/usr/bin/python3
"""script lists all State objects,"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    s = session.query(State).order_by(State.id).all()
    for st in s:
        print("{}: {}".format(st.id, st.name))
    session.close()
