# Serviço de emails

Este serviço é responsável únicamente pelo envio de e-mails. Ele recebe requisições com o conteúdo do e-mail e o destinatário, e realiza o envio do e-mail. O serviço é utilizado pelos demais serviços para enviar notificações aos usuários, seja com o link para verificar o e-mail, resetar a senha ou notificar sobre um novo questionário disponível. Este serviço usa o [Neutrino API](https://www.neutrinoapi.com/) para verificar se o e-mail é válido.

Antes de utilizar o serviço, crie um arquivo `.env` com as seguintes variáveis:

- GOOGLE_APP_PASS - Chave do google para permitir o envio de e-mails via gmail.
- NEUTRINO_URL - URL base do neutrino, usualmente: "https://neutrinoapi.net".
- NEUTRINO_ID - User ID do Neutrino.
- NEUTRINO_KEY - API Key do Neutrino.


## Instalação local

Para utilizar o serviço localmente, é recomendado a criação de um ambiente virtual.

```bash
python -m venv .venv
.venv/scripts/activate
```

Após a criação do ambiente virtual, instale as dependências do projeto.

```bash
pip install -r requirements.txt
```

### Execução

Para executar o servidor, utilize o comando:

```bash
fastapi run app --port 8006
```

O servidor estará disponível em `http://localhost:8006`.

## Utilizando via Docker

Para executar via Docker, é necessário ter o Docker instalado e em execução. Também é necessário que exista uma rede chamada `psitest`. A rede deve ser criada uma única vez com o seguinte comando:

```bash
docker network create psitest
```

Após a criação da rede, execute o seguinte comando para criar a imagem do serviço:

```bash
docker compose up
```

O serviço estará disponível em `http://localhost:8006`.

