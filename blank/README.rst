Dojo Day 2017
=============

Motivação
---------

Você foi contratado para desenvolver uma simples página com um formulário de login de um site, porém você possui um arqui-inimigo que é um hacker. Ele descobriu que você foi contratado para esse freela e irá tentar te atrapalhar (ou ajudar).

Você sabe que ele não é muito criativo e vai utilizar um método de força bruta para achar um usuário cadastrado para os dados, portanto elabore um sistema que previna a utilização deste método.

Entregas
--------

Todas as entregas tem que ser implementadas utilizando a metodologia de ``TDD``:

1. Testar a aplicação desejada;
2. Quebrar o teste pois a lógica ainda não foi desenvolvida;
3. Implementar a lógica;
4. Testar novamente e passar;
5. Refatorar se for necessário.


* Primeira entrega: Implementar a aplicação básica do ``Flask``.

  * Dica: Testar url local (``http://localhost:5000``) e url do formulário (http://localhost:5000/login).

* Segunda entrega: Implementar a aplicação básica do ``Selenium``. Testar o preenchimento do formulário.

  * Dica: Criar um stub de usuários e testar se o usuário que está querendo entrar vai entrar e receber uma mensagem de "Bem Vindo!" ou se não tiver cadastrado irá emitir erro na página de formulário.

* Terceira entrega: Implementar prevenção de login por força bruta.

  * Dica: Se caso o usuário tentar entrar com o mesmo usuário 5 vezes seguidas e errar estas 5 vezes, gerar um atraso como resposta para este usuário para que o algoritmo de força bruta que este usuário está utilizando demore mais que o desejado.
