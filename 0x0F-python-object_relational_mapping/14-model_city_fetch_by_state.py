#!/usr/bin/python3
"""OAOAOAOAOAO"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                    argv[2], argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State.name, City.id, City.name).join(
        State, State.id == City.state_id).order_by(City.id)

    for e in results:
        print(f"{e[0]}: ({e[1]}) {e[2]}")


if __name__ == '__main__':
    main()
