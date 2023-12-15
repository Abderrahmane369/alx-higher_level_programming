#!/usr/bin/python3
"""Module that contains the clasand an instance"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                    argv[2], argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    objects = session.query(State).order_by(State.id).limit(1).first()

    if object != []:
        print(str(1) + ': ' + objects.name)
    else:
        print("Nothing")


if __name__ == '__main__':
    main()
