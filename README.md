# Desafio-Tech-Frexco
Projeto feito para o desafio para vaga de estágio na Frexco. O desafio proposto foi:
construir pelo menos dois endpoints utilizando Django:
  - Cadastrar usuário, fornecendo o login, senha e data de nascimento
  - Senha deixar como opcional, se não fornecido gerar uma senha aleatória.
  - Consultar usuários cadastrados.
  - Deve ser possível consultar em XLSX, CSV ou JSON.

O Projeto foi feito a partir do Django Rest Framework, uma biblioteca para o framework Django que nos permite implementar uma API de formar intuitiva e produtiva. A partir da API foi criado o app que irá conter o Back-End.

O arquivo models.py contem o modelo para criação da tabela que utilizaremos no banco de dados, onde teremos os dados de login, senha e data de nascimento.

O arquivo views.py contém todas as views que foram utilizadas no projeto. Nele temos definidos os tipos de requisição e as funções que tratam e recebem os dados para serem inseridos no banco de dados. As Views utilizadas no Rest Framework são basicamente o controller da nossa aplicação.

Para este projeto temos 3 views:

  - A view createUser cria um novo usuário a partir dos dados recebidos pelo método de requisição POST. Nele verificamos se o login de cadastro já existe no banco, para evitar múltiplos usuários com o o mesmo login, verificamos se a senha digitada é nula, caso for é gerada uma senha e ela é salva neste usuário e também retornada à requisição para futuras utilizações com o front-End, e verificamos também se a senha digitada é nula, retornando uma mensagem para solicitar que digitem a senha. Para todos estes dados é ainda utilizada uma função da classe ModelsSerializer para verificar se os dados recebidos estão no formato correto para serem salvos no banco, adicionando mais uma verificação quanto a validação dos dados.

  - A view usersList retorna os dados dos usuários cadastrados no banco em 3 formatos, JSON, XLSX e CSV, de acordo com o especificado na URL.

  - A view getById retorna os dados do usuário pelo ID que é passado junto a URL.

Por fim temos as urls dos nossos endpoinst.

Para iniciar o servidor da nossa apllicação basta utilizar o comando "python manage.py runserver". o nosso servidor é iniciado em http://127.0.0.1:8000/, e temos os seguintes endpoinst:

O endpoint /create, onde os dados do usuário são enviados em formato JSON, como mostrado o exemplo abaixo utilizando a ferramenta de desenvolvimento e teste Insomnia.

![image](https://user-images.githubusercontent.com/99613258/201769854-ffc52fd3-8cf7-49f4-9323-f0f1d28ca5e4.png)

O endpoint /users, onde enviamos junto ao endereço da url o formato em que desejamos o retorno da busca dos usuários já cadastrados, sendo as urls aceitas a /users/?formato=JSON, /users/?formato=XLSX e /users/?formato=CSV, que retornarão como resposta da requisição os dados respectivamente nos formatos JOSN ,XLSX e CSV, como mostrado abaixo.

![image](https://user-images.githubusercontent.com/99613258/201769932-b1ce8dfd-6fe1-4c46-bd30-92a329c0e562.png)

Além de ser possível consultar um usuário específico pelo id na url /users, basta após a url inserir o id do usuário:

![image](https://user-images.githubusercontent.com/99613258/201769958-22b7ab9c-373b-4ee0-ab27-f4bb03642675.png)
