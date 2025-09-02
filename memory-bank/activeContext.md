# Active Context: Setup e Planejamento

## Foco Atual

O foco no momento é **Planejamento e Arquitetura**.

Estamos na fase inicial do projeto, onde o objetivo é definir claramente o "o quê", o "porquê" e o "como". Não estamos escrevendo código de implementação ainda.

## Atividades em Andamento

1. **Estruturação do Memory Bank**: Estamos criando a documentação fundamental que guiará todo o desenvolvimento. Já definimos:
    - `projectbrief.md`: O escopo e objetivos.
    - `productContext.md`: O valor para o usuário.
    - `techContext.md`: A stack de tecnologia.
    - `systemPatterns.md`: A arquitetura e o fluxo de dados.

## Próximos Passos Imediatos

1. Criar o arquivo `progress.md` para finalizar a estrutura do Memory Bank.
2. Revisar o plano completo com o stakeholder (você) para obter aprovação.
3. Após a aprovação, preparar para a transição para o modo de implementação, começando pelo **Módulo de Web Scraping**.

## Decisões Recentes

- O agendamento será feito via biblioteca `schedule` em Python para portabilidade.
- O gerenciamento de dependências será com `uv`.
- A persistência de dados será feita com `SQLite`.
