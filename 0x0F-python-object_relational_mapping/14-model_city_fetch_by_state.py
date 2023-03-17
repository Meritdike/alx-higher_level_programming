#!/usr/bin/python3
""" python script that prints all City objects
from the database hbtn_0e_14_usa """

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    cities = session.query(City).all()
    for city in cities:
        state = session.query(State).filter_by(id=city.state_id).first()
        print(f'{state.name}: ({city.id}) {city.name}')
