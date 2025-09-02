# Project Brief: ETL de Oportunidades Freelancer

## 1. Objetivo Principal

Automatizar a coleta, categorização e notificação de novos projetos de freelancer postados em plataformas online, com foco inicial no Workana, para otimizar a busca por oportunidades relevantes.

## 2. Core Features

- **Web Scraping**: Extrair dados de projetos (título, descrição, número de propostas, faixa de preço) de sites como Workana e 99Freela.
- **Categorização Inteligente**: Utilizar a API do Gemini para analisar o conteúdo dos projetos e atribuir tags pré-determinadas (ex: `Automatização`, `Chatbot`, `Landing Page`, `Site Completo`).
- **Agendamento**: Executar o processo de ETL em intervalos de tempo configuráveis.
- **Notificação**: Enviar um resumo das novas oportunidades para um endereço de email cadastrado.

## 3. Escopo do MVP (Minimum Viable Product)

- Foco exclusivo no site **Workana**.
- Extração dos campos: Título, Descrição, URL, Faixa de Preço, Número de Propostas.
- Um conjunto fixo de 5 a 10 tags para categorização.
- Envio de um email em formato de texto simples.
- Agendamento manual ou com um intervalo fixo (ex: a cada 6 horas).
