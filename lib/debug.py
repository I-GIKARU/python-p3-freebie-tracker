#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    
    # Create a Session class and instantiate it
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Make the session available in the debugger
    import ipdb; ipdb.set_trace()