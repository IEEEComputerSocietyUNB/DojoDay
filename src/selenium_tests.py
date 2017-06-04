import unittest
import time
from selenium import webdriver

class TestSelenium(unittest.TestCase):

    def setUp(self):
        # create the fake browser
        self.driver = webdriver.Firefox()
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')

    def test_fill_only_login(self):
        username = self.driver.find_element_by_id('inputLogin')
        username.send_keys('Dayanne')
        self.driver.find_element_by_name('submit').click()
        time.sleep(2)
        # self.assertIn('Erro, insira uma senha.', self.driver.page_source)
        username.clear()
        self.closeWeb()

    def closeWeb(self):
        # close the fake browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
