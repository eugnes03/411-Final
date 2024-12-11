import unittest
from app import app

class SmokeTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_app_starts(self):
        """Check if the app starts and the home route works."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_account_page(self):
        """Check if the create-account page is accessible."""
        response = self.app.get('/create-account')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Create Account', response.data)

    def test_login_page(self):
        """Check if the login page is accessible."""
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_static_files(self):
        response = self.app.get('/static/styles.css')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
