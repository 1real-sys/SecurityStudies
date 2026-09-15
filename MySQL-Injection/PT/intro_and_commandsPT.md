# Introdução ao MySQL e comandos essenciais

Este material apresenta os fundamentos de SQL com a sintaxe do MySQL/MariaDB. Esses conceitos são necessários para entender consultas, bancos de dados relacionais e, posteriormente, SQL injection. Esta versão remove repetições de saídas do terminal e mantém os exemplos que melhor representam cada conceito.

## Structured Query Language (SQL)

SQL é a linguagem usada para interagir com sistemas gerenciadores de bancos de dados relacionais (RDBMS). Embora a sintaxe varie entre produtos, os principais usos são:

- consultar, inserir, atualizar e excluir dados;
- criar ou alterar bancos de dados e tabelas;
- criar ou remover usuários;
- atribuir permissões.

Os exemplos a seguir usam MySQL/MariaDB. As palavras-chave SQL normalmente não diferenciam maiúsculas de minúsculas, mas escrevê-las em maiúsculas facilita a leitura. A sensibilidade dos nomes de bancos e tabelas depende do sistema operacional e da configuração do servidor; portanto, use sempre a grafia exata.

## Acesso pela linha de comando

O cliente `mysql` autentica um usuário e abre uma sessão com o servidor:

```bash
mysql -u root -p
```

- `-u root`: define o usuário `root`;
- `-p`: solicita a senha de modo interativo.

Não coloque a senha imediatamente depois de `-p`, pois ela poderá ficar exposta no histórico do shell, em logs ou na lista de processos.

Para acessar um servidor remoto e uma porta específica:

```bash
mysql -u root -h docker.hackthebox.eu -P 3306 -p
```

- `-h`: endereço do servidor;
- `-P`: porta TCP (letra maiúscula);
- `3306`: porta padrão do MySQL/MariaDB, embora possa ser alterada.

Sem `-h`, o cliente usa a conexão local configurada. Use contas e credenciais apenas em ambientes autorizados. O usuário conectado só poderá executar as operações permitidas por seus privilégios.

## Bancos de dados

Cada instrução enviada pelo cliente deve terminar com ponto e vírgula (`;`). Para criar um banco, listar os existentes e selecionar aquele que será usado:

```sql
CREATE DATABASE users;
SHOW DATABASES;
USE users;
```

## Tabelas e tipos de dados

Uma tabela organiza os dados em linhas (registros) e colunas (campos). Cada coluna possui um tipo, como número, texto, data/hora ou dado binário.

O exemplo abaixo cria uma tabela para armazenar logins:

```sql
CREATE TABLE logins (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    date_of_joining DATETIME DEFAULT NOW(),
    PRIMARY KEY (id)
);
```

As propriedades utilizadas são:

- `INT`: número inteiro;
- `VARCHAR(100)`: texto com limite de 100 caracteres;
- `DATETIME`: data e hora;
- `NOT NULL`: exige um valor;
- `AUTO_INCREMENT`: gera automaticamente o próximo número;
- `UNIQUE`: impede valores repetidos na coluna;
- `DEFAULT NOW()`: usa a data e a hora atuais quando nenhum valor é informado;
- `PRIMARY KEY`: identifica cada registro de forma única.

Para listar as tabelas do banco atual e inspecionar a estrutura de uma delas:

```sql
SHOW TABLES;
DESCRIBE logins;
```

## Inserção de dados

`INSERT` adiciona registros. É preferível informar explicitamente as colunas, pois isso torna a consulta mais clara e evita dependência da ordem da tabela:

```sql
INSERT INTO logins (username, password)
VALUES ('administrator', 'adm1n_p@ss');
```

Também é possível inserir vários registros na mesma instrução:

```sql
INSERT INTO logins (username, password)
VALUES
    ('john', 'john123!'),
    ('tom', 'tom123!');
```

Colunas `NOT NULL` sem valor padrão não podem ser omitidas. Os valores de `id` e `date_of_joining` foram omitidos porque são preenchidos por `AUTO_INCREMENT` e `DEFAULT NOW()`.

> As senhas em texto puro servem somente para demonstração. Em aplicações reais, armazene senhas com uma função de hash própria para senhas, como Argon2id ou bcrypt, usando salt e parâmetros adequados.

## Consulta de dados

`SELECT` recupera dados de uma tabela:

```sql
SELECT * FROM logins;
SELECT username, password FROM logins;
```

