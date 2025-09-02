# Product Context: ETL de Oportunidades Freelancer

## 1. Problema a Ser Resolvido

A busca manual por projetos em sites de freelancer como o Workana é um processo repetitivo e demorado. Profissionais perdem um tempo valioso navegando por dezenas de projetos irrelevantes antes de encontrar oportunidades que se encaixam em suas habilidades e interesses.

Isso leva a:

- **Perda de tempo**: Horas gastas em uma tarefa de baixo valor.
- **Perda de oportunidades**: Projetos bons podem ser perdidos no meio de tanto ruído ou se o profissional não verificar a plataforma no momento certo.
- **Desgaste**: A tarefa de procurar manualmente pode ser desmotivante.

## 2. Solução Proposta

Um sistema automatizado (ETL) que:

1. **Extrai** as informações essenciais dos novos projetos publicados.
2. **Transforma** esses dados brutos, limpando-os e, mais importante, categorizando-os de forma inteligente com base no conteúdo da descrição.
3. **Carrega** (entrega) um resumo diário ou periódico diretamente no email do usuário, contendo apenas as oportunidades que são relevantes para ele.

## 3. Experiência do Usuário (User Experience)

O usuário final deve ter uma experiência "configure e esqueça".

- **Setup**: O usuário apenas informa seu email e as categorias de seu interesse.
- **Recebimento**: Ele recebe um email claro e conciso, com uma lista de projetos. Cada item da lista deve conter:
  - Título do Projeto (com link para a vaga original).
  - Tags de categoria (ex: `Chatbot`, `Web Scraping`).
  - Faixa de Preço.
  - Número de propostas já enviadas.
- **Resultado**: O usuário economiza tempo e foca apenas em analisar e enviar propostas para os projetos que realmente importam.
