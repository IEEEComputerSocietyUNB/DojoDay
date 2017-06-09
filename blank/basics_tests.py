import unittest
from main import app

# Métodos do Flask que podem ser uteis:
#
#   app.test_client() -> inicia o servidor para testar aplicação
#   app.test_client().get(url) -> abre uma url com a aplicação do flask
#                               (localhost = '/')
#   app.test_client().get(url).data.decode('utf-8') -> coleta o html da url
#                                                       como string
#   app.test_client().get(url).status_code -> código da resposta da requisição
#                                           (200 é OK, 404 erro)
#   app.test_client().get(url).content_type -> tipo do arquivo retornado no get

class TestHome(unittest.TestCase):

    # Inicia aplicação e url inicial
    def setUp(self):
        pass

class TestForms(unittest.TestCase):

    # Inicia aplicação e url inicial
    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()
