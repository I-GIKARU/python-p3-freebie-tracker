# seed.py
#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data
    session.query(Freebie).delete()
    session.query(Company).delete()
    session.query(Dev).delete()

    # Create sample companies
    company1 = Company(name="Google", founding_year=1998)
    company2 = Company(name="Facebook", founding_year=2004)
    company3 = Company(name="Amazon", founding_year=1994)

    # Create sample devs
    dev1 = Dev(name="Alice")
    dev2 = Dev(name="Bob")
    dev3 = Dev(name="Charlie")

    # Create sample freebies
    freebie1 = Freebie(item_name="T-shirt", value=10, dev=dev1, company=company1)
    freebie2 = Freebie(item_name="Stickers", value=5, dev=dev1, company=company2)
    freebie3 = Freebie(item_name="Mug", value=15, dev=dev2, company=company1)
    freebie4 = Freebie(item_name="Laptop", value=1000, dev=dev3, company=company3)

    # Add to session
    session.add_all([company1, company2, company3, dev1, dev2, dev3, freebie1, freebie2, freebie3, freebie4])
    session.commit()
    print("Database seeded successfully!")