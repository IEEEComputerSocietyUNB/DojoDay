Dojo Day 2017
=============

Motivação
---------

Você se chama ``Batman`` e foi contratado para desenvolver uma simples página com um formulário de login de um site. Como todo grande herói, você possui um arqui-inimigo, chamado ``Coringa``, que é um hacker. Ele descobriu que você foi contratado para este freela e vai tentar minar este serviço.

Como todo vilão, ele vai utilizar um método de força bruta para achar um usuário cadastrado para roubar os dados, portanto elabore um sistema que previna a utilização deste método.

.. image:: http://i.imgur.com/Zl5Mjan.jpg

Entregas
--------

Todas as entregas têm que ser implementadas utilizando a metodologia de ``TDD``:

1. Testar a aplicação desejada;
2. Quebrar o teste pois a lógica ainda não foi desenvolvida;
3. Implementar a lógica;
4. Testar novamente e passar;
5. Refatorar se for necessário.

* Primeira entrega: Implementar a aplicação básica de um back-end em ``Flask``. Testar url local (``http://localhost:5000``) e url do formulário (``http://localhost:5000/login``).

* Segunda entrega: Implementar a aplicação básica do ``Selenium`` para testar o preenchimento do formulário. Para tanto, pode-se criar um ``stub`` de usuários cadastrados e testar se o usuário que está querendo entrar vai conseguir logar e receber uma mensagem de "Bem Vindo!" ou um erro na página de formulário caso contrário.

* Terceira entrega: Implementar prevenção de login por força bruta. Sugestão: se caso o usuário tentar entrar com o mesmo login 5 vezes seguidas e errar todas elas, colocar um ReCaptcha para verificar se o usuário é um humano e não um bot, causando um certo atraso como resposta para este usuário afim de retardar o algoritmo de força bruta ou até mesmo quebrar.
