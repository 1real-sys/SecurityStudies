# RESUMO - Reconhecimento DNS

Este resumo abrange as principais técnicas e ferramentas para reconhecimento DNS em testes de penetração e segurança web.

---

## 1. Fundamentos do DNS

O Sistema de Nomes de Domínio (DNS) traduz nomes de domínio legíveis (www.example.com) em endereços IP numéricos (192.0.2.1).

### Fluxo de Resolução DNS

1. **Consulta DNS:** Computador verifica cache local, se não encontrar, consulta o resolvedor DNS (ISP)
2. **Servidor Raiz:** Aponta para o servidor TLD correto (.com, .org, etc.)
3. **Servidor TLD:** Indica o servidor autoritativo do domínio
4. **Servidor Autoritativo:** Retorna o endereço IP real
5. **Resposta:** IP retorna pela cadeia até o computador

### Arquivo Hosts

Mapeamento manual de nomes para IPs, ignorando o DNS.

| Sistema | Localização |
|---------|-------------|
| Windows | `C:\Windows\System32\drivers\etc\hosts` |
| Linux/Mac | `/etc/hosts` |

**Formato:**
```
192.168.1.10    devserver.local
0.0.0.0         site-bloqueado.com
```

### Tipos de Registros DNS

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| **A** | Mapeia hostname → IPv4 | `www.example.com. IN A 192.0.2.1` |
| **AAAA** | Mapeia hostname → IPv6 | `www.example.com. IN AAAA 2001:db8::1` |
| **CNAME** | Alias para outro hostname | `blog.example.com. IN CNAME webserver.example.net.` |
| **MX** | Servidor de e-mail | `example.com. IN MX 10 mail.example.com.` |
| **NS** | Servidor de nomes autoritativo | `example.com. IN NS ns1.example.com.` |
| **TXT** | Texto arbitrário (SPF, DKIM) | `example.com. IN TXT "v=spf1 mx -all"` |
| **SOA** | Início de autoridade da zona | Informações administrativas da zona |
| **PTR** | DNS reverso (IP → hostname) | `1.2.0.192.in-addr.arpa. IN PTR www.example.com.` |
| **SRV** | Localização de serviços | `_sip._udp.example.com. IN SRV 10 5 5060 sipserver.example.com.` |

---

## 2. Ferramentas de Consulta DNS

### Tabela Comparativa

| Ferramenta | Descrição | Uso Principal |
|------------|-----------|---------------|
| **dig** | Consulta versátil, saída detalhada | Análise aprofundada, troubleshooting |
| **nslookup** | Consulta simples | Verificações rápidas |
| **host** | Saída concisa | Consultas básicas |
| **dnsenum** | Enumeração automatizada | Descoberta de subdomínios |
| **fierce** | Busca recursiva | Identificação de alvos |
| **dnsrecon** | Múltiplas técnicas | Enumeração abrangente |
| **theHarvester** | OSINT | Coleta de e-mails e informações |

### Comando dig - Referência Completa

```bash
# Consultas básicas
dig domain.com              # Registro A padrão
dig domain.com A            # IPv4
dig domain.com AAAA         # IPv6
dig domain.com MX           # Servidores de e-mail
dig domain.com NS           # Servidores de nome
dig domain.com TXT          # Registros TXT
dig domain.com CNAME        # Nome canônico
dig domain.com SOA          # Início de autoridade
dig domain.com ANY          # Todos os registros (pode ser ignorado)

# Opções avançadas
dig @1.1.1.1 domain.com     # Usar DNS específico
dig +trace domain.com       # Caminho completo da resolução
dig -x 192.168.1.1          # Consulta reversa (IP → hostname)
dig +short domain.com       # Resposta curta
dig +noall +answer domain.com  # Apenas seção de resposta
```

### Interpretando a Saída do dig

```bash
dig google.com

;; HEADER: opcode: QUERY, status: NOERROR, id: 16449
;; flags: qr rd ad; QUERY: 1, ANSWER: 1

;; QUESTION SECTION:
;google.com.                    IN      A

;; ANSWER SECTION:
google.com.             0       IN      A       142.251.47.142

;; Query time: 0 msec
;; SERVER: 172.23.176.1#53 (UDP)
```

