import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Creează un client de test pentru aplicația Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        # Verifică dacă ruta "/" răspunde corect
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Conexiune reușită", response.get_data(as_text=True))

if __name__ == "__main__":
    unittest.main()
