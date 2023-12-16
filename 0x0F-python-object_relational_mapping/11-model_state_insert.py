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

    louisana = State()
    louisana.name = "Louisiana"

    session.add(louisana)
    session.commit()

    print(louisana.id)


if __name__ == '__main__':
    main()