| Seção | Significado |
|-------|-------------|
| **Header** | Status (NOERROR = sucesso), flags (qr=resposta, rd=recursão, ad=dados autênticos) |
| **Question** | A pergunta feita ao DNS |
| **Answer** | Resposta com IP e TTL |
| **Footer** | Tempo, servidor usado, tamanho |

---

## 3. Subdomínios

Subdomínios (blog.example.com, dev.example.com) frequentemente hospedam:
- Ambientes de desenvolvimento/staging com segurança relaxada
- Portais administrativos ocultos
- Aplicações legadas vulneráveis
- Informações sensíveis expostas

### Métodos de Enumeração

| Tipo | Descrição | Vantagens | Desvantagens |
|------|-----------|-----------|--------------|
| **Ativa** | Interage com servidores DNS (força bruta, transferência de zona) | Mais controle, descoberta abrangente | Mais detectável |
| **Passiva** | Fontes externas (CT logs, motores de busca) | Mais furtiva | Pode não encontrar todos |

---

## 4. Força Bruta de Subdomínios

### Processo

1. **Seleção de Wordlist:** Propósito geral, direcionada ou personalizada
2. **Iteração:** Anexa cada palavra ao domínio (dev.example.com)
3. **Consulta DNS:** Verifica se resolve para um IP
4. **Validação:** Confirma existência e funcionalidade

### Ferramentas

| Ferramenta | Descrição |
|------------|-----------|
| **dnsenum** | Enumeração completa com força bruta |
| **fierce** | Descoberta recursiva com detecção de wildcard |
| **dnsrecon** | Múltiplas técnicas combinadas |
| **amass** | Descoberta avançada com integração de fontes |
| **puredns** | Força bruta rápida e filtragem eficiente |

### DNSEnum - Comandos

```bash
# Enumeração com força bruta recursiva
dnsenum --enum inlanefreight.com -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -r
```

**Parâmetros:**
- `--enum`: Modo de enumeração
- `-f`: Caminho para wordlist
- `-r`: Força bruta recursiva (enumera subdomínios de subdomínios)

**Funcionalidades do dnsenum:**
- Recupera registros A, AAAA, NS, MX, TXT
- Tenta transferências de zona
- Scraping do Google
- Lookup DNS reverso
- Consultas WHOIS

---

## 5. Transferência de Zona DNS

Uma transferência de zona (AXFR) copia **todos** os registros DNS de uma zona. Se mal configurada, expõe informações sensíveis.

### Informações Reveladas

- Lista completa de subdomínios
- Endereços IP associados
- Servidores de nomes e configurações
- Ambientes de desenvolvimento ocultos

### Comando para Testar

```bash
dig axfr @servidor_dns dominio.com

# Exemplo com servidor de teste
dig axfr @nsztm1.digi.ninja zonetransfer.me
```

### Saída de Exemplo

```
zonetransfer.me.    7200    IN  SOA  nsztm1.digi.ninja. robin.digi.ninja.
zonetransfer.me.    7200    IN  NS   nsztm1.digi.ninja.
zonetransfer.me.    7200    IN  A    5.196.105.14
asfdbbox.zonetransfer.me.   7200    IN  A    127.0.0.1
canberra-office.zonetransfer.me. 7200 IN A  202.14.81.230
```

> **Nota:** A maioria dos servidores modernos bloqueia transferências não autorizadas.

---

## 6. Logs de Transparência de Certificados (CT)

Registros públicos que armazenam todos os certificados SSL/TLS emitidos.

### Vantagens para Reconhecimento

- Registro **definitivo** de certificados (não depende de wordlist)
- Visão **histórica** dos subdomínios
- Revela subdomínios de certificados **antigos/expirados**

### Ferramentas

| Ferramenta | Descrição | Prós | Contras |
|------------|-----------|------|---------|
| **crt.sh** | Interface web gratuita | Fácil, sem registro | Filtragem limitada |
| **Censys** | Busca avançada com API | Dados extensivos | Requer registro |

