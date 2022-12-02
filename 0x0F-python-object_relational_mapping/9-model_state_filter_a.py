#!/usr/bin/python3
"""
a script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter(State.name.like("%a%"))
    for r in res:
        print('{}: {}'.format(r.id, r.name))
