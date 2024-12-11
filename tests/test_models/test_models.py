import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from initialize_db import Base, User, LoanQualification

class TestModels(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_create_user(self):
        """Test creating a new user."""
        new_user = User(username='testuser', email='testuser@example.com', salt='random_salt', hashed_password='dummy_hashed_password')
        self.session.add(new_user)
        self.session.commit()
        user = self.session.query(User).filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'testuser@example.com')

    def test_unique_email(self):
        """Test that emails must be unique."""
        user1 = User(username='user1', email='unique@example.com', salt='salt1', hashed_password='password1')
        user2 = User(username='user2', email='unique@example.com', salt='salt2', hashed_password='password2')
        self.session.add(user1)
        self.session.commit()
        self.session.add(user2)
        with self.assertRaises(Exception):
            self.session.commit()

    def test_unique_username(self):
        """Test that usernames must be unique."""
        user1 = User(username='uniqueuser', email='uniqueuser1@example.com', salt='salt1', hashed_password='password1')
        user2 = User(username='uniqueuser', email='uniqueuser2@example.com', salt='salt2', hashed_password='password2')
        self.session.add(user1)
        self.session.commit()
        self.session.add(user2)
        with self.assertRaises(Exception):
            self.session.commit()

if __name__ == "__main__":
    unittest.main()
