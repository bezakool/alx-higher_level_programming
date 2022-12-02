#!/usr/bin/python3
"""
a script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_city import City
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    resArr = session.query(State.name, City.id, City.name)
    resFilterArr = resArr.filter(City.state_id == State.id, City.id)
    resOrderdArr = resFilterArr.order_by(City.id)
    for r in resOrderdArr:
        print('{}: ({}) {}'.format(r[0], r[1], r[2]))
