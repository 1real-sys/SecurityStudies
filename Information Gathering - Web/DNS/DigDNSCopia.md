# Explorando o DNS

Tendo estabelecido uma compreensão sólida dos fundamentos do DNS e seus vários tipos de registros, vamos agora passar para a prática. Esta seção explorará as ferramentas e técnicas para utilizar o DNS na reconhecimento web.

## Ferramentas DNS

O reconhecimento DNS envolve a utilização de ferramentas especializadas projetadas para consultar servidores DNS e extrair informações valiosas. Aqui estão algumas das ferramentas mais populares e versáteis no arsenal de profissionais de reconhecimento web:

| Ferramenta | Recursos Principais | Casos de Uso |
|------------|---------------------|--------------|
| dig | Ferramenta versátil de consulta DNS que suporta vários tipos de consulta (A, MX, NS, TXT, etc.) e saída detalhada. | Consultas DNS manuais, transferências de zona (se permitidas), solução de problemas de DNS e análise aprofundada de registros DNS. |
| nslookup | Ferramenta de consulta DNS mais simples, principalmente para registros A, AAAA e MX. | Consultas DNS básicas, verificações rápidas de resolução de domínio e registros de servidor de e-mail. |
| host | Ferramenta de consulta DNS simplificada com saída concisa. | Verificações rápidas de registros A, AAAA e MX. |
| dnsenum | Ferramenta automatizada de enumeração DNS, ataques de dicionário, força bruta, transferências de zona (se permitidas). | Descoberta de subdomínios e coleta eficiente de informações DNS. |
| fierce | Ferramenta de reconhecimento DNS e enumeração de subdomínios com busca recursiva e detecção de wildcard. | Interface amigável para reconhecimento DNS, identificação de subdomínios e alvos potenciais. |
| dnsrecon | Combina múltiplas técnicas de reconhecimento DNS e suporta vários formatos de saída. | Enumeração DNS abrangente, identificação de subdomínios e coleta de registros DNS para análise posterior. |
| theHarvester | Ferramenta OSINT que coleta informações de várias fontes, incluindo registros DNS (endereços de e-mail). | Coleta de endereços de e-mail, informações de funcionários e outros dados associados a um domínio de múltiplas fontes. |
| Serviços Online de Consulta DNS | Interfaces amigáveis para realizar consultas DNS. | Consultas DNS rápidas e fáceis, convenientes quando ferramentas de linha de comando não estão disponíveis, verificação de disponibilidade de domínio ou informações básicas. |

## O Domain Information Groper (dig)

O comando `dig` (Domain Information Groper) é um utilitário versátil e poderoso para consultar servidores DNS e recuperar vários tipos de registros DNS. Sua flexibilidade e saída detalhada e personalizável o tornam uma escolha essencial.

### Comandos dig Comuns

| Comando | Descrição |
|---------|-----------|
| `dig domain.com` | Realiza uma consulta padrão de registro A para o domínio. |
| `dig domain.com A` | Recupera o endereço IPv4 (registro A) associado ao domínio. |
| `dig domain.com AAAA` | Recupera o endereço IPv6 (registro AAAA) associado ao domínio. |
| `dig domain.com MX` | Encontra os servidores de e-mail (registros MX) responsáveis pelo domínio. |
| `dig domain.com NS` | Identifica os servidores de nome autoritativos para o domínio. |
| `dig domain.com TXT` | Recupera quaisquer registros TXT associados ao domínio. |
| `dig domain.com CNAME` | Recupera o registro de nome canônico (CNAME) para o domínio. |
| `dig domain.com SOA` | Recupera o registro de início de autoridade (SOA) para o domínio. |
| `dig @1.1.1.1 domain.com` | Especifica um servidor de nome específico para consultar; neste caso 1.1.1.1 |
| `dig +trace domain.com` | Mostra o caminho completo da resolução DNS. |
| `dig -x 192.168.1.1` | Realiza uma consulta reversa no endereço IP 192.168.1.1 para encontrar o nome de host associado. Pode ser necessário especificar um servidor de nome. |
| `dig +short domain.com` | Fornece uma resposta curta e concisa à consulta. |
| `dig +noall +answer domain.com` | Exibe apenas a seção de resposta da saída da consulta. |
| `dig domain.com ANY` | Recupera todos os registros DNS disponíveis para o domínio (Nota: Muitos servidores DNS ignoram consultas ANY para reduzir carga e prevenir abuso, conforme RFC 8482). |

> **Cuidado:** Alguns servidores podem detectar e bloquear consultas DNS excessivas. Use com cautela e respeite os limites de taxa. Sempre obtenha permissão antes de realizar reconhecimento DNS extensivo em um alvo.

## Explorando o DNS na Prática

```bash
dig google.com

; <<>> DiG 9.18.24-0ubuntu0.22.04.1-Ubuntu <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 16449
;; flags: qr rd ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
;; WARNING: recursion requested but not available

;; QUESTION SECTION:
;google.com.                    IN      A

;; ANSWER SECTION:
google.com.             0       IN      A       142.251.47.142

;; Query time: 0 msec
;; SERVER: 172.23.176.1#53(172.23.176.1) (UDP)
;; WHEN: Thu Jun 13 10:45:58 SAST 2024
;; MSG SIZE  rcvd: 54
```

Esta saída é o resultado de uma consulta DNS usando o comando dig para o domínio google.com. A saída pode ser dividida em quatro seções principais:

### Header (Cabeçalho)

- `opcode: QUERY, status: NOERROR, id: 16449`: Indica o tipo de consulta (QUERY), o status bem-sucedido (NOERROR) e um identificador único (16449) para esta consulta específica.
- **Flags:**
  - `qr`: Query Response - indica que esta é uma resposta.
  - `rd`: Recursion Desired - significa que a recursão foi solicitada.
  - `ad`: Authentic Data - significa que o resolver considera os dados autênticos.
- Os números restantes indicam a quantidade de entradas em cada seção: 1 pergunta, 1 resposta, 0 registros de autoridade e 0 registros adicionais.
- `WARNING: recursion requested but not available`: Indica que a recursão foi solicitada, mas o servidor não a suporta.

### Question Section (Seção de Pergunta)

- `;google.com. IN A`: Especifica a pergunta: "Qual é o endereço IPv4 (registro A) para google.com?"

### Answer Section (Seção de Resposta)

- `google.com. 0 IN A 142.251.47.142`: Esta é a resposta à consulta. Indica que o endereço IP associado a google.com é 142.251.47.142. O '0' representa o TTL (time-to-live), indicando por quanto tempo o resultado pode ser armazenado em cache antes de ser atualizado.

### Footer (Rodapé)

- `Query time: 0 msec`: Mostra o tempo que levou para a consulta ser processada (0 milissegundos).
- `SERVER: 172.23.176.1#53(172.23.176.1) (UDP)`: Identifica o servidor DNS que forneceu a resposta e o protocolo usado (UDP).
- `WHEN: Thu Jun 13 10:45:58 SAST 2024`: Timestamp de quando a consulta foi feita.
- `MSG SIZE rcvd: 54`: Indica o tamanho da mensagem DNS recebida (54 bytes).

> Uma seção opt (pseudosection) pode às vezes existir em uma consulta dig. Isso ocorre devido aos Mecanismos de Extensão para DNS (EDNS), que permitem recursos adicionais como tamanhos de mensagem maiores e suporte a DNSSEC (DNS Security Extensions).

### Resposta Simplificada

Se você quer apenas a resposta à pergunta, sem nenhuma outra informação, você pode consultar o dig usando `+short`:

```bash
dig +short hackthebox.com

104.18.20.126
104.18.21.126
```
