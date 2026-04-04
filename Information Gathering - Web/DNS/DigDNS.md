# Explorando o DNS

Esta seção explora as ferramentas e técnicas para utilizar o DNS no reconhecimento web.

## Ferramentas DNS

| Ferramenta | Recursos Principais | Casos de Uso |
|------------|---------------------|--------------|
| dig | Consulta DNS versátil com suporte a vários tipos (A, MX, NS, TXT, etc.) | Consultas manuais, transferências de zona, troubleshooting |
| nslookup | Consulta DNS simples para registros A, AAAA e MX | Consultas básicas e verificações rápidas |
| host | Consulta DNS simplificada com saída concisa | Verificações rápidas de registros A, AAAA e MX |
| dnsenum | Enumeração DNS automatizada, força bruta, transferências de zona | Descoberta de subdomínios |
| fierce | Reconhecimento DNS com busca recursiva e detecção de wildcard | Identificação de subdomínios e alvos |
| dnsrecon | Múltiplas técnicas de reconhecimento DNS | Enumeração DNS abrangente |
| theHarvester | OSINT que coleta informações de várias fontes incluindo DNS | Coleta de e-mails e informações de funcionários |

## O Comando dig

O `dig` (Domain Information Groper) é um utilitário versátil para consultar servidores DNS.

### Comandos Comuns

| Comando | Descrição |
|---------|-----------|
| `dig domain.com` | Consulta padrão de registro A |
| `dig domain.com A` | Recupera o endereço IPv4 (registro A) |
| `dig domain.com AAAA` | Recupera o endereço IPv6 (registro AAAA) |
| `dig domain.com MX` | Encontra os servidores de e-mail (MX) |
| `dig domain.com NS` | Identifica os servidores de nome autoritativos |
| `dig domain.com TXT` | Recupera registros TXT |
| `dig domain.com CNAME` | Recupera o registro de nome canônico |
| `dig domain.com SOA` | Recupera o registro de início de autoridade |
| `dig @1.1.1.1 domain.com` | Consulta um servidor DNS específico |
| `dig +trace domain.com` | Mostra o caminho completo da resolução DNS |
| `dig -x 192.168.1.1` | Consulta reversa (IP → hostname) |
| `dig +short domain.com` | Resposta curta e concisa |
| `dig +noall +answer domain.com` | Exibe apenas a seção de resposta |
| `dig domain.com ANY` | Todos os registros disponíveis (muitos servidores ignoram - RFC 8482) |

> **Cuidado:** Alguns servidores detectam e bloqueiam consultas DNS excessivas. Respeite limites de taxa e obtenha permissão antes de reconhecimento extensivo.

## Exemplo Prático

```bash
dig google.com

; <<>> DiG 9.18.24-0ubuntu0.22.04.1-Ubuntu <<>> google.com
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 16449
;; flags: qr rd ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;google.com.                    IN      A

;; ANSWER SECTION:
google.com.             0       IN      A       142.251.47.142

;; Query time: 0 msec
;; SERVER: 172.23.176.1#53(172.23.176.1) (UDP)
```

### Seções da Saída

| Seção | Descrição |
|-------|-----------|
| **Header** | Tipo de consulta (QUERY), status (NOERROR), flags (qr=resposta, rd=recursão solicitada, ad=dados autênticos) |
| **Question** | A pergunta: "Qual é o registro A de google.com?" |
| **Answer** | A resposta: `142.251.47.142` com TTL de 0 |
| **Footer** | Tempo de consulta, servidor DNS usado, timestamp, tamanho da mensagem |

### Resposta Simplificada

```bash
dig +short hackthebox.com

104.18.20.126
104.18.21.126
```
