# Roadmap

Agrupamento de necessidades de execução e idéias para o webhook e bot do telegram.

### Prospecção

Relação de necessidades funcionais e não-funcionais:

  - Tornar o Bot em multi clientes
  - avaliar necessidade de estruturar Dockerfile e Compose
  - Avaliar a necessidade do implementar o flask juntamente com o
    gunicorn
  - Avaliar o uso do i18n (via gettext?)

### A Fazer

Relação de necessidades técnicas:

  - Implementar o menu com todos os monitores cadastrados no uptime
  - Separar as mensagens de down e up, das mensagens de ssl
  - Reavaliar a implementação das mensagens
  - Rever as variáveis de ambiente
  - Build da aplicação somente após passar os testes automáticos

### Em Andamento
  - Implementar os testes automáticos
  - Estruturar a implementação dos logs da aplicação


### Feito

  - ~~Remover as mensagens desnecessárias dos retornos de exceção da
  api~~
  - ~~Avaliar melhor forma de disparar o bot, juntamente com o
  webservice (Procfile, imports e Dockerfile e compose)~~
    - **Avaliação**: Para disparar o bot, seria necessário desvincular do flask e o
    uso da variável 'app' e resolver problemas de importação. Por ora,
    em tempo de desenvolvimento e devido a facilidade de disparar os
    dois processos, será mantido assim até a versão 1.0 - stable.