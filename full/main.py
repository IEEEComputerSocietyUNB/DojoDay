from flask import Flask, render_template, request, redirect, url_for

local_app = Flask('local_app')

@local_app.route('/')
def home():
    return render_template('index.html')

@local_app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        if valid_login(request.form['inputLogin'], request.form['inputPassword']):
            error = 'Bem vinda.'
            # return redirect(url_for('index'))
        else:
            error = 'Erro, insira um login válido.'

    return render_template('forms.html', error = error)

def valid_login(username, password):
    return True if (username, password) in all_users else False

all_users = [('dayanne@gg.com', '12345'), ('day@gg.com', '123')]

if __name__ == '__main__':
    local_app.run(debug=True)
