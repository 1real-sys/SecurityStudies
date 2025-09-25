# cURL - Client URL

cURL (Client URL) é uma ferramenta de linha de comando e biblioteca multiplataforma para transferir dados de/para servidores usando diversos protocolos. É uma das ferramentas mais versáteis para testes de APIs, automação, pentesting e desenvolvimento web.

## Protocolos Suportados

cURL suporta mais de 25 protocolos diferentes:
- **HTTP/HTTPS**: Web requests
- **FTP/FTPS/SFTP**: Transferência de arquivos
- **SCP**: Secure Copy Protocol
- **LDAP/LDAPS**: Directory services
- **SMTP/SMTPS**: Email sending
- **POP3/IMAP**: Email retrieval
- **Telnet**: Remote terminal
- **TFTP**: Trivial File Transfer
- **Gopher**: Information retrieval

## Sintaxe Básica

```bash
curl [opções] <URL>
```

### Estrutura de uma URL
```
protocolo://[usuário:senha@]host[:porta]/caminho[?parâmetros][#fragmento]
```

## Quando Usar cURL

### 1. **Desenvolvimento e Testes de API**
- Testar endpoints REST/GraphQL
- Validar respostas de APIs
- Automação de testes
- Debugging de problemas de comunicação

### 2. **Pentesting e Security Assessment**
- Enumerar aplicações web
- Testar autenticação e autorização
- Explorar vulnerabilidades
- Bypass de controles de segurança

### 3. **Automação e Scripts**
- Download automatizado de arquivos
- Integração em pipelines CI/CD
- Monitoramento de serviços
- Backup e sincronização

### 4. **Troubleshooting de Rede**
- Diagnóstico de conectividade
- Análise de cabeçalhos HTTP
- Teste de certificados SSL/TLS
- Verificação de redirecionamentos

## Exemplos Práticos Básicos

### GET Requests
```bash
# GET básico
curl https://httpbin.org/get

# Com parâmetros de query
curl "https://httpbin.org/get?nome=João&idade=30"

# Salvar resposta em arquivo
curl -o resposta.json https://httpbin.org/get

# Download com nome original
curl -O https://example.com/arquivo.zip

# Mostrar apenas cabeçalhos
curl -I https://httpbin.org/get

# Seguir redirecionamentos
curl -L https://bit.ly/shortened-url
```

### POST Requests
```bash
# POST com dados de formulário
curl -X POST -d "nome=João&email=joao@email.com" https://httpbin.org/post

# POST com JSON
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"nome":"João","email":"joao@email.com"}' \
  https://httpbin.org/post

# POST com arquivo
curl -X POST -F "arquivo=@documento.pdf" https://httpbin.org/post

# POST multipart form
curl -X POST \
  -F "nome=João" \
  -F "foto=@perfil.jpg" \
  -F "documento=@id.pdf" \
  https://httpbin.org/post
```

### Autenticação
```bash
# Basic Authentication
curl -u usuario:senha https://httpbin.org/basic-auth/usuario/senha

# Bearer Token
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." https://api.example.com/data

# API Key
curl -H "X-API-Key: abc123def456" https://api.example.com/data

# OAuth 2.0
curl -H "Authorization: Bearer $(cat token.txt)" https://api.example.com/data
```

## Parâmetros Mais Úteis

### Controle de Requisição
| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `-X, --request` | Método HTTP | `curl -X POST url` |
| `-d, --data` | Dados para POST | `curl -d "key=value" url` |
| `-H, --header` | Cabeçalho customizado | `curl -H "Content-Type: application/json"` |
| `-F, --form` | Multipart form data | `curl -F "file=@image.jpg"` |
| `-G, --get` | Força GET com -d | `curl -G -d "q=search" url` |

### Controle de Saída
| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `-o, --output` | Salva em arquivo | `curl -o file.html url` |
| `-O, --remote-name` | Nome do arquivo remoto | `curl -O url/file.zip` |
| `-s, --silent` | Modo silencioso | `curl -s url` |
| `-v, --verbose` | Modo verboso | `curl -v url` |
| `-w, --write-out` | Formato de saída | `curl -w "%{http_code}" url` |

### Controle de Conexão
| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `-L, --location` | Segue redirecionamentos | `curl -L url` |
| `-k, --insecure` | Ignora erros SSL | `curl -k https://url` |
| `-m, --max-time` | Timeout máximo | `curl -m 30 url` |
| `--connect-timeout` | Timeout de conexão | `curl --connect-timeout 10 url` |
| `-x, --proxy` | Usar proxy | `curl -x proxy:8080 url` |

