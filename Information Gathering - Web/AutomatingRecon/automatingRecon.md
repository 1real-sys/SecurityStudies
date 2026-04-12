# Automação de Reconhecimento Web

Embora o reconhecimento manual possa ser eficaz, ele também pode consumir muito tempo e estar sujeito a erro humano. Automatizar tarefas de reconhecimento web aumenta a eficiência e a precisão, permitindo coletar informações em escala e identificar vulnerabilidades potenciais com mais rapidez.

## Por que automatizar o reconhecimento?

A automação oferece vantagens importantes:

- **Eficiência:** tarefas repetitivas são executadas muito mais rápido.
- **Escalabilidade:** facilita analisar muitos alvos e domínios.
- **Consistência:** reduz variações de execução e minimiza erro humano.
- **Cobertura ampla:** combina DNS, subdomínios, crawling, portas e outros vetores.
- **Integração:** conecta facilmente com ferramentas de avaliação e exploração.

## Frameworks de reconhecimento

| Ferramenta | Descrição |
|---|---|
| **FinalRecon** | Ferramenta em Python com módulos para headers, SSL, Whois, crawling, DNS, subdomínios, diretórios e Wayback. |
| **Recon-ng** | Framework modular em Python para múltiplas tarefas de reconhecimento, incluindo DNS, subdomínios, portas e crawling. |
| **theHarvester** | Coleta e-mails, subdomínios, hosts, nomes de funcionários, portas e banners em fontes públicas. |
| **SpiderFoot** | Plataforma de automação OSINT que integra várias fontes para coletar dados de alvo. |
| **OSINT Framework** | Conjunto de recursos para inteligência de fontes abertas (redes sociais, buscadores, registros públicos etc.). |

## FinalRecon em foco

O FinalRecon oferece uma cobertura rica de informações:

- **Header Information:** identifica servidor, tecnologias e sinais de má configuração.
- **Whois Lookup:** coleta dados de registro de domínio.
- **SSL Certificate Information:** avalia validade, emissor e detalhes do certificado.
- **Crawler:**
  - HTML/CSS/JavaScript: extrai links e recursos.
  - Links internos/externos: mapeia estrutura e relacionamentos.
  - Imagens, `robots.txt`, `sitemap.xml`: revela rotas e estrutura do site.
  - Links em JavaScript e Wayback: ajuda a descobrir URLs ocultas e históricas.
- **DNS Enumeration:** consulta dezenas de tipos de registros (incluindo DMARC).
- **Subdomain Enumeration:** usa múltiplas fontes (crt.sh, AnubisDB, ThreatMiner, CertSpotter, APIs etc.).
- **Directory Enumeration:** suporta wordlists e extensões customizadas.
- **Wayback Machine:** recupera URLs históricas para análise de mudanças.

## Instalação rápida

```shellsession
git clone https://github.com/thewhiteh4t/FinalRecon.git
cd FinalRecon
pip3 install -r requirements.txt
chmod +x ./finalrecon.py
./finalrecon.py --help
```

## Opções mais usadas

| Opção | Argumento | Descrição |
|---|---|---|
| `-h`, `--help` | - | Mostra a ajuda e sai. |
| `--url` | `URL` | Define a URL alvo. |
| `--headers` | - | Coleta cabeçalhos HTTP. |
| `--sslinfo` | - | Coleta informações do certificado SSL/TLS. |
| `--whois` | - | Executa consulta Whois. |
| `--crawl` | - | Faz crawling do alvo. |
| `--dns` | - | Executa enumeração DNS. |
| `--sub` | - | Enumera subdomínios. |
| `--dir` | - | Busca diretórios. |
| `--wayback` | - | Coleta URLs históricas via Wayback. |
| `--ps` | - | Executa varredura rápida de portas. |
| `--full` | - | Executa reconhecimento completo. |

## Exemplo de uso

Para coletar headers e Whois de um domínio:

```shellsession
./finalrecon.py --headers --whois --url http://inlanefreight.com
```

Esse comando normalmente retorna IP do alvo, cabeçalhos HTTP e dados de registro do domínio, além de exportar os resultados para um diretório local.
