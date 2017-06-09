import unittest
import time
from selenium import webdriver

class TestSelenium(unittest.TestCase):

    def setUp(self):
        # create the fake browser
        self.driver = webdriver.Firefox()

    def test_fill_only_login(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')
        username = self.driver.find_element_by_id('inputLogin')
        username.send_keys('Dayanne')
        self.driver.find_element_by_name('submit').click()
        self.resend_and_update()
        # either an error message appear
        self.assertNotIn('Erro, insira um login válido.', self.driver.page_source)
        # either a login message apeear
        self.assertNotIn('Bem vinda.', self.driver.page_source)
        self.tearDown()

    def test_fill_only_password(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')
        password = self.driver.find_element_by_id('inputPassword')
        password.send_keys('123')
        self.driver.find_element_by_name('submit').click()
        self.resend_and_update()
        # either an error message appear
        self.assertNotIn('Erro, insira um login válido.', self.driver.page_source)
        # either a login message apeear
        self.assertNotIn('Bem vinda.', self.driver.page_source)
        self.tearDown()

    def test_fill_wrong_login(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')
        username = self.driver.find_element_by_id('inputLogin')
        password = self.driver.find_element_by_id('inputPassword')
        username.send_keys('dayanne@g.com')
        password.send_keys('gg')
        self.driver.find_element_by_name('submit').click()
        self.resend_and_update()
        # an error message appear
        self.assertIn('Erro, insira um login válido.', self.driver.page_source)
        self.tearDown()

    def test_fill_correct_login(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')
        username = self.driver.find_element_by_id('inputLogin')
        password = self.driver.find_element_by_id('inputPassword')
        username.send_keys('dayanne@gg.com')
        password.send_keys('12345')
        self.driver.find_element_by_name('submit').click()
        self.resend_and_update()
        # an error message appear
        self.assertIn('Bem vinda.', self.driver.page_source)
        self.tearDown()

    def test_insert_two_wrong_logins(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')

        self.login('day@g.com', '123')
        self.resend_and_update()
        self.assertIn('Erro, insira um login válido.', self.driver.page_source)

        self.login('cris@g.com', '123')
        self.resend_and_update()
        self.assertIn('Erro, insira um login válido.', self.driver.page_source)

        self.tearDown()

    def test_dismiss_captcha_after_five_wrong_logins_followed(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')

        count, msg_error = 0, ''

        while count < 5:
            self.login('day@g.com', '123')
            self.resend_and_update()
            count += 2
            time.sleep(4)
            if 'error' in self.driver.page_source:
                msg_error = self.driver.find_element_by_id('error').text

        self.assertEqual("You're a HACKER!", msg_error)
        self.tearDown()

    def login(self, user_email, user_pass):
        username = self.driver.find_element_by_id('inputLogin')
        password = self.driver.find_element_by_id('inputPassword')

        username.send_keys(user_email)
        password.send_keys(user_pass)

        self.driver.find_element_by_name('submit').click()

    def resend_and_update(self):
        try:
            time.sleep(1)
            # refresh with the form
            self.driver.refresh()
            time.sleep(2)
            self.driver.switch_to.alert.accept()
        except:
            pass

    def tearDown(self):
        # wait a little and close the fake web
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
