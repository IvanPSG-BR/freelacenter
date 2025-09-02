# Tech Context: ETL de Oportunidades Freelancer

## 1. Linguagem de Programação Principal

- **Python**: Escolhido por sua simplicidade, ecossistema robusto de bibliotecas para web scraping, manipulação de dados e integração com APIs.

## 2. Bibliotecas e Frameworks Chave

- **Web Scraping**:
  - **Beautiful Soup**: Para parsing de HTML.
  - **Requests**: Para realizar as requisições HTTP.
  - *Consideração*: `Selenium` ou `Playwright` serão avaliados se o conteúdo dinâmico via JavaScript se provar um obstáculo.

- **Interação com API**:
  - **Google AI Python SDK (`google-generativeai`)**: Para interagir com a API do Gemini.

- **Envio de Email**:
  - **smtplib**: Biblioteca padrão do Python para envio de emails via SMTP.

- **Agendamento (Scheduling)**:
  - **Schedule**: Biblioteca Python leve e intuitiva para agendar tarefas. Essencial para rodar em ambientes de deploy como o Render, onde não temos acesso a um `cron` do sistema.

- **Banco de Dados**:
  - **sqlite3**: Biblioteca nativa do Python para interagir com o banco de dados SQLite.

## 3. Ambiente de Desenvolvimento

- **Gerenciador de Pacotes e Ambientes Virtuais**: **uv**. Será utilizado para gerenciar as dependências e o ambiente virtual do projeto de forma unificada e performática.

## 4. Armazenamento de Dados

- **SQLite**: Será o banco de dados do projeto. Utilizado para:
  - Persistir os dados coletados dos sites (projetos, propostas, etc.).
  - Manter um registro das notificações já enviadas para evitar o envio de duplicatas.
