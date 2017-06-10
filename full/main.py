from flask import Flask, render_template, request, redirect, url_for, Markup
from flask_recaptcha import ReCaptcha

app = Flask('app')
recaptcha = ReCaptcha(app=app,
                    site_key='6LeS4SQUAAAAAGbKWNy1b9oG7TSV6bhUaUJ4V-cF',
                    secret_key='6LeS4SQUAAAAAO8JR_FkGwbZBQ721uLci19X3bcC')

log = {}
captcha = ''
all_users = [('dayanne@gg.com', '12345'), ('day@gg.com', '123')]
google_captcha = Markup('<div class="g-recaptcha" data-sitekey="6LeS4SQUAAAAAGbKWNy1b9oG7TSV6bhUaUJ4V-cF"></div>')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    global log, captcha
    error = ''
    if request.method == 'POST':
        user_email, user_password = request.form['inputLogin'], request.form['inputPassword']

        if captcha:
            if recaptcha.verify():
                if valid_login(user_email, user_password):
                    log[user_email], error = 0, 'Bem vinda.'
            else:
                error = "You're a HACKER!"
        elif valid_login(user_email, user_password):
            log[user_email], error, captcha = 0, 'Bem vinda.', ''
        else:
            if user_email not in log.keys():
                log[user_email] = 1
            else:
                log[user_email] += 1

            if log[user_email] >= 5:
                captcha = google_captcha

            error = 'Erro, insira um login válido.'
    else:
        log, captcha = {}, ''

    return render_template('forms.html', error = error, captcha = captcha)

def valid_login(username, password):
    return True if (username, password) in all_users else False

if __name__ == '__main__':
    app.run(debug=True)
