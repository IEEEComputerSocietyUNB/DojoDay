# from selenium import webdriver
from flask import Flask

local_app = Flask('local_app')

@local_app.route('/')
def home():
    return 'Dojo Day 2017'

if __name__ == '__main__':
    local_app.run()


# def main():
#     # create the fake browser
#     driver = webdriver.Firefox()
#
#     # get request using the fake browser
#     driver.get('/')
#
#     # close the fake browser
#     driver.quit()
