# Headers HTTP

Os cabeçalhos HTTP são componentes essenciais das requisições e respostas HTTP, fornecendo metadados sobre a comunicação entre cliente e servidor. Eles permitem que tanto o cliente quanto o servidor passem informações adicionais sobre a requisição ou resposta.

## Estrutura dos Headers

Os headers HTTP seguem o formato:
```
Nome-do-Header: valor
```

**Exemplo:**
```http
Content-Type: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
```

## General Headers

Utilizados tanto em solicitações quanto em respostas HTTP, contendo informações gerais sobre a comunicação.

### Date
Contém a data e hora de origem da mensagem.
```http
Date: Wed, 16 Feb 2022 10:38:44 GMT
```

### Connection
Determina se a conexão de rede atual deve permanecer ativa após o término da solicitação.
```http
Connection: keep-alive
Connection: close
```

### Cache-Control
Controla o comportamento de cache.
```http
Cache-Control: no-cache
Cache-Control: max-age=3600
Cache-Control: public, max-age=31536000
```

### Via
Utilizado por proxies para indicar protocolos intermediários.
```http
Via: 1.1 proxy.exemplo.com
```

## Entity Headers

Descrevem o conteúdo da entidade/corpo da mensagem. Geralmente encontrados em requisições POST, PUT e respostas com conteúdo.

### Content-Type
Especifica o tipo de mídia do recurso sendo transferido.
```http
Content-Type: text/html; charset=UTF-8
Content-Type: application/json
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary
```

### Content-Length
Indica o tamanho do corpo da mensagem em bytes.
```http
Content-Length: 348
```

### Content-Encoding
Especifica a codificação aplicada ao corpo da mensagem.
```http
Content-Encoding: gzip
Content-Encoding: deflate
Content-Encoding: br
```

### Content-Disposition
Indica como o conteúdo deve ser apresentado (inline ou como download).
```http
Content-Disposition: attachment; filename="arquivo.pdf"
Content-Disposition: inline
```

### Last-Modified
Data da última modificação do recurso.
```http
Last-Modified: Tue, 15 Feb 2022 08:12:31 GMT
```

### ETag
Identificador único para uma versão específica do recurso.
```http
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
ETag: W/"0815"
```

## Request Headers

Utilizados em requisições HTTP, fornecendo informações sobre o cliente e modificando ou condicionalizando a requisição.

### Host
Especifica o nome do domínio do servidor (obrigatório no HTTP/1.1).
```http
Host: www.exemplo.com
Host: api.exemplo.com:8080
```

### User-Agent
Identifica o software cliente fazendo a requisição.
```http
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
User-Agent: curl/7.77.0
User-Agent: PostmanRuntime/7.28.0
```

### Accept
Especifica os tipos de conteúdo que o cliente pode processar.
```http
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept: application/json
Accept: image/webp,image/apng,*/*;q=0.8
```

### Accept-Language
Indica os idiomas preferidos pelo cliente.
```http
Accept-Language: pt-BR,pt;q=0.9,en;q=0.8
Accept-Language: en-US,en;q=0.5
```

### Accept-Encoding
Especifica as codificações de conteúdo aceitas.
```http
Accept-Encoding: gzip, deflate, br
Accept-Encoding: identity
```

### Authorization
Contém credenciais para autenticar o cliente no servidor.
```http
Authorization: Basic dXNlcjpwYXNzd29yZA==
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
Authorization: Digest username="user", realm="exemplo.com"
```

### Cookie
Envia cookies armazenados para o servidor.
```http
Cookie: sessionid=abc123; preferences=dark_mode
Cookie: PHPSESSID=b4e4fbd93540; user_lang=pt-BR
```

### Referer
Indica a URL da página que fez a requisição.
```http
Referer: https://www.google.com/
Referer: https://exemplo.com/pagina-anterior
```

### If-Modified-Since
Requisição condicional baseada na data de modificação.
```http
If-Modified-Since: Tue, 15 Feb 2022 08:12:31 GMT
```

### If-None-Match
Requisição condicional baseada no ETag.
```http
If-None-Match: "33a64df551425fcc55e4d42a148795d9f25f89d4"
```

## Response Headers

Utilizados em respostas HTTP, fornecendo informações sobre o servidor e modificando ou condicionalizando a resposta.

### Server
Identifica o software do servidor que processou a requisição.
```http
Server: Apache/2.4.41 (Ubuntu)
Server: nginx/1.18.0
Server: Microsoft-IIS/10.0
```

### Set-Cookie
Define cookies que devem ser armazenados pelo cliente.
```http
Set-Cookie: sessionid=abc123; Path=/; HttpOnly; Secure
Set-Cookie: preferences=dark_mode; Max-Age=3600; SameSite=Strict
```

### Location
Indica a URL para redirecionamento.
```http
Location: https://www.exemplo.com/nova-pagina
Location: /login
```

