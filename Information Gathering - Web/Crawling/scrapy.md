# Scrapy

## O que esse recurso faz

**Scrapy** é um framework em Python para **crawling** e **extração de dados** em aplicações web.  
No contexto de reconhecimento, ele permite:

- Navegar automaticamente por links (spidering).
- Coletar URLs, parâmetros, títulos, metadados e conteúdos de páginas.
- Estruturar saída em formatos como JSON, CSV e outros pipelines.
- Escalar a coleta com concorrência e regras de profundidade.

Em resumo, ele acelera o mapeamento de superfície de uma aplicação.

## Requisitos para executar

### Requisitos técnicos

- **Python 3.8+** (recomendado 3.10+).
- **pip** para instalar dependências.
- Ambiente Linux/macOS/Windows com acesso de rede ao alvo.
- (Recomendado) **venv** para isolar dependências.

### Fluxo informado pela HTB (ReconSpider)

Segundo o material da HTB, o uso segue estes 4 comandos:

```bash
pip3 install scrapy
wget -O ReconSpider.zip https://academy.hackthebox.com/storage/modules/144/ReconSpider.v1.2.zip
unzip ReconSpider.zip
python3 ReconSpider.py http://inlanefreight.com
```

Interpretação correta:

- **Comandos 1 a 3:** requisitos/preparação do ambiente.
- **Comando 4:** execução da ferramenta.

### Requisitos operacionais

- **Autorização explícita** para testar o alvo.
- Definição de escopo (domínios, limites de rota e volume de requisições).
- Registro de execução (logs e horários) para auditoria.

## Risco de detecção (deixe isso claro)

O uso de Scrapy tem **alto potencial de detecção** quando mal configurado.

Motivos principais:

- Padrão de requisições automatizadas e repetitivas.
- Volume de tráfego acima do comportamento humano.
- Assinatura de crawler em headers/User-Agent (se não tratada).
- Acesso a rotas sensíveis ou não navegáveis via fluxo normal.
- Geração de eventos em WAF, IDS/IPS, SIEM e logs de aplicação.

### O que aumenta o risco

- Alta concorrência (`CONCURRENT_REQUESTS` elevado).
- Sem atraso entre requisições (`DOWNLOAD_DELAY = 0`).
- Falhas repetidas (muitos 401/403/404/429).
- Execução em horários incomuns e origem de IP não usual.

### Boa prática em teste autorizado

- Reduzir taxa de requisições.
- Respeitar escopo e janelas acordadas.
- Monitorar respostas `429` e sinais de bloqueio.
- Pausar ao identificar impacto no serviço.

> **Conclusão:** Scrapy é muito eficiente para reconhecimento, mas é facilmente perceptível por mecanismos de defesa se usado de forma agressiva.
