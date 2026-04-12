# Automação de Reconhecimento

Embora o reconhecimento manual possa ser eficaz, ele também pode consumir tempo e estar sujeito a erros humanos. Automatizar tarefas de reconhecimento web pode aumentar significativamente a eficiência e a precisão, permitindo coletar informações em escala e identificar potenciais vulnerabilidades com mais rapidez.

## Por que automatizar o reconhecimento?

A automação oferece várias vantagens importantes para o reconhecimento web:

- **Eficiência:** ferramentas automatizadas executam tarefas repetitivas muito mais rápido que humanos, liberando tempo para análise e tomada de decisão.
- **Escalabilidade:** a automação permite ampliar esforços de reconhecimento para muitos alvos ou domínios, cobrindo uma superfície maior de informação.
- **Consistência:** ferramentas automatizadas seguem regras e procedimentos predefinidos, garantindo resultados consistentes e reproduzíveis, além de reduzir risco de erro humano.
- **Cobertura abrangente:** a automação pode executar diversas tarefas, como enumeração DNS, descoberta de subdomínios, crawling web, varredura de portas e mais.
- **Integração:** muitos frameworks de automação se integram facilmente com outras ferramentas e plataformas, criando um fluxo contínuo entre reconhecimento, avaliação de vulnerabilidades e exploração.

## Frameworks de reconhecimento

Esses frameworks buscam oferecer uma suíte completa para reconhecimento web:

- **FinalRecon:** ferramenta de reconhecimento em Python com módulos para checagem de certificado SSL, coleta de Whois, análise de headers e crawling. Sua estrutura modular facilita customização.
- **Recon-ng:** framework poderoso escrito em Python, com estrutura modular para várias tarefas de reconhecimento. Pode executar enumeração DNS, descoberta de subdomínios, varredura de portas, crawling e até exploração de vulnerabilidades conhecidas.
- **theHarvester:** projetado para coletar endereços de e-mail, subdomínios, hosts, nomes de funcionários, portas abertas e banners em fontes públicas como motores de busca, servidores de chave PGP e SHODAN.
- **SpiderFoot:** ferramenta de automação OSINT de código aberto que integra várias fontes para coletar dados do alvo, incluindo IPs, domínios, e-mails e perfis sociais.
- **OSINT Framework:** coleção de ferramentas e recursos para inteligência de fontes abertas, cobrindo redes sociais, buscadores, registros públicos e muito mais.

## FinalRecon

O FinalRecon oferece uma grande quantidade de informações de reconhecimento:

- **Header Information:** revela detalhes do servidor, tecnologias utilizadas e possíveis falhas de configuração.
- **Whois Lookup:** obtém detalhes de registro de domínio, incluindo dados de registrante e contato.
- **SSL Certificate Information:** analisa o certificado SSL/TLS quanto a validade, emissor e outros detalhes relevantes.
- **Crawler:**
  - **HTML, CSS, JavaScript:** extrai links, recursos e possíveis vulnerabilidades desses arquivos.
  - **Links internos/externos:** mapeia estrutura do site e conexões com outros domínios.
  - **Imagens, robots.txt, sitemap.xml:** coleta informações sobre caminhos permitidos/proibidos e estrutura do site.
  - **Links em JavaScript, Wayback Machine:** encontra links ocultos e dados históricos do site.
- **DNS Enumeration:** consulta mais de 40 tipos de registros DNS, incluindo DMARC para avaliação de segurança de e-mail.
- **Subdomain Enumeration:** utiliza múltiplas fontes de dados (crt.sh, AnubisDB, ThreatMiner, CertSpotter, Facebook API, VirusTotal API, Shodan API, BeVigil API).
- **Directory Enumeration:** suporta wordlists e extensões de arquivo customizadas para encontrar diretórios e arquivos ocultos.
- **Wayback Machine:** recupera URLs dos últimos cinco anos para analisar mudanças do site e possíveis vulnerabilidades.

A instalação é rápida e simples:

```shellsession
JLMreal@htb[/htb]$ git clone https://github.com/thewhiteh4t/FinalRecon.git
JLMreal@htb[/htb]$ cd FinalRecon
JLMreal@htb[/htb]$ pip3 install -r requirements.txt
JLMreal@htb[/htb]$ chmod +x ./finalrecon.py
JLMreal@htb[/htb]$ ./finalrecon.py --help
```

```text
usage: finalrecon.py [-h] [--url URL] [--headers] [--sslinfo] [--whois]
                     [--crawl] [--dns] [--sub] [--dir] [--wayback] [--ps]
                     [--full] [-nb] [-dt DT] [-pt PT] [-T T] [-w W] [-r] [-s]
                     [-sp SP] [-d D] [-e E] [-o O] [-cd CD] [-k K]

FinalRecon - All in One Web Recon | v1.1.6

optional arguments:
  -h, --help  show this help message and exit
  --url URL   Target URL
  --headers   Header Information
  --sslinfo   SSL Certificate Information
  --whois     Whois Lookup
  --crawl     Crawl Target
  --dns       DNS Enumeration
  --sub       Sub-Domain Enumeration
  --dir       Directory Search
  --wayback   Wayback URLs
  --ps        Fast Port Scan
  --full      Full Recon

Extra Options:
  -nb         Hide Banner
  -dt DT      Number of threads for directory enum [ Default : 30 ]
  -pt PT      Number of threads for port scan [ Default : 50 ]
  -T T        Request Timeout [ Default : 30.0 ]
  -w W        Path to Wordlist [ Default : wordlists/dirb_common.txt ]
  -r          Allow Redirect [ Default : False ]
  -s          Toggle SSL Verification [ Default : True ]
  -sp SP      Specify SSL Port [ Default : 443 ]
  -d D        Custom DNS Servers [ Default : 1.1.1.1 ]
  -e E        File Extensions [ Example : txt, xml, php ]
  -o O        Export Format [ Default : txt ]
  -cd CD      Change export directory [ Default : ~/.local/share/finalrecon ]
  -k K        Add API key [ Example : shodan@key ]
```

