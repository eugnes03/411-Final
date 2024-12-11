import unittest
from app import app
from initialize_db import Base, engine, session
from flask import json
import hashlib
from hashlib import sha256

class TestRoutes(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(engine)

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        session.rollback()

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(engine)

    def test_index_route(self):
        response = self.app.get('/index')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<h1>Loan Qualification System</h1>", response.data)

    def test_create_account_success(self):
        response = self.app.post('/create-account', data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'confirm-password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Account created! Username: testuser, Email: testuser@example.com", response.data)

    def test_create_account_duplicate_user(self):
        self.app.post('/create-account', data={
            'username': 'someone',
            'email': 'whatever@example.com',
            'password': 'password123',
            'confirm-password': 'password123'
        })
        response = self.app.post('/create-account', data={
            'username': 'someone',
            'email': 'notwhatever@example.com',
            'password': 'password123',
            'confirm-password': 'password123'
        }, follow_redirects=True)
        self.assertIn(b"Username already exists.", response.data)

# not working
    def test_login_success(self):
        from initialize_db import User
        salt = "random_salt"
        hashed_password = hashlib.sha256((salt + "dummy_hashed_password").encode()).hexdigest()
        user = User(username="noone", email="another@example.com", salt=salt, hashed_password=hashed_password)
        session.add(user)
        session.commit()

        response = self.app.post('/login', data={
            'username': 'noone',
            'password': 'dummy_hashed_password'
        }
        self.assertIn(b"Welcome back, noone!", response.data)

        

    def test_check_eligibility(self):
        payload = {
            "username": "testuser",
            "creditScore": 700,
            "annualIncome": 50000,
            "loanAmount": 20000
        }
        response = self.app.post('/check-eligibility', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"qualified", response.data)

if __name__ == '__main__':
    unittest.main()
