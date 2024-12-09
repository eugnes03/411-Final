from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for SQLAlchemy
Base = declarative_base()

# Define the User model for account management
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
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

# Create SQLite database and tables
DATABASE_URL = "sqlite:///loan_qualification_system.db"
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

# Create a session maker
Session = sessionmaker(bind=engine)
session = Session()

print("Database and tables have been successfully created for the Loan Qualification System.")