### Controle de Cookies
| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `-c, --cookie-jar` | Salva cookies | `curl -c cookies.txt url` |
| `-b, --cookie` | Envia cookies | `curl -b cookies.txt url` |
| `-j, --junk-session-cookies` | Ignora cookies de sessão | `curl -j -b cookies.txt url` |

## Exemplos Avançados

### Testes de Performance
```bash
# Medir tempos de resposta
curl -w "DNS: %{time_namelookup}s\nConnect: %{time_connect}s\nTLS: %{time_appconnect}s\nTTFB: %{time_starttransfer}s\nTotal: %{time_total}s\n" -o /dev/null -s https://example.com

# Teste de velocidade de download
curl -w "Speed: %{speed_download} bytes/sec\n" -o /dev/null -s https://example.com/largefile.zip

# Múltiplas requisições paralelas
curl -w "%{http_code} - %{url_effective}\n" -o /dev/null -s \
  https://site1.com \
  https://site2.com \
  https://site3.com
```

### Simulação de Navegadores
```bash
# User-Agent personalizado
curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" url

# Referrer
curl -H "Referer: https://google.com" url

# Accept headers
curl -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" url

# Accept-Language
curl -H "Accept-Language: pt-BR,pt;q=0.9,en;q=0.8" url
```

### Upload de Arquivos
```bash
# PUT upload
curl -X PUT -T arquivo.txt https://httpbin.org/put

# POST multipart
curl -F "upload=@arquivo.zip" https://httpbin.org/post

# Raw binary upload
curl -X POST --data-binary @image.jpg https://httpbin.org/post

# Upload com progress bar
curl -# -F "file=@largefile.zip" https://httpbin.org/post
```

## cURL para Pentesting

### Enumeração Web
```bash
# Directory enumeration
curl -s -o /dev/null -w "%{http_code}" http://target.com/admin/
curl -s -o /dev/null -w "%{http_code}" http://target.com/backup/
curl -s -o /dev/null -w "%{http_code}" http://target.com/config/

# Virtual host discovery
curl -H "Host: admin.target.com" http://192.168.1.100/
curl -H "Host: api.target.com" http://192.168.1.100/

# HTTP methods testing
curl -X OPTIONS http://target.com/api/
curl -X TRACE http://target.com/
curl -X TRACK http://target.com/
```

### Bypass Techniques
```bash
# IP vs Domain
curl http://192.168.1.100/admin/ -H "Host: target.com"

# Different protocols
curl ftp://target.com/
curl ldap://target.com/

# Case variation
curl http://target.com/Admin/
curl http://target.com/ADMIN/

# Trailing slash
curl http://target.com/admin
curl http://target.com/admin/

# URL encoding
curl http://target.com/%61%64%6D%69%6E/  # /admin/
```

### Authentication Testing
```bash
# SQL Injection in login
curl -d "username=admin'--&password=anything" http://target.com/login

# Weak passwords
curl -u admin:admin http://target.com/admin/
curl -u admin:password http://target.com/admin/
curl -u admin:123456 http://target.com/admin/

# Session fixation
curl -c cookies.txt http://target.com/login
curl -b cookies.txt -d "user=admin&pass=pass" http://target.com/auth
```

### Data Extraction
```bash
# Extract specific data with grep
curl -s http://target.com/ | grep -oP 'email:\K[^"]*'

# Extract titles
curl -s http://target.com/ | grep -oP '<title>\K[^<]*'

# Extract forms
curl -s http://target.com/ | grep -A 10 -B 2 '<form'

# Download all images
curl -s http://target.com/ | grep -oP 'src="\K[^"]*\.(jpg|png|gif)' | while read img; do curl -O "$img"; done
```

## Scripts e Automação

### Bash Script Example
```bash
#!/bin/bash
# API Health Check Script

ENDPOINTS=(
    "https://api.example.com/health"
    "https://api.example.com/status"
    "https://api.example.com/version"
)

for endpoint in "${ENDPOINTS[@]}"; do
    response=$(curl -s -o /dev/null -w "%{http_code}" "$endpoint")
    if [ "$response" -eq 200 ]; then
        echo "✓ $endpoint - OK"
    else
        echo "✗ $endpoint - Error ($response)"
    fi
done
```

### JSON Processing with jq
```bash
# Extract specific fields
curl -s https://api.github.com/users/octocat | jq '.name, .public_repos'

# Filter arrays
curl -s https://api.github.com/users/octocat/repos | jq '.[] | select(.language == "JavaScript") | .name'

# Format output
curl -s https://api.github.com/users/octocat | jq '{name: .name, repos: .public_repos, followers: .followers}'
```

