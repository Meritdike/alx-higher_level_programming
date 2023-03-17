#!/usr/bin/python3
""" python script that deletes all State objects with a
name containing the letter a from the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        session.delete(state)
    session.commit()