### Consulta via API (crt.sh)

```bash
# Buscar todos os subdomínios de um domínio
curl -s "https://crt.sh/?q=facebook.com&output=json" | jq -r '.[].name_value' | sort -u

# Filtrar subdomínios contendo "dev"
curl -s "https://crt.sh/?q=facebook.com&output=json" | jq -r '.[]
 | select(.name_value | contains("dev")) | .name_value' | sort -u
```

**Explicação:**
- `curl -s`: Busca silenciosa do JSON
- `jq -r '.[].name_value'`: Extrai campo name_value
- `select(.name_value | contains("dev"))`: Filtra por string
- `sort -u`: Ordena e remove duplicatas

---

## 7. Virtual Hosts (VHosts)

Permite múltiplos sites no mesmo servidor/IP usando o cabeçalho HTTP `Host`.

### Diferença entre Subdomínios e VHosts

| Aspecto | Subdomínio | Virtual Host |
|---------|------------|--------------|
| **DNS** | Precisa de registro DNS | Pode não ter registro DNS |
| **Configuração** | Definido no DNS | Definido no servidor web |
| **Descoberta** | Consultas DNS | Fuzzing do cabeçalho Host |

### Tipos de Virtual Hosting

| Tipo | Descrição | Vantagens | Desvantagens |
|------|-----------|-----------|--------------|
| **Baseado em Nome** | Diferencia pelo cabeçalho Host | Econômico, flexível | Limitações com SSL/TLS |
| **Baseado em IP** | IP único por site | Qualquer protocolo | Caro, menos escalável |
| **Baseado em Porta** | Porta diferente por site | Útil com IPs limitados | Menos amigável |

### Ferramentas de Descoberta

| Ferramenta | Descrição |
|------------|-----------|
| **gobuster** | Força bruta rápida com múltiplos métodos |
| **feroxbuster** | Implementação em Rust, recursão e filtros |
| **ffuf** | Fuzzer rápido com opções customizáveis |

### Gobuster - Força Bruta de VHosts

```bash
# Comando básico
gobuster vhost -u http://<IP_ALVO> -w <WORDLIST> --append-domain

# Exemplo completo
gobuster vhost -u http://inlanefreight.htb:81 -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain

# Com opções adicionais
gobuster vhost -u http://alvo.com -w wordlist.txt --append-domain -t 50 -k -o resultados.txt
```

**Parâmetros:**
- `-u`: URL alvo
- `-w`: Arquivo wordlist
- `--append-domain`: Anexa domínio base a cada palavra (obrigatório em versões novas)
- `-t`: Número de threads
- `-k`: Ignora erros de certificado SSL
- `-o`: Salva saída em arquivo

### Configuração do /etc/hosts

Para acessar VHosts sem DNS público:

```bash
# Adicionar ao /etc/hosts
echo "192.168.1.100 alvo.htb" | sudo tee -a /etc/hosts

# Ou editar manualmente
sudo nano /etc/hosts
# Adicionar: 192.168.1.100    alvo.htb
```

---

## 8. Importância do DNS no Reconhecimento

| Objetivo | Como o DNS Ajuda |
|----------|------------------|
| **Descobrir Ativos** | Registros revelam subdomínios, servidores de e-mail, etc. |
| **Mapear Infraestrutura** | Identificar provedores, balanceadores, conexões entre sistemas |
| **Monitorar Mudanças** | Novos subdomínios podem indicar novos pontos de entrada |
| **Identificar Vulnerabilidades** | CNAMEs para servidores antigos, certificados expirados |

---

## 9. Ferramentas e Risco de Detecção

### Tabela de Detecção (Mais Chamativo → Menos Chamativo)