O asterisco (`*`) seleciona todas as colunas. Em consultas reais, selecionar apenas as colunas necessárias costuma melhorar clareza, segurança e desempenho.

### Filtros com `WHERE`

`WHERE` limita a operação aos registros que atendem a uma condição:

```sql
SELECT * FROM logins WHERE id > 1;
SELECT * FROM logins WHERE username = 'admin';
```

Textos e datas devem ser delimitados por aspas. Números podem ser escritos diretamente.

### Padrões com `LIKE`

`LIKE` pesquisa padrões em textos:

```sql
SELECT * FROM logins WHERE username LIKE 'admin%';
SELECT * FROM logins WHERE username LIKE '___';
```

- `%` corresponde a zero ou mais caracteres;
- `_` corresponde a exatamente um caractere.

No primeiro exemplo, são encontrados nomes iniciados por `admin`. No segundo, nomes com exatamente três caracteres.

### Ordenação com `ORDER BY`

```sql
SELECT * FROM logins ORDER BY password;
SELECT * FROM logins ORDER BY password DESC;
SELECT * FROM logins ORDER BY password DESC, id ASC;
```

A ordem padrão é ascendente (`ASC`). `DESC` inverte a ordem. Várias colunas permitem definir critérios de desempate.

### Limitação de resultados

```sql
SELECT * FROM logins LIMIT 2;
SELECT * FROM logins LIMIT 1, 2;
```

O primeiro comando retorna no máximo dois registros. No segundo, `1` é o deslocamento iniciado em zero e `2` é a quantidade: ele ignora o primeiro registro e retorna os dois seguintes. Para paginação previsível, combine `LIMIT` com `ORDER BY`.

## Atualização de registros

`UPDATE` altera os registros que atendem à condição de `WHERE`:

```sql
UPDATE logins
SET password = 'change_password'
WHERE id > 1;
```

Sem `WHERE`, todos os registros da tabela serão atualizados. Antes de uma alteração importante, é recomendável executar um `SELECT` com a mesma condição para confirmar o conjunto afetado.

## Alteração da estrutura

`ALTER TABLE` modifica a estrutura de uma tabela existente:

```sql
ALTER TABLE logins ADD newColumn INT;
ALTER TABLE logins RENAME COLUMN newColumn TO newerColumn;
ALTER TABLE logins MODIFY newerColumn DATE;
ALTER TABLE logins DROP COLUMN newerColumn;
```

Esses comandos, respectivamente, adicionam uma coluna, renomeiam uma coluna, alteram seu tipo e a removem. A sintaxe pode variar conforme a versão do MySQL/MariaDB.

## Remoção de objetos

`DROP` remove objetos inteiros:

```sql
DROP TABLE logins;
```

Essa operação remove a estrutura e os dados da tabela, normalmente sem confirmação. Verifique o objeto selecionado e mantenha backups antes de usá-la fora de laboratórios.

## Operadores lógicos

Os operadores mais comuns para combinar ou inverter condições são:

- `AND`: verdadeiro somente quando todas as condições são verdadeiras;
- `OR`: verdadeiro quando pelo menos uma condição é verdadeira;
- `NOT`: inverte o resultado lógico;
- `!=` ou `<>`: diferente de.

```sql
SELECT * FROM logins WHERE username != 'john';
SELECT * FROM logins WHERE username != 'john' AND id > 1;
SELECT * FROM logins WHERE NOT username = 'tom';
```

O MySQL também aceita `&&`, `||` e `!` em certos modos, mas `AND`, `OR` e `NOT` são mais claros e portáveis. O significado de `||` pode mudar conforme o SQL mode, por isso não deve ser usado como substituto de `OR` em material geral.

## Precedência dos operadores

Em uma expressão simplificada, operações aritméticas são avaliadas antes de comparações, que são avaliadas antes de `NOT`, `AND` e `OR`. Parênteses tornam a intenção explícita e evitam depender da memorização da precedência.

```sql
SELECT *
FROM logins
WHERE username != 'tom' AND id > (3 - 2);
```

Quando uma condição mistura vários operadores, prefira agrupar as partes relevantes com parênteses.

## Privilégios

O servidor autoriza cada operação de acordo com os privilégios da conta. Para consultar as permissões efetivas da sessão atual:

```sql
SHOW GRANTS;
```

Em administração e desenvolvimento, aplique o princípio do menor privilégio: conceda somente as permissões necessárias para cada conta.
