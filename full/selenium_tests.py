import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class TestSelenium(unittest.TestCase):

    def setUp(self):
        # create the fake browser
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)

    def waitForElement(self, type, name):
        if type == 'id':
            return self.wait.until(EC.visibility_of_element_located((By.ID,
                                                                    name)))
        elif type == 'class':
            return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,
                                                            name)))

    def test_fill_only_login(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')

        username = self.driver.find_element_by_id('inputLogin')
        username.send_keys('Dayanne')
        self.driver.find_element_by_name('submit').click()

        # error message will never appear, so raise a timetout
        self.assertRaises(TimeoutException,
                            lambda : self.waitForElement('id', 'error'))

        self.tearDown()

    def test_fill_only_password(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')

        password = self.driver.find_element_by_id('inputPassword')
        password.send_keys('123')

        self.driver.find_element_by_name('submit').click()

        # error message will never appear, so raise a timetout
        self.assertRaises(TimeoutException,
                            lambda : self.waitForElement('id', 'error'))

        self.tearDown()

    def test_fill_wrong_login(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')

        username = self.driver.find_element_by_id('inputLogin')
        password = self.driver.find_element_by_id('inputPassword')

        username.send_keys('dayanne@g.com')
        password.send_keys('gg')

        self.driver.find_element_by_name('submit').click()

        # an error message appear
        self.assertEqual('Erro, insira um login válido.',
                            self.waitForElement('id', 'error').text)

        self.tearDown()

    def test_fill_correct_login(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')

        username = self.driver.find_element_by_id('inputLogin')
        password = self.driver.find_element_by_id('inputPassword')

        username.send_keys('dayanne@gg.com')
        password.send_keys('12345')

        self.driver.find_element_by_name('submit').click()

        # a welcome message appear
        self.assertEqual('Bem vinda.',
                        self.waitForElement('id', 'error').text)

        self.tearDown()

    def test_insert_two_wrong_logins(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')

        self.login('day@g.com', '123')
        # an error message appear
        self.assertEqual('Erro, insira um login válido.',
                            self.waitForElement('id', 'error').text)

        self.login('cris@g.com', '123')
        # an error message appear
        self.assertEqual('Erro, insira um login válido.',
                            self.waitForElement('id', 'error').text)

        self.tearDown()

    def login(self, user_email, user_pass):
        self.waitForElement('id', 'inputLogin')
        username = self.driver.find_element_by_id('inputLogin')
        password = self.driver.find_element_by_id('inputPassword')

        username.send_keys(user_email)
        password.send_keys(user_pass)

        self.driver.find_element_by_name('submit').click()

    def test_not_appear_captcha_if_insert_five_diff_wrong_logins_followed(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')

        for i in range(5):
            self.login('day'+str(i)+'@g.com', str(i))

        # error message will never appear, so raise a timetout
        self.assertRaises(TimeoutException,
                            lambda : self.waitForElement('class',
                                                        'g-recaptcha'))

        self.tearDown()

    def test_dismiss_captcha_after_six_wrong_logins_followed(self):
        # get request using the fake browser
        self.driver.get('http://localhost:5000/login')

        for i in range(6):
            self.login('day@g.com', '1'+str(i))
            time.sleep(1)

        time.sleep(1)
        self.assertEqual("You're a HACKER!",
                        self.waitForElement('id', 'error').text)

        self.tearDown()

    def tearDown(self):
        # wait a little and close the fake web
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
