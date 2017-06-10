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

# Métodos do Unittest que podem ser uteis:
#
#   self.assertEqual(obj1, obj2) -> testa se obj1 é igual ao obj2
#   self.assertRaises(exception, callable) -> testa se a execução de callable
#                                               chama a exceção exception
#   self.assertTrue(obj1) -> testa se o obj1 é avaliado como verdadeiro
#   self.assertFalse(obj1) -> testa se o obj1 é avaliado como falso
#   self.assertNotIn(ob1, obj2) -> testa se obj1 não está dentro do obj2
#   self.assertIn(ob1, obj2) -> testa se obj1 está dentro do obj2

class TestHome(unittest.TestCase):

    # TODO Iniciar aplicação e url inicial
    def setUp(self):
        pass

class TestForms(unittest.TestCase):

    # TODO Iniciar aplicação e url inicial
    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()
