from flask import Flask, render_template, request, redirect, url_for, Markup
from flask_recaptcha import ReCaptcha

# Nome da aplicação
app = Flask('app')

# Google ReCaptcha
# recaptcha = ReCaptcha(app=app,
#                     site_key='6LeS4SQUAAAAAGbKWNy1b9oG7TSV6bhUaUJ4V-cF',
#                     secret_key='6LeS4SQUAAAAAO8JR_FkGwbZBQ721uLci19X3bcC')

# HTML do widget do recaptcha
# google_captcha = Markup('<div class="g-recaptcha" data-sitekey="6LeS4SQUAAAAAGbKWNy1b9oG7TSV6bhUaUJ4V-cF"></div>')

# Método do ReCaptcha que podem ser uteis:
#
#   recaptcha.verify() -> confere se o recaptcha foi validado corretamente

# Métodos do Flask que podem ser uteis:
#
#   @app.route('/') -> url local irá ser redirecionada para a função 'func'
#   def func():
#       return render_template(file) (e.g. file = 'index.html') -> renderiza um
#                                                    arquivo html para esta url
#
#   @app.route('/olar', methods=['GET', 'POST']) -> a url '/olar' aceita
#                                   requisições do tipo GET e também POST
#
#   request.method -> checa a requisição atual
#   request.form[name] -> pega o input inserido no elemento identificado com
#                           o 'name'
#
#   render_template(file, data = error) (e.g. error = {'bar': 'foo'}) -> dados
#           enviados ao html do file para o framework do Jinja processar com
#              'data.bar' para sair 'foo'

if __name__ == '__main__':
    # Inicia aplicação em modo debug : permite atualizar o content a medida
    #   que os arquivos HTMLs forem sendo alterados
    app.run(debug=True)
