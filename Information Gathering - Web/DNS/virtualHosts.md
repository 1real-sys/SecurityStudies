# Virtual Hosts

Após o DNS direcionar o tráfego para o servidor correto, a configuração do servidor web determina como as requisições são tratadas. Servidores como Apache, Nginx ou IIS hospedam múltiplos sites em um único servidor através de **virtual hosting**.

## Como Funcionam: VHosts vs Subdomínios

Servidores web distinguem múltiplos sites no mesmo IP usando o cabeçalho HTTP **Host**.

- **Subdomínios:** Extensões do domínio principal (ex: `blog.example.com`). Têm registros DNS próprios.
- **VHosts:** Configurações no servidor web que permitem hospedar múltiplos sites. Podem ser associados a domínios ou subdomínios.

> Sem registro DNS, você pode acessar um VHost modificando o arquivo `hosts` local.

**VHost fuzzing** descobre subdomínios/VHosts públicos e não-públicos testando hostnames contra um IP conhecido.

### Exemplo de Configuração Apache

```apacheconf
<VirtualHost *:80>
    ServerName www.example1.com
    DocumentRoot /var/www/example1
</VirtualHost>

<VirtualHost *:80>
    ServerName www.example2.org
    DocumentRoot /var/www/example2
</VirtualHost>
```

## Processo de Lookup

![Virtual Host Lookup](../../img/virtualhosts.png)

1. **Navegador requisita site:** Envia requisição HTTP para o IP do domínio
2. **Host Header:** Navegador inclui o domínio no cabeçalho Host
3. **Servidor determina VHost:** Examina o Host e consulta configuração
4. **Serve conteúdo:** Recupera arquivos do document root correspondente

## Tipos de Virtual Hosting

| Tipo | Descrição | Vantagens | Limitações |
|------|-----------|-----------|------------|
| **Baseado em Nome** | Usa cabeçalho Host | Econômico, flexível, fácil | Limitações com SSL/TLS |
| **Baseado em IP** | IP único por site | Melhor isolamento, qualquer protocolo | Caro, menos escalável |
| **Baseado em Porta** | Porta diferente por site | Útil com IPs limitados | Menos amigável, requer porta na URL |

## Ferramentas de Descoberta

| Ferramenta | Descrição |
|------------|-----------|
| **gobuster** | Força bruta de diretórios e VHosts. Rápida, wordlists customizadas |
| **Feroxbuster** | Implementação Rust. Recursão, wildcard, filtros |
| **ffuf** | Fuzzer web rápido para cabeçalho Host |

## Gobuster para VHosts

### Preparação

1. **Identificar alvo:** IP do servidor web (via DNS lookup)
2. **Wordlist:** Lista de nomes potenciais (ex: SecLists)

### Comando Básico

```bash
gobuster vhost -u http://<IP_alvo> -w <wordlist> --append-domain
```

- `-u`: URL alvo
- `-w`: arquivo wordlist
- `--append-domain`: anexa domínio base a cada palavra (necessário em versões novas)

### Flags Úteis

- `-t`: aumenta threads para varredura mais rápida
- `-k`: ignora erros de certificado SSL/TLS
- `-o`: salva saída em arquivo

### Exemplo

```bash
gobuster vhost -u http://inlanefreight.htb:81 -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain
```

```
Found: forum.inlanefreight.htb:81 Status: 200 [Size: 100]
```

> **Aviso:** Descoberta de VHost gera tráfego significativo e pode ser detectada por IDS/WAF. Obtenha autorização antes de escanear.
