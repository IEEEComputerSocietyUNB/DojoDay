Dojo Day 2017
=============

Repositório para formular o material que o Coding Dojo UnB irá apresentar no `Dojo Day 2017`_.

Tools
-----

* Virtualenv
* Python 3.x
* Unittest
* Flask
* Bootstrap
* Selenium
* HTML

Create
------

* Criar ambiente env/
* Ativar o ambiente env/
* Baixar o `geckodriver`_
* Colocar o geckodriver em uma pasta e adicionar o PATH dele em seu ambiente:

    $ export PATH=$PATH:/path/to/geckodriver

* Executar o script:

    $ python3 setup.py install

Run Basics Tests
----------------

* Entrar em src/
* Executar o script:

    $ python3 basic_tests.py

Run Selenium Tests
----------------

* Rodar a aplicação web (ver próximo tópico)
* Entrar em src/
* Executar o script:

    $ python3 selenium_tests.py

* Como cada método de teste abre um browser para testar uma funcionalidade então é aconselhável rodar um teste por vez, por exemplo:

    $ python3 selenium_tests.py TestSelenium.test_fill_only_login

Run Web
---------

* Entrar em src/
* Executar o script:

    $ python3 main.py

* Acessar a página no http://localhost:5000

.. _Dojo Day 2017: https://www.sympla.com.br/dojo-day-3__144322
.. _geckodriver: https://github.com/mozilla/geckodriver/releases
