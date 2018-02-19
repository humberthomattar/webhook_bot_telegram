# Roadmap

Agrupamento de necessidades de execução e idéias para o webhook e bot do telegram.

### Prospecção

Relação de necessidades funcionais e não-funcionais:

  - Tornar o Bot em multi clientes
  - avaliar necessidade de estruturar Dockerfile e Compose
  - Avaliar a necessidade do implementar o flask juntamente com o gunicorn
  - Avaliar o uso do i18n (via gettext?)

### A Fazer

Relação de necessidades técnicas:

  - Separar as mensagens de down e up, das mensagens de ssl
  - Estruturar a implementação dos logs da aplicação
  - Avaliar a implementação das mensagens
  - Rever as variáveis de ambiente
  - Remover as mensagens desnecessárias dos retornos de exceção da api
  - Avaliar melhor forma de disparar o bot, juntamente com o webservice (Procfile, imports e Dockerfile e compose)
  - Implementar os testes automáticos
  - Build da aplicação somente após passar os testes automáticos
