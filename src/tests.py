import unittest
from main import local_app
from selenium import webdriver

class TestHome(unittest.TestCase):

    def setUp(self):
        app = local_app.test_client()
        self.response = app.get('/')
        # return bytes
        self.content = self.response.data.decode('utf-8')

    def test_get_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_content(self):
        self.assertIn('text/html', self.response.content_type)

    def test_index_title(self):
        self.assertIn('<title>Dojo Day 2017</title>', self.content)

    def test_index_event_detail(self):
        self.assertIn('<p>Como testar sua', self.content)

    def test_bootstrap_css(self):
        self.assertIn('bootstrap.min.css', self.content)

class TestForms(unittest.TestCase):

    def setUp(self):
        app = local_app.test_client()
        self.response = app.get('/login')
        self.content = self.response.data.decode('utf-8')

    def test_login_form(self):
        self.assertIn('type="email"', self.content)

    def test_password_form(self):
        self.assertIn('type="password"', self.content)

    def test_send_button(self):
        self.assertIn('type="submit"', self.content)

class TestSelenium(unittest.TestCase):

    def setUp(self):
        # create the fake browser
        self.driver = webdriver.Firefox()
        # get request using the fake browser
        self.driver.get('/')

    def closeWeb(self):
        # close the fake browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
