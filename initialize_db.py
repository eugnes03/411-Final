from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# User model
class User(Base):
    '''
    User model for storing user data

    Attributes:
    id (int): primary key
    username (str): username of the user
    email (str): email of the user
    salt (str): salt used for hashing the password
    hashed_password (str): hashed password
    '''

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    salt = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

# Define the LoanQualification model for storing loan application data
class LoanQualification(Base):
    '''
    LoanQualification model for storing loan application data

    Attributes:
    id (int): primary key
    user_id (int): foreign key to the user
    credit_score (int): credit score of the user
    annual_income (float): annual income of the user
    loan_amount (float): loan amount requested by the user
    qualified (bool): whether the user is qualified for the loan or not
    '''
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

