# Resumo de comandos essenciais do MySQL

Material de consulta rápida sobre conexão, navegação, estrutura e manipulação de dados. Os exemplos pressupõem um banco de laboratório ou outro ambiente autorizado. Não há comandos nem payloads de SQL injection neste arquivo.

## Cliente `mysql`

| Comando | Para que serve | Caso de uso |
|---|---|---|
| `mysql -u root -p` | Abre uma sessão e solicita a senha de forma interativa. | Acessar um servidor MySQL/MariaDB local sem expor a senha na linha de comando. |
| `mysql -u root -h host -P 3306 -p` | Informa usuário, host e porta TCP. | Conectar-se a um servidor remoto autorizado ou a um serviço em porta não padrão. |
| `mysql --version` | Mostra a versão do cliente. | Confirmar a instalação e identificar diferenças de compatibilidade. |
| `exit` ou `quit` | Encerra a sessão do cliente. | Sair do console do MySQL. |
| `help` ou `\h` | Abre a ajuda do cliente. | Consultar comandos disponíveis durante uma sessão. |
| `status` ou `\s` | Exibe dados da conexão e do servidor. | Confirmar usuário, banco atual, protocolo, versão e conexão ativa. |
| `source arquivo.sql` | Executa instruções salvas em um arquivo. | Carregar um esquema ou script SQL conhecido em laboratório. |

> Use `-p` sem escrever a senha em seguida. Senhas fornecidas diretamente na linha de comando podem aparecer no histórico, em logs ou na lista de processos.

## Bancos, tabelas e permissões

| Comando | Para que serve | Caso de uso |
|---|---|---|
| `SHOW DATABASES;` | Lista os bancos visíveis para o usuário atual. | Descobrir quais bancos a conta pode acessar. |
| `CREATE DATABASE users;` | Cria um banco. | Preparar um banco para exercício ou aplicação. |
| `USE users;` | Seleciona o banco da sessão. | Definir onde as próximas consultas serão executadas. |
| `SELECT DATABASE();` | Mostra o banco selecionado. | Evitar executar uma alteração no banco errado. |
| `SHOW TABLES;` | Lista as tabelas do banco atual. | Explorar a estrutura disponível. |
| `DESCRIBE logins;` | Mostra colunas, tipos, chaves e valores padrão. | Entender rapidamente a estrutura de uma tabela. |
| `SHOW CREATE TABLE logins;` | Exibe a instrução completa usada para definir a tabela. | Ver constraints, engine, charset e detalhes omitidos por `DESCRIBE`. |
| `SHOW GRANTS;` | Exibe os privilégios efetivos da conta atual. | Verificar quais operações estão autorizadas. |

## Criação e alteração de estrutura (DDL)

| Comando | Para que serve | Caso de uso |
|---|---|---|
| `CREATE TABLE logins (...);` | Cria uma tabela e suas colunas. | Definir uma nova estrutura de dados. |
| `ALTER TABLE logins ADD coluna INT;` | Adiciona uma coluna. | Evoluir o esquema para armazenar um novo atributo. |
| `ALTER TABLE logins RENAME COLUMN coluna TO nova_coluna;` | Renomeia uma coluna. | Corrigir ou padronizar um nome. |
| `ALTER TABLE logins MODIFY nova_coluna DATE;` | Altera o tipo ou as propriedades de uma coluna. | Adequar o formato dos dados armazenados. |
| `ALTER TABLE logins DROP COLUMN nova_coluna;` | Remove uma coluna e seus dados. | Eliminar um campo obsoleto após validação e backup. |
| `DROP TABLE logins;` | Remove a tabela, sua estrutura e seus dados. | Recriar ou descartar uma tabela de laboratório; é destrutivo. |
| `TRUNCATE TABLE logins;` | Remove todos os registros e mantém a estrutura. | Reiniciar rapidamente os dados de uma tabela de testes; é destrutivo e não aceita `WHERE`. |

Exemplo de definição completa:

```sql
CREATE TABLE logins (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    date_of_joining DATETIME DEFAULT NOW(),
    PRIMARY KEY (id)
);
```

## Manipulação e consulta de dados (DML/DQL)

