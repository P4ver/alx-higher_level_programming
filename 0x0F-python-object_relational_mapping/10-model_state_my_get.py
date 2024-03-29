#!/usr/bin/python3
"""
Script prints the stat obj with the name passed as arg
from db SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    s = session.query(State).filter(State.name == argv[4]).first()

    if s:
        print("{}".format(s.id))
    else:
        print("Not found")
    session.close()
