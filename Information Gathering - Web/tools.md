# Inventário de Ferramentas (arquivos *Copia)

Arquivos analisados: `AutomatingRecon/automatingReconCopia.md`, `Crawling/CRAWLINGCopia.md`, `Crawling/RobotsCopia.md`, `Crawling/SearchEngineCopia.md`, `Crawling/Well-KnownCopia.md`, `DNS/BruteForceSubDomainCopia.md`, `DNS/CertificateTransparencyCopia.md`, `DNS/DigDNSCopia.md`, `DNS/DNSzoneCopia.md`, `DNS/SubDomainCopia.md`, `DNS/virtualHostsCopia.md`, `FingerPrint/FingerprintCopia.md`.

**Legenda de detecção:** 🟢 não detectável/discreto · 🟡 detectável · 🔴 detectável com risco de banimento e rastreio

| Ferramenta | Grau | Caso de uso | Comando exemplo |
| --- | --- | --- | --- |
| Wappalyzer | 🟢 | Fingerprinting de tecnologias web (CMS, frameworks, analytics). | `wappalyzer https://alvo.com` |
| BuiltWith | 🟢 | Perfil tecnológico de um domínio via serviço externo. | `xdg-open "https://builtwith.com/alvo.com"` |
| WhatWeb | 🟡 | Fingerprinting ativo de stack web por assinaturas. | `whatweb -a 3 https://alvo.com` |
| Nmap | 🔴 | Descoberta de serviços/versões e mapeamento de portas. | `nmap -sV -p 80,443 alvo.com` |
| Netcraft | 🟢 | Consulta de relatório externo de tecnologia e hosting. | `xdg-open "https://sitereport.netcraft.com/?url=alvo.com"` |
| wafw00f | 🟡 | Identificação de WAF na frente da aplicação. | `wafw00f https://alvo.com` |
| Nikto | 🔴 | Scanner web com checks conhecidos de vulnerabilidades/configuração. | `nikto -h https://alvo.com -Tuning b` |
| curl | 🟢 | Coleta de headers/banner e validação rápida de resposta HTTP. | `curl -I https://alvo.com` |
| dnsenum | 🟡 | Enumeração DNS e força bruta de subdomínios. | `dnsenum --enum alvo.com -f wordlist.txt -r` |
| ffuf | 🟡 | Fuzzing de diretórios, parâmetros e virtual hosts. | `ffuf -u https://alvo.com/FUZZ -w wordlist.txt` |
| gobuster | 🟡 | Descoberta de diretórios/subdomínios/vhosts por wordlist. | `gobuster vhost -u http://10.10.10.10 -w wordlist.txt --append-domain` |
| crt.sh | 🟢 | Enumeração passiva de subdomínios via CT logs. | `curl -s "https://crt.sh/?q=alvo.com&output=json" | jq -r '.[].name_value'` |
| Censys | 🟢 | Pesquisa de certificados/hosts por base externa. | `xdg-open "https://search.censys.io/search?resource=hosts&q=alvo.com"` |
| jq | 🟢 | Parse/filtragem local de JSON em pipelines OSINT. | `jq -r '.[].name_value' resultado.json` |
| Google | 🟢 | OSINT com dorks para achar superfícies expostas. | `xdg-open 'https://www.google.com/search?q=site%3Aalvo.com+inurl%3Alogin'` |
| DuckDuckGo | 🟢 | Descoberta passiva de subdomínios e páginas indexadas. | `xdg-open 'https://duckduckgo.com/?q=site%3Aalvo.com'` |
| dig | 🟡 | Consulta DNS detalhada, troubleshooting e tentativa AXFR. | `dig axfr @ns1.alvo.com alvo.com` |
| nslookup | 🟡 | Consultas DNS básicas (A/AAAA/MX). | `nslookup -type=MX alvo.com` |
| host | 🟡 | Verificação rápida de resolução DNS e registros. | `host -t A alvo.com` |
| fierce | 🟡 | Enumeração recursiva de subdomínios com detecção de wildcard. | `fierce --domain alvo.com` |
| dnsrecon | 🟡 | Reconhecimento DNS com múltiplas técnicas e relatórios. | `dnsrecon -d alvo.com -t brt -D wordlist.txt` |
| amass | 🟡 | Enumeração de subdomínios (passiva/ativa). | `amass enum -d alvo.com` |
| assetfinder | 🟢 | Descoberta rápida e passiva de subdomínios. | `assetfinder --subs-only alvo.com` |
| puredns | 🔴 | Força bruta DNS em alto volume com resolução/filtragem. | `puredns bruteforce wordlist.txt alvo.com` |
| theHarvester | 🟢 | Coleta OSINT (e-mails, hosts, subdomínios, fontes públicas). | `theHarvester -d alvo.com -b all` |
| FinalRecon | 🟡 | Recon web automatizado (headers, whois, dns, crawl, subdomínios). | `finalrecon.py --headers --whois --url https://alvo.com` |
| Recon-ng | 🟡 | Framework modular de reconhecimento/OSINT. | `recon-ng` |
| SpiderFoot | 🟡 | Automação OSINT com múltiplas fontes e correlação. | `spiderfoot -l 127.0.0.1:5001` |
| OSINT Framework | 🟢 | Catálogo de fontes/ferramentas OSINT para investigação. | `xdg-open "https://osintframework.com/"` |
| Feroxbuster | 🔴 | Descoberta recursiva de conteúdo com alto volume de requisições. | `feroxbuster -u https://alvo.com -w wordlist.txt -t 50` |

> Nota: o grau de detecção varia com taxa de requisições, volume, recursão, user-agent, distribuição de origem (IP/proxy) e presença de WAF/IDS/SIEM no alvo.