### Rate Limiting and Throttling
```bash
# Delay between requests
for url in $(cat urls.txt); do
    curl -s "$url" -o "$(basename $url).html"
    sleep 1
done

# Concurrent requests with xargs
cat urls.txt | xargs -n 1 -P 5 curl -s -O

# Custom rate limiting
curl --limit-rate 100K https://example.com/largefile.zip
```

## Configurações e Arquivos

### Config File (~/.curlrc)
```bash
# Default options
user-agent = "Mozilla/5.0 (Custom Client)"
max-time = 30
connect-timeout = 10
retry = 3
retry-delay = 2
```

### Environment Variables
```bash
export http_proxy=http://proxy:8080
export https_proxy=http://proxy:8080
export no_proxy=localhost,127.0.0.1

# Use with curl
curl https://example.com  # Will use proxy automatically
```

## Troubleshooting e Debug

### Verbose Output
```bash
# Detailed connection info
curl -v https://example.com

# Trace all communication
curl --trace trace.txt https://example.com
curl --trace-ascii trace.txt https://example.com

# Show request/response headers
curl -D headers.txt https://example.com
```

### SSL/TLS Debugging
```bash
# Certificate details
curl -vI https://example.com 2>&1 | grep -A 20 "Server certificate"

# Specific TLS version
curl --tlsv1.2 https://example.com
curl --tlsv1.3 https://example.com

# Certificate verification
curl --cacert mycert.pem https://example.com
curl --cert client.crt --key client.key https://example.com
```

### Error Handling
```bash
# Exit codes
curl -f https://httpbin.org/status/404  # Fail on HTTP errors
echo $?  # Check exit code

# Retry on failure
curl --retry 3 --retry-delay 2 https://unreliable-server.com

# Continue partial downloads
curl -C - -O https://example.com/largefile.zip
```

## Integração com Outras Ferramentas

### Combinando com grep/awk/sed
```bash
# Extract all links
curl -s http://example.com | grep -oP 'href="\K[^"]*'

# Count response lines
curl -s http://example.com | wc -l

# Extract specific patterns
curl -s http://api.example.com | sed -n 's/.*"token":"\([^"]*\)".*/\1/p'
```

### Pipeline com outras ferramentas
```bash
# curl + jq + sort
curl -s https://api.github.com/users/octocat/repos | jq -r '.[].name' | sort

# curl + while loop
curl -s http://example.com/api/users | jq -r '.users[].email' | while read email; do
    echo "Processing: $email"
    # Processar cada email
done
```

## Alternativas e Comparações

### wget vs curl
- **curl**: Melhor para APIs, mais protocolos, biblioteca
- **wget**: Melhor para downloads recursivos, mirror de sites

### HTTPie vs curl
- **HTTPie**: Interface mais amigável, JSON por padrão
- **curl**: Mais poderoso, universal, scripting

### Postman vs curl
- **Postman**: GUI, coleções, testes automatizados
- **curl**: Command line, scripting, integração CI/CD

## Boas Práticas

### Segurança
```bash
# Nunca exponha credenciais no histórico
curl -u "$(cat credentials.txt)" https://api.example.com

# Use variáveis de ambiente
curl -H "Authorization: Bearer $API_TOKEN" https://api.example.com

# Valide certificados SSL
curl --cacert ca-bundle.crt https://secure-api.com
```

### Performance
```bash
# Reutilize conexões
curl --keepalive-time 60 https://api.example.com/endpoint1
curl --keepalive-time 60 https://api.example.com/endpoint2

# Compressão
curl --compressed https://api.example.com/large-response

# HTTP/2
curl --http2 https://http2-enabled-site.com
```

### Logging e Monitoramento
```bash
# Log all requests
alias curl='curl -w "Time: %{time_total}s\nStatus: %{http_code}\nSize: %{size_download} bytes\n"'

# Save request details
curl -w "@curl-format.txt" -s -o response.json https://api.example.com
```

## Conclusão

cURL é uma ferramenta fundamental para qualquer profissional que trabalhe com APIs, desenvolvimento web ou segurança. Sua versatilidade, combinada com a ampla gama de protocolos suportados, a torna indispensável para automação, testes e diagnósticos de rede. Dominar cURL significa ter uma ferramenta poderosa para praticamente qualquer tarefa relacionada à transferência de dados pela rede.