### WWW-Authenticate
Especifica o método de autenticação requerido.
```http
WWW-Authenticate: Basic realm="Área Protegida"
WWW-Authenticate: Bearer realm="api"
```

### Expires
Data/hora quando a resposta é considerada obsoleta.
```http
Expires: Thu, 01 Dec 2022 16:00:00 GMT
```

### Access-Control-Allow-Origin
Define origens permitidas para requisições CORS.
```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Origin: https://exemplo.com
```

## Security Headers

Headers de segurança implementam políticas e proteções adicionais no navegador.

### Content-Security-Policy (CSP)
Define política de segurança para recursos externos, prevenindo ataques XSS.
```http
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'
Content-Security-Policy: script-src 'self'; object-src 'none'; base-uri 'self'
```

### X-Content-Type-Options
Previne MIME type sniffing.
```http
X-Content-Type-Options: nosniff
```

### X-Frame-Options
Controla se a página pode ser exibida em frames (previne clickjacking).
```http
X-Frame-Options: DENY
X-Frame-Options: SAMEORIGIN
X-Frame-Options: ALLOW-FROM https://exemplo.com
```

### X-XSS-Protection
Habilita filtro XSS do navegador (obsoleto, substituído por CSP).
```http
X-XSS-Protection: 1; mode=block
```

### Strict-Transport-Security (HSTS)
Força o uso de HTTPS.
```http
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

### Referrer-Policy
Controla informações de referrer enviadas.
```http
Referrer-Policy: strict-origin-when-cross-origin
Referrer-Policy: no-referrer
```

### Permissions-Policy (Feature-Policy)
Controla quais APIs e recursos podem ser usados.
```http
Permissions-Policy: geolocation=(), microphone=(), camera=()
```

## Headers Customizados

Aplicações podem definir headers customizados, geralmente prefixados com `X-`.

### Exemplos Comuns
```http
X-API-Key: sk_test_123456789
X-Rate-Limit-Remaining: 99
X-Request-ID: 550e8400-e29b-41d4-a716-446655440000
X-Forwarded-For: 203.0.113.195, 70.41.3.18
X-Real-IP: 203.0.113.195
```

## Ferramentas para Análise de Headers

### cURL - Visualizar Headers
```bash
# Mostrar apenas headers de resposta
curl -I https://exemplo.com

# Mostrar headers completos (requisição e resposta)
curl -v https://exemplo.com

# Adicionar header customizado
curl -H "X-API-Key: 123456" https://api.exemplo.com
```

### Browser Developer Tools
1. Abrir F12 (Developer Tools)
2. Aba **Network**
3. Fazer requisição
4. Clicar na requisição para ver headers

### Burp Suite
- Interceptar requisições
- Modificar headers em tempo real
- Analisar headers de segurança

### OWASP ZAP
- Scan automático de headers de segurança
- Identificação de headers ausentes
- Relatórios de conformidade

## Headers em Pentesting

### Information Gathering
```bash
# Identificar tecnologias do servidor
curl -I https://target.com | grep -i server

# Verificar headers de segurança
curl -I https://target.com | grep -i "x-\|content-security\|strict-transport"
```

### User-Agent Manipulation
```bash
# Bypass de filtros baseados em User-Agent
curl -H "User-Agent: Googlebot/2.1" https://target.com
curl -H "User-Agent: Mozilla/5.0 (compatible; Baiduspider/2.0)" https://target.com
```

### Header Injection
```bash
# Teste de injeção CRLF
curl -H "X-Test: value%0d%0aX-Injected: malicious" https://target.com

# Host Header Injection
curl -H "Host: evil.com" https://target.com
```

### Bypass de Autenticação
```bash
# Headers de proxy/load balancer
curl -H "X-Forwarded-For: 127.0.0.1" https://target.com/admin
curl -H "X-Real-IP: 192.168.1.1" https://target.com/internal
curl -H "X-Originating-IP: 10.0.0.1" https://target.com
```

## Boas Práticas de Segurança

### Headers Obrigatórios
- **Content-Security-Policy**: Política rigorosa
- **X-Content-Type-Options**: nosniff
- **X-Frame-Options**: DENY ou SAMEORIGIN
- **Strict-Transport-Security**: Para sites HTTPS

### Headers a Remover/Ocultar
- **Server**: Não revelar versão específica
- **X-Powered-By**: Remove informações da stack
- **X-AspNet-Version**: Remove versão do .NET

### Configuração Segura
```apache
# Apache - Remover headers informativos
ServerTokens Prod
ServerSignature Off
Header unset X-Powered-By
```

```nginx
# Nginx - Headers de segurança
server_tokens off;
add_header X-Content-Type-Options nosniff;
add_header X-Frame-Options SAMEORIGIN;
add_header Content-Security-Policy "default-src 'self'";
```