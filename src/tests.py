import unittest
from main import local_app

class TestHome(unittest.TestCase):

    def test_get(self):
        app = local_app.test_client()
        response = app.get('/')
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
