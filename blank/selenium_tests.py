import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Métodos e propriedades do Selenium que podem ser uteis:
#
#   webdriver.Firefox() -> abre o browser
#
#   driver.get(url) -> acessa uma url e coleta o html estático da página
#   driver.find_element_by_id(id) -> pega o elemento que contêm a id procurada
#   driver.find_element_by_name(name) -> pega o elemento que contêm a o name
#                                        procurado
#   driver.page_source -> último arquivo html da url requisitada no setup
#   driver.refresh() -> atualiza a página atual
#   driver.switch_to.alert() -> foca no dialog aberto
#   driver.add_cookie(cookie) (e.g. cookie: {‘name’ : ‘foo’}) -> adiciona
#                                                               cookies
#   driver.get_cookies() -> coleta os cookies atuais
#   driver.close() -> fecha uma aba, se tiver só uma aba então fecha o browser
#   driver.quit() -> fecha o browser
#   driver.forward() -> avança no histórico da página do browser
#   driver.back() -> retrocede no histórico da página do browser
#
#   dialog.accept() -> aceita o dialog
#   dialog.dismiss() -> dispensa o dialog
#
#   element.send_keys(key) -> key pode ser uma string ou um chave,
#                               e.g. Keys.RETURN
#   element.clear() -> limpa qualquer texto em um campo de input
#   element.click() -> manda evento de clicar no elemento

# Métodos do Unittest que podem ser uteis:
#
#   self.assertEqual(obj1, obj2) -> testa se obj1 é igual ao obj2
#   self.assertRaises(exception, callable) -> testa se a execução de callable
#                                               chama a exceção exception
#   self.assertTrue(obj1) -> testa se o obj1 é avaliado como verdadeiro
#   self.assertFalse(obj1) -> testa se o obj1 é avaliado como falso
#   self.assertNotIn(ob1, obj2) -> testa se obj1 não está dentro do obj2
#   self.assertIn(ob1, obj2) -> testa se obj1 está dentro do obj2

# Métodos do Python que podem ser uteis:
#
#   time.sleep(x) -> insere delay de x segundos no programa

class TestSelenium(unittest.TestCase):

    # TODO Iniciar o browser e url inicial
    def setUp(self):
        pass

    # TODO Fechar o browser
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
