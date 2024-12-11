from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    salt = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

# Define the LoanQualification model for storing loan application data
class LoanQualification(Base):
    __tablename__ = 'loan_qualifications'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    credit_score = Column(Integer, nullable=False)
    annual_income = Column(Float, nullable=False)
    loan_amount = Column(Float, nullable=False)
    qualified = Column(Boolean, default=False)

# Set up db & session
engine = create_engine('sqlite:///loan_qualification_system.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# create tables
Base.metadata.create_all(engine)
print("Database and tables have been successfully created for the Loan Qualification System.")