Para começar, primeiro clone o repositório FinalRecon no GitHub com:

```shellsession
git clone https://github.com/thewhiteh4t/FinalRecon.git
```

Isso cria um diretório chamado `FinalRecon` com todos os arquivos necessários.

Depois, entre no diretório:

```shellsession
cd FinalRecon
```

Em seguida, instale as dependências Python:

```shellsession
pip3 install -r requirements.txt
```

Para garantir que o script principal possa ser executado:

```shellsession
chmod +x ./finalrecon.py
```

Por fim, confira a instalação e veja as opções disponíveis:

```shellsession
./finalrecon.py --help
```

Isso exibirá a ajuda da ferramenta, incluindo módulos e opções de uso.

| Opção | Argumento | Descrição |
|---|---|---|
| `-h`, `--help` | - | Mostra a ajuda e sai. |
| `--url` | `URL` | Especifica a URL alvo. |
| `--headers` | - | Coleta informações de header da URL alvo. |
| `--sslinfo` | - | Coleta informações do certificado SSL da URL alvo. |
| `--whois` | - | Executa consulta Whois do domínio alvo. |
| `--crawl` | - | Faz crawling do site alvo. |
| `--dns` | - | Executa enumeração DNS no domínio alvo. |
| `--sub` | - | Enumera subdomínios do domínio alvo. |
| `--dir` | - | Procura diretórios no site alvo. |
| `--wayback` | - | Recupera URLs históricas via Wayback para o alvo. |
| `--ps` | - | Executa varredura rápida de portas no alvo. |
| `--full` | - | Executa um reconhecimento completo do alvo. |

Por exemplo, se quisermos que o FinalRecon colete headers e faça Whois para `inlanefreight.com`, usamos as flags `--headers` e `--whois`:

```shellsession
JLMreal@htb[/htb]$ ./finalrecon.py --headers --whois --url http://inlanefreight.com
```

```text
 ______  __   __   __   ______   __
/\  ___\/\ \ /\ "-.\ \ /\  __ \ /\ \
\ \  __\\ \ \\ \ \-.  \\ \  __ \\ \ \____
 \ \_\   \ \_\\ \_\\"\_\\ \_\ \_\\ \_____\
  \/_/    \/_/ \/_/ \/_/ \/_/\/_/ \/_____/
 ______   ______   ______   ______   __   __
/\  == \ /\  ___\ /\  ___\ /\  __ \ /\ "-.\ \
\ \  __< \ \  __\ \ \ \____\ \ \/\ \\ \ \-.  \
 \ \_\ \_\\ \_____\\ \_____\\ \_____\\ \_\\"\_\
  \/_/ /_/ \/_____/ \/_____/ \/_____/ \/_/ \/_/

[>] Created By   : thewhiteh4t
 |---> Twitter   : https://twitter.com/thewhiteh4t
 |---> Community : https://twc1rcle.com/
[>] Version      : 1.1.6

[+] Target : http://inlanefreight.com

[+] IP Address : 134.209.24.248

[!] Headers :

Date : Tue, 11 Jun 2024 10:08:00 GMT
Server : Apache/2.4.41 (Ubuntu)
Link : <https://www.inlanefreight.com/index.php/wp-json/>; rel="https://api.w.org/", <https://www.inlanefreight.com/index.php/wp-json/wp/v2/pages/7>; rel="alternate"; type="application/json", <https://www.inlanefreight.com/>; rel=shortlink
Vary : Accept-Encoding
Content-Encoding : gzip
Content-Length : 5483
Keep-Alive : timeout=5, max=100
Connection : Keep-Alive
Content-Type : text/html; charset=UTF-8

[!] Whois Lookup :

   Domain Name: INLANEFREIGHT.COM
   Registry Domain ID: 2420436757_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.registrar.amazon.com
   Registrar URL: http://registrar.amazon.com
   Updated Date: 2023-07-03T01:11:15Z
   Creation Date: 2019-08-05T22:43:09Z
   Registry Expiry Date: 2024-08-05T22:43:09Z
   Registrar: Amazon Registrar, Inc.
   Registrar IANA ID: 468
   Registrar Abuse Contact Email: abuse@amazonaws.com
   Registrar Abuse Contact Phone: +1.2024422253
   Domain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Domain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited
   Name Server: NS-1303.AWSDNS-34.ORG
   Name Server: NS-1580.AWSDNS-05.CO.UK
   Name Server: NS-161.AWSDNS-20.COM
   Name Server: NS-671.AWSDNS-19.NET
   DNSSEC: unsigned
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/


[+] Completed in 0:00:00.257780

[+] Exported : /home/htb-ac-643601/.local/share/finalrecon/dumps/fr_inlanefreight.com_11-06-2024_11:07:59
```
