# HTTP - HyperText Transfer Protocol

HTTP é um protocolo de nível de aplicação usado para acessar recursos da World Wide Web. Funciona baseado no modelo cliente-servidor, onde o cliente (navegador, aplicação) faz requisições para um servidor web.

## Características do HTTP

- **Stateless**: Cada requisição é independente
- **Baseado em texto**: Cabeçalhos e dados são legíveis
- **Porta padrão**: 80 (HTTP) e 443 (HTTPS)
- **Modelo Request/Response**: Cliente solicita, servidor responde

## Métodos HTTP

- **GET**: Solicita dados do servidor
- **POST**: Envia dados para o servidor
- **PUT**: Atualiza um recurso completo
- **PATCH**: Atualiza parcialmente um recurso
- **DELETE**: Remove um recurso
- **HEAD**: Como GET, mas retorna apenas cabeçalhos
- **OPTIONS**: Verifica métodos suportados

## Códigos de Status HTTP

### 1xx - Informacional
- **100**: Continue

### 2xx - Sucesso
- **200**: OK
- **201**: Created
- **204**: No Content

### 3xx - Redirecionamento
- **301**: Moved Permanently
- **302**: Found (Temporary Redirect)
- **304**: Not Modified

### 4xx - Erro do Cliente
- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found

### 5xx - Erro do Servidor
- **500**: Internal Server Error
- **502**: Bad Gateway
- **503**: Service Unavailable

## URL - Uniform Resource Locator

Para acessar recursos via HTTP, utilizamos URLs que seguem a estrutura:

```
protocolo://domínio:porta/caminho?parâmetros#fragmento
```

**Exemplo:**
```
https://example.com:443/api/users?id=123#section1
```

## cURL - Client URL

cURL é uma ferramenta de linha de comando e biblioteca que suporta principalmente HTTP, além de muitos outros protocolos (FTP, SFTP, LDAP, etc.). É amplamente utilizada para scripts, automação e testes de APIs.

### Sintaxe Básica
```bash
curl [opções] <URL>
```

### Exemplos Práticos

#### Requisição GET básica
```bash
curl https://httpbin.org/get
```

#### Download de arquivo
```bash
curl -O https://example.com/arquivo.zip
# ou especificar nome
curl -o meuarquivo.zip https://example.com/arquivo.zip
```

#### Requisição POST com dados
```bash
curl -X POST -d "nome=João&email=joao@email.com" https://httpbin.org/post
```

#### Enviar JSON
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"nome":"João","email":"joao@email.com"}' \
  https://httpbin.org/post
```

#### Adicionar cabeçalhos personalizados
```bash
curl -H "Authorization: Bearer token123" \
     -H "User-Agent: MeuApp/1.0" \
     https://api.example.com/data
```

#### Seguir redirecionamentos
```bash
curl -L https://bit.ly/example-redirect
```

#### Mostrar apenas cabeçalhos de resposta
```bash
curl -I https://example.com
```

#### Mostrar informações detalhadas da requisição
```bash
curl -v https://example.com
```

#### Salvar cookies e reutilizar
```bash
# Salvar cookies
curl -c cookies.txt https://example.com/login

# Usar cookies salvos
curl -b cookies.txt https://example.com/protected
```

#### Autenticação básica
```bash
curl -u usuario:senha https://example.com/protected
```

### Opções Úteis do cURL

| Opção | Descrição |
|-------|-----------|
| `-X` | Especifica método HTTP |
| `-d` | Dados para enviar (POST) |
| `-H` | Adiciona cabeçalho |
| `-o` | Salva output em arquivo |
| `-O` | Salva com nome original |
| `-L` | Segue redirecionamentos |
| `-I` | Mostra apenas cabeçalhos |
| `-v` | Modo verboso |
| `-s` | Modo silencioso |
| `-c` | Salva cookies |
| `-b` | Usa cookies |
| `-u` | Autenticação básica |
| `-k` | Ignora erros SSL |

### Exemplo de Uso em Pentesting
```bash
# Baixar arquivo PHP de um servidor
curl -O http://94.237.122.241:43003/download.php

# Testar diferentes User-Agents
curl -H "User-Agent: Mozilla/5.0..." https://target.com

# Verificar cabeçalhos de segurança
curl -I https://target.com
```

## HTTPS vs HTTP

- **HTTP**: Dados transmitidos em texto claro
- **HTTPS**: HTTP sobre TLS/SSL, dados criptografados
- **Porta HTTPS**: 443 (padrão)
- **Certificados**: Validam identidade do servidor

## Cabeçalhos HTTP Importantes

### Requisição
- `Host`: Domínio do servidor
- `User-Agent`: Identificação do cliente
- `Accept`: Tipos de conteúdo aceitos
- `Authorization`: Credenciais de autenticação

### Resposta
- `Content-Type`: Tipo do conteúdo retornado
- `Content-Length`: Tamanho do conteúdo
- `Set-Cookie`: Define cookies
- `Location`: URL para redirecionamento

