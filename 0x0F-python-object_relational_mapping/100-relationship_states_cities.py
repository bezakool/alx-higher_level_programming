#!/usr/bin/python3
"""
a script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_data = State(name="California")
    city_data = City(name="San Francisco")
    state_data.cities.append(city_data)

    session.add(state_data)
    session.add(city_data)
    session.commit()
