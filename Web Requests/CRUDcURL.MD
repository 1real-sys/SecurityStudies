# CRUD e cURL - Resumo

## CRUD (Create, Read, Update, Delete)

**CRUD** é um acrônimo que representa as quatro operações básicas de manipulação de dados:

- **Create (Criar)**: Inserir novos dados no sistema
- **Read (Ler)**: Consultar dados existentes
- **Update (Atualizar)**: Modificar dados existentes
- **Delete (Excluir)**: Remover dados do sistema

Essas operações correspondem aos métodos HTTP:
- **POST** → Create
- **GET** → Read
- **PUT/PATCH** → Update
- **DELETE** → Delete

## cURL (Client URL)

**cURL** é uma ferramenta de linha de comando para transferir dados usando vários protocolos de rede (HTTP, HTTPS, FTP, etc.).

### Sintaxe Básica:
```bash
curl [opções] [URL]
```

### Exemplos de Operações CRUD com cURL:

**CREATE (POST)**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"João","email":"joao@email.com"}' https://api.exemplo.com/users
```

**READ (GET)**:
```bash
curl https://api.exemplo.com/users
curl https://api.exemplo.com/users/123
```

**UPDATE (PUT)**:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name":"João Silva","email":"joao.silva@email.com"}' https://api.exemplo.com/users/123
```

**DELETE**:
```bash
curl -X DELETE https://api.exemplo.com/users/123
```

### Principais Opções do cURL:
- `-X`: Especifica método HTTP
- `-H`: Adiciona cabeçalhos
- `-d`: Dados para envio (payload)
- `-i`: Inclui headers na resposta
- `-v`: Modo verboso (debug)
- `-o`: Salva resposta em arquivo

## Importância na Segurança

- **Teste de APIs**: Verificar autenticação e autorização
- **Análise de vulnerabilidades**: Testar injeções e falhas de validação
- **Interceptação de requisições**: Monitorar tráfego de dados
- **Auditoria**: Verificar logs e rastros de operações CRUD 