import csv
import os
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "sqlite:///./banks.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Bank(Base):
    __tablename__ = "banks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    branches = relationship("Branch", back_populates="bank")

class Branch(Base):
    __tablename__ = "branches"
    ifsc = Column(String, primary_key=True, index=True)
    branch = Column(String)
    address = Column(String)
    city = Column(String)
    district = Column(String)
    state = Column(String)
    bank_id = Column(Integer, ForeignKey("banks.id"))
    bank = relationship("Bank", back_populates="branches")

def init_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Check if we already loaded the data to avoid duplicate loading
    if db.query(Branch).first() is None:
        csv_path = "bank_branches.csv"
        if os.path.exists(csv_path):
            print("Loading data from CSV... this will take a few seconds.")
            with open(csv_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                banks_added = set()
                
                for row in reader:
                    bank_id = int(row["bank_id"])
                    if bank_id not in banks_added:
                        db.add(Bank(id=bank_id, name=row["bank_name"]))
                        banks_added.add(bank_id)
                    
                    db.add(Branch(
                        ifsc=row["ifsc"],
                        branch=row["branch"],
                        address=row["address"],
                        city=row["city"],
                        district=row["district"],
                        state=row["state"],
                        bank_id=bank_id
                    ))
                db.commit()
            print("Database successfully populated from CSV!")
    db.close()