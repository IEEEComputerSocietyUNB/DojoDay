# from selenium import webdriver
from flask import Flask, render_template

local_app = Flask('local_app')

@local_app.route('/')
def home():
    return render_template('index.html')

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
