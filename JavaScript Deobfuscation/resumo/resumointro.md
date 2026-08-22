# Introdução à desofuscação de JavaScript

## O que é

Desofuscação é o processo de transformar um código deliberadamente difícil de ler em uma representação mais clara, preservando e compreendendo seu comportamento.

O objetivo não é apenas “embelezar” o código. Uma análise completa busca responder:

- quais dados o código recebe;
- quais transformações ele realiza;
- quais funções são executadas;
- com quais recursos externos ele se comunica;
- qual é seu efeito final.

## Por que é importante

Código JavaScript ofuscado aparece em diferentes contextos:

- proteção de lógica proprietária;
- redução e empacotamento de aplicações web;
- desafios de CTF e laboratórios;
- tentativas de ocultar indicadores e comportamentos maliciosos;
- malware que carrega ou reconstrói um payload em etapas.

Em atividades de red team, a análise pode revelar endpoints, parâmetros, tokens, validações executadas no cliente e funcionalidades ocultas. Em blue team e resposta a incidentes, pode ajudar a identificar indicadores de comprometimento, URLs externas, mecanismos de persistência e estágios de execução.

## Ofuscação não é criptografia

Esses conceitos não são equivalentes:

- **Ofuscação:** dificulta a leitura e a análise, mas o navegador ainda precisa conseguir executar o código.
- **Codificação:** representa dados em outro formato, como Base64 ou hexadecimal, sem necessariamente oferecer sigilo.
- **Criptografia:** protege o conteúdo com um algoritmo e, normalmente, uma chave.
- **Minificação:** reduz o tamanho do arquivo removendo espaços e encurtando identificadores; pode prejudicar a leitura sem ter a intenção principal de esconder o comportamento.

Um código pode combinar vários desses mecanismos.

## Fluxo básico de análise

1. Identificar onde o JavaScript está localizado.
2. Preservar uma cópia do conteúdo original para comparação.
3. Formatar o código para tornar sua estrutura visível.
4. Localizar strings, funções, variáveis e pontos de entrada importantes.
5. Reconhecer camadas de codificação ou construção dinâmica de código.
6. Desofuscar uma camada por vez.
7. Acompanhar o fluxo de dados e as chamadas de rede.
8. Reproduzir manualmente apenas as partes necessárias para confirmar o comportamento.

## Onde localizar JavaScript

O código pode aparecer:

- diretamente entre tags `<script>` no HTML;
- em arquivos externos referenciados por `src`;
- em atributos de eventos, como `onclick`;
- carregado dinamicamente por outras funções;
- retornado por uma API ou reconstruído em tempo de execução.

As ferramentas de desenvolvedor do navegador ajudam a inspecionar o DOM, os scripts carregados e as requisições HTTP.

## O que observar em código ofuscado

- nomes de variáveis sem significado;
- grandes arrays de strings;
- acessos indiretos a propriedades;
- strings em Base64, hexadecimal ou percent-encoding;
- uso de `eval()`, `Function()` ou timers com strings;
- concatenações que constroem URLs ou nomes de funções;
- múltiplas camadas de decodificação;
- requisições feitas por `fetch()`, `XMLHttpRequest` ou bibliotecas externas.

A presença desses padrões não prova comportamento malicioso. Eles são pontos de investigação.

## Cuidados durante a análise

Executar código desconhecido diretamente no navegador ou no sistema pode produzir efeitos indesejados. Em laboratórios, prefira:

- trabalhar em ambiente isolado;
- analisar estaticamente antes de executar;
- evitar inserir segredos ou credenciais reais;
- observar requisições de rede;
- substituir chamadas perigosas por registros ou valores controlados quando possível;
- manter o código original inalterado para comparação.

## Conteúdo previsto no módulo

- localização de código JavaScript;
- fundamentos de ofuscação;
- técnicas de desofuscação;
- decodificação de mensagens;
- análise básica de código;
- envio e interpretação de requisições HTTP básicas.

## Pontos-chave para revisão

- Desofuscar significa recuperar legibilidade e compreender comportamento.
- O navegador precisa interpretar o código ofuscado, o que permite estudar suas transformações.
- Formatar o código é apenas o começo; o objetivo real é entender o fluxo de dados e os efeitos.
- Codificação, criptografia, minificação e ofuscação possuem finalidades diferentes.
- Código desconhecido deve ser analisado em um ambiente controlado e autorizado.
