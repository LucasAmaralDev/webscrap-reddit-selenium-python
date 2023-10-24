# Automatização de Web Scraping do r/brdev

Este é um projeto de automação de web scraping que coleta os posts mais quentes do subreddit r/brdev no Reddit e os envia para uma API para armazenamento e disponibilização dos dados. O projeto utiliza as bibliotecas Selenium, Selenium Stealth, Requests e Webdriver Manager para automatizar o processo.

## Instalação

Certifique-se de ter o Python instalado no seu sistema. Em seguida, siga estas etapas para configurar o ambiente:

1. Clone o repositório:

        git clone https://github.com/LucasAmaralDev/webscrap-reddit-selenium-python
        cd webscrap-reddit-selenium-python


2. Instale as dependências:

        pip install selenium
        pip install selenium-stealth
        pip install requests
        pip install webdriver_manager

3. Configure as credenciais da API, se necessário, no arquivo `config.json`.

## Uso

Para executar a automação, simplesmente execute o script `main.py`:

    python main.py

Isso iniciará o processo de web scraping e envio dos dados para a API.

## Configuração

No arquivo `config.json`, você pode definir as seguintes configurações:

- `reddit_url`: URL do subreddit alvo (neste caso, https://www.reddit.com/r/brdev/).
- `api_url`: URL da API para o envio dos dados.

## Contribuição

Se desejar contribuir para este projeto, siga estas etapas:

    1. Fork o repositório.
    2. Crie uma branch para a sua contribuição: `git checkout -b minha-contribuicao`
    3. Faça as alterações e commit: `git commit -m 'Adicionei recurso X'`
    4. Faça o push para a sua branch: `git push origin minha-contribuicao`
    5. Crie um Pull Request.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.

## Contato

Se você tiver alguma dúvida ou precisar de suporte, entre em contato com [lucashsamaral@gmail.com](mailto:lucashsamaral@gmail.com).


