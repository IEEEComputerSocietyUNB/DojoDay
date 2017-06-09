from flask import Flask, render_template, request, redirect, url_for

# Nome da aplicação
app = Flask('app')

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