| Comando | Para que serve | Caso de uso |
|---|---|---|
| `INSERT INTO logins (username, password) VALUES ('ana', 'exemplo');` | Insere um registro nas colunas indicadas. | Adicionar dados sem depender da ordem de todas as colunas. |
| `SELECT * FROM logins;` | Consulta todas as colunas e linhas. | Inspecionar uma tabela pequena em laboratório. |
| `SELECT username FROM logins;` | Consulta somente colunas escolhidas. | Retornar apenas os dados necessários. |
| `SELECT DISTINCT username FROM logins;` | Elimina valores repetidos do resultado. | Obter uma lista de valores únicos. |
| `UPDATE logins SET username = 'ana2' WHERE id = 1;` | Atualiza registros que atendem à condição. | Corrigir um dado específico. |
| `DELETE FROM logins WHERE id = 1;` | Exclui registros que atendem à condição. | Remover uma linha específica mantendo a tabela. |
| `SELECT COUNT(*) FROM logins;` | Conta registros. | Medir o tamanho do conjunto retornado. |
| `EXPLAIN SELECT * FROM logins WHERE id = 1;` | Mostra o plano de execução estimado. | Analisar índices e desempenho de uma consulta. |

> Antes de executar `UPDATE` ou `DELETE`, rode um `SELECT` com o mesmo `WHERE`. Sem `WHERE`, essas instruções afetam todas as linhas.

## Filtros e organização dos resultados

| Comando | Para que serve | Caso de uso |
|---|---|---|
| `SELECT * FROM logins WHERE id > 1;` | Filtra linhas por uma condição. | Consultar apenas IDs acima de um valor. |
| `SELECT * FROM logins WHERE username LIKE 'admin%';` | Pesquisa um padrão; `%` representa zero ou mais caracteres. | Encontrar nomes que começam com `admin`. |
| `SELECT * FROM logins WHERE username LIKE '___';` | Pesquisa um padrão; cada `_` representa exatamente um caractere. | Encontrar nomes com exatamente três caracteres. |
| `SELECT * FROM logins ORDER BY username ASC;` | Ordena em ordem crescente. | Produzir uma listagem alfabética. |
| `SELECT * FROM logins ORDER BY id DESC;` | Ordena em ordem decrescente. | Mostrar primeiro os maiores IDs. |
| `SELECT * FROM logins LIMIT 10;` | Limita a quantidade de linhas. | Visualizar uma amostra pequena. |
| `SELECT * FROM logins ORDER BY id LIMIT 10 OFFSET 20;` | Ignora 20 linhas e retorna até 10, em ordem definida. | Paginar resultados de forma previsível. |
| `SELECT * FROM logins WHERE id BETWEEN 10 AND 20;` | Filtra um intervalo inclusivo. | Consultar IDs dentro de uma faixa. |
| `SELECT * FROM logins WHERE id IN (1, 3, 5);` | Compara com uma lista de valores. | Buscar vários IDs sem repetir `OR`. |
| `SELECT * FROM logins WHERE date_of_joining IS NULL;` | Testa corretamente a ausência de valor. | Localizar registros sem data cadastrada. |

## Operadores e condições

| Operador | Para que serve | Caso de uso |
|---|---|---|
| `=` | Verifica igualdade. | `WHERE username = 'admin'`. |
| `!=` ou `<>` | Verifica diferença. | Excluir um valor específico do resultado. |
| `>`, `<`, `>=`, `<=` | Comparam valores ou intervalos. | Filtrar números e datas. |
| `AND` | Exige que todas as condições sejam verdadeiras. | Combinar usuário e estado de uma conta. |
| `OR` | Exige que pelo menos uma condição seja verdadeira. | Aceitar uma entre várias alternativas. |
| `NOT` | Inverte uma condição. | Excluir as linhas que correspondem a um critério. |
| `LIKE` | Compara texto com um padrão. | Pesquisar prefixos, sufixos ou formatos simples. |
| `IS NULL` / `IS NOT NULL` | Testa a presença de `NULL`. | Encontrar campos sem valor ou já preenchidos. |

Use parênteses quando combinar condições para tornar a ordem explícita:

```sql
SELECT *
FROM logins
WHERE (username = 'ana' OR username = 'bruno')
  AND id > 10;
```

## Cuidados essenciais

- Termine instruções no cliente com `;`.
- Use a grafia exata dos identificadores; a sensibilidade a maiúsculas pode variar conforme o ambiente.
- Selecione somente as colunas necessárias em vez de usar `SELECT *` por padrão.
- Combine `LIMIT` com `ORDER BY` quando a ordem precisar ser previsível.
- Use o princípio do menor privilégio para contas de banco.
- Faça backup e confirme o alvo antes de `DROP`, `TRUNCATE`, `ALTER ... DROP`, `UPDATE` ou `DELETE`.
- Em aplicações reais, use consultas parametrizadas e armazene senhas com hash próprio para senhas. Este resumo deliberadamente não apresenta técnicas de injeção.
