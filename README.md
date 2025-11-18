# pesquisaWeb

Este guia explica como instalar e executar a aplicação em seu próprio computador utilizando Docker.
Antes de começar, você precisa ter dois programas instalados no seu computador:

1.  **Git:** Para baixar o código do projeto. Se não tiver, pode baixá-lo em 
    [git-scm.com](https://git-scm.com/downloads).
2.  **Docker Desktop:** Esta é a ferramenta principal. Ela gerencia todos os "contêineres" (pequenos ambientes virtuais) para o banco de dados, a aplicação e os serviços de fundo, tudo de forma automática. Baixe em 
    [www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/).

#### **Passo 1: Obter o Código do Projeto**

1.  Abra um terminal (no Windows, pode ser o "Prompt de Comando", "PowerShell" ou "Terminal"; no Mac Linux, o "Terminal").
2.  Clone o repositório do projeto para o seu computador. Você precisará do link do repositório (ex: `https://github.com/seu-usuario/seu-projeto.git`).
    ```bash
    git clone ---URL_DO_REPOSITORIO_GIT---
    ```
3.  Navegue para a pasta do projeto que foi criada.
    ```bash
    cd pesquisaWeb 
    ```
    *(ou o nome da pasta principal do projeto)*


#### **Passo 2: Iniciar a Aplicação com Docker**

Este é o passo principal. Com o Docker Desktop aberto e em execução, execute o seguinte comando no seu terminal, dentro da pasta `pesquisaWeb`:

```bash
docker-compose up --build
```

Você verá muitas mensagens no terminal, indicando que os serviços estão a iniciar. Deixe este terminal aberto, pois ele mostrará os logs da aplicação.

#### **Passo 3: Acessar à Aplicação**

Pronto!! Agora você pode abrir o seu navegador de internet (Chrome, Firefox, etc.) e acessar ao seguinte endereço:

[http://localhost:5000](https://www.google.com/search?q=http://localhost:5000)

Use o login 'admin' e senha '123' para acessar a aplicação.

#### **Como Parar a Aplicação**

Quando terminar de usar, volte ao terminal onde o `docker-compose` está a rodar e pressione `Ctrl + C`. Quando as menssagens terminarem basta encerrar o docker-compose:
```bash
docker-compose down
```

Este comando irá parar e remover todos os contêineres relacionados ao projeto, libertando os recursos do seu computador.