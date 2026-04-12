# Introdução ao Web Fuzzing

O web fuzzing é uma técnica crítica de segurança em aplicações web para identificar vulnerabilidades por meio de testes com diferentes entradas. Ele automatiza o envio de dados inesperados ou aleatórios para detectar falhas potenciais que invasores poderiam explorar.

## Fuzzing vs. Força Bruta

Embora os termos sejam usados como sinônimos em muitos contextos, há diferenças importantes:

- **Fuzzing:** abordagem mais ampla. Envia entradas inesperadas (dados malformados, caracteres inválidos e combinações sem sentido) para observar como a aplicação reage e revelar falhas no tratamento de entrada. Ferramentas de fuzzing costumam usar wordlists com padrões comuns, mutações de parâmetros existentes ou sequências aleatórias para gerar payloads diversos.
- **Força bruta:** abordagem mais direcionada. Testa sistematicamente várias possibilidades para um valor específico, como senha ou ID. Ferramentas de força bruta normalmente usam listas e dicionários predefinidos para acertar o valor por tentativa e erro.

## Por que fazer fuzzing em aplicações web?

Aplicações web sustentam operações críticas e processam grandes volumes de dados sensíveis. Pela complexidade e interconexão, também são alvos frequentes de ataques. O fuzzing ajuda a ampliar a cobertura de testes de segurança:

- **Descoberta de vulnerabilidades ocultas:** pode encontrar falhas que métodos tradicionais não identificam.
- **Automação de testes de segurança:** economiza tempo e recursos ao automatizar geração e envio de entradas de teste.
- **Simulação de ataques reais:** reproduz técnicas usadas por atacantes e permite corrigir fraquezas antes da exploração.
- **Fortalecimento da validação de entrada:** evidencia fraquezas em validações, reduzindo risco de SQL Injection e XSS.
- **Melhoria da qualidade do código:** expõe bugs e erros, contribuindo para código mais robusto e seguro.
- **Segurança contínua:** pode ser integrado ao SDLC e pipelines de CI/CD para testes frequentes e detecção precoce de falhas.

## Conceitos essenciais

Antes da parte prática, é importante dominar os conceitos abaixo:

| Conceito | Descrição | Exemplo |
| --- | --- | --- |
| **Wordlist** | Dicionário/lista de palavras, frases, nomes de arquivos, diretórios ou valores de parâmetros usados como entrada durante o fuzzing. | Genérico: `admin`, `login`, `password`, `backup`, `config`<br>Específico da aplicação: `productID`, `addToCart`, `checkout` |
| **Payload** | Dado enviado para a aplicação durante o fuzzing; pode ser string simples, valor numérico ou estrutura complexa. | `' OR 1=1 --` (SQL Injection) |
| **Análise de resposta** | Avaliação das respostas da aplicação (códigos de status, mensagens de erro etc.) para identificar anomalias que indiquem vulnerabilidades. | Normal: `200 OK`<br>Erro (potencial SQLi): `500 Internal Server Error` com mensagem de banco |
| **Fuzzer** | Ferramenta que automatiza geração/envio de payloads e análise de respostas. | `ffuf`, `wfuzz`, `Burp Suite Intruder` |
| **Falso positivo** | Resultado marcado incorretamente como vulnerabilidade. | Erro `404 Not Found` para diretório inexistente |
| **Falso negativo** | Vulnerabilidade real que não foi detectada pelo fuzzer. | Falha lógica sutil em função de processamento de pagamento |
| **Escopo de fuzzing** | Partes específicas da aplicação escolhidas para testes de fuzzing. | Testar apenas a página de login ou um endpoint específico de API |