| Risco | Ferramenta | Tipo | Motivo | Detectável por |
|:-----:|------------|------|--------|----------------|
| 🔴 **ALTO** | **gobuster vhost** | Ativa | Milhares de requisições HTTP com Headers diferentes | WAF, IDS, Rate Limiting, Logs do servidor |
| 🔴 **ALTO** | **feroxbuster** | Ativa | Similar ao gobuster, alto volume de requisições | WAF, IDS, Rate Limiting |
| 🔴 **ALTO** | **ffuf** | Ativa | Fuzzing agressivo de headers/parâmetros | WAF, IDS, Firewall |
| 🟠 **MÉDIO-ALTO** | **dnsenum** | Ativa | Múltiplas consultas DNS + scraping Google | DNS Firewall, Rate Limiting DNS |
| 🟠 **MÉDIO-ALTO** | **fierce** | Ativa | Enumeração recursiva gera muitas consultas | DNS Firewall, Logs DNS |
| 🟠 **MÉDIO-ALTO** | **dnsrecon** | Ativa | Combina várias técnicas (transferência, força bruta) | DNS Firewall, IDS |
| 🟡 **MÉDIO** | **amass** | Mista | Combina ativa + passiva, pode ser configurado | Depende da configuração |
| 🟡 **MÉDIO** | **dig axfr** | Ativa | Tentativa de transferência de zona é logada | Logs DNS, alertas de segurança |
| 🟢 **BAIXO** | **dig** (consultas simples) | Ativa | Consultas individuais são normais | Quase indetectável (tráfego normal) |
| 🟢 **BAIXO** | **nslookup / host** | Ativa | Consultas básicas, tráfego comum | Quase indetectável |
| 🟢 **BAIXO** | **theHarvester** | Passiva | Coleta de fontes públicas (não toca o alvo diretamente) | Não detectável pelo alvo |
| ⚪ **NENHUM** | **crt.sh / Censys** | Passiva | Consulta bancos de dados públicos externos | Impossível detectar |
| ⚪ **NENHUM** | **Google Dorks** | Passiva | Busca em motor de busca | Impossível detectar |

### Estratégia Recomendada (Stealth → Agressivo)

```
1. PASSIVO PRIMEIRO (Zero detecção)
   └── crt.sh, Censys, Google Dorks, theHarvester
   
2. CONSULTAS LEVES (Baixa detecção)
   └── dig, nslookup, host (consultas individuais)
   
3. ENUMERAÇÃO MODERADA (Média detecção)
   └── dig axfr, amass (modo passivo)
   
4. FORÇA BRUTA (Alta detecção - SOMENTE COM AUTORIZAÇÃO)
   └── dnsenum, fierce, dnsrecon, gobuster, ffuf
```

### Dicas para Reduzir Detecção

| Técnica | Comando/Configuração |
|---------|---------------------|
| Reduzir velocidade | `gobuster vhost ... -t 5` (menos threads) |
| Delays entre requisições | `ffuf -rate 10` (10 req/segundo) |
| Usar DNS diferente | `dig @8.8.8.8 dominio.com` (não usa DNS do alvo) |
| Randomizar User-Agent | Configurar headers customizados |
| Usar VPN/Proxy | Mascarar origem das requisições |

---

## 10. Comandos Rápidos - Referência

```bash
# === PASSIVO (Sem detecção) ===
# Subdomínios via CT logs
curl -s "https://crt.sh/?q=dominio.com&output=json" | jq -r '.[].name_value' | sort -u

# === BAIXA DETECÇÃO ===
# Consulta DNS básica
dig +short dominio.com

# Todos os registros
dig dominio.com ANY

# === MÉDIA DETECÇÃO ===
# Transferência de zona (logado pelo servidor)
dig axfr @ns1.dominio.com dominio.com

# === ALTA DETECÇÃO (requer autorização) ===
# Força bruta com dnsenum
dnsenum --enum dominio.com -f wordlist.txt -r

# Força bruta de VHosts
gobuster vhost -u http://IP -w wordlist.txt --append-domain

# === CONFIGURAÇÃO LOCAL ===
# Configurar hosts local
echo "IP dominio.local" | sudo tee -a /etc/hosts
```

---

## 10. Considerações de Segurança

> ⚠️ **Importante:**
> - Alguns servidores detectam e bloqueiam consultas DNS excessivas
> - Descoberta de VHosts pode ser detectada por IDS/WAF
> - **Sempre obtenha autorização** antes de realizar reconhecimento extensivo
> - Respeite limites de taxa (rate limits)
