#!/usr/bin/python3
"""
a script that lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from relationship_city import City
from relationship_state import Base, State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    resArr = session.query(City.id, City.name, State.name)
    resFilteredArr = resArr.filter(City.state_id == State.id).order_by(City.id)
    for r in resFilteredArr:
        print("{}: {} -> {}".format(r[0], r[1], r[2]))
