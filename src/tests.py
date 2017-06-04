import unittest
from main import local_app

class TestHome(unittest.TestCase):

    def setUp(self):
        app = local_app.test_client()
        self.response = app.get('/')

    def test_get_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_content(self):
        self.assertIn('text/html', self.response.content_type)

    def test_index_title(self):
        response = self.response.data.decode('utf-8')
        self.assertIn('<title>Dojo Day 2017</title>', str(response))

if __name__ == '__main__':
    unittest.main()
