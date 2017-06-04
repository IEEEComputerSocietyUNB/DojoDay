import unittest
from main import local_app

class TestHome(unittest.TestCase):

    def setUp(self):
        app = local_app.test_client()
        self.response = app.get('/')
        self.response_str = self.response.data.decode('utf-8')

    def test_get_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_content(self):
        self.assertIn('text/html', self.response.content_type)

    def test_index_title(self):
        self.assertIn('<title>Dojo Day 2017</title>', str(self.response_str))

    def test_index_event_detail(self):
        self.assertIn('<p>Como testar sua', str(self.response_str))

    def test_bootstrap_css(self):
        self.assertIn('bootstrap.min.css', self.response_str)

if __name__ == '__main__':
    unittest.main()
