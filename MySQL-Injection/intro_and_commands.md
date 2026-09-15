# Introduction to MySQL and Essential Commands

This material presents SQL fundamentals using MySQL/MariaDB syntax. These concepts are necessary to understand queries, relational databases, and, later, SQL injection. Repetitive terminal output has been removed while representative examples have been retained.

## Structured Query Language (SQL)

SQL is used to interact with relational database management systems (RDBMS). Although syntax varies between products, its main uses include:

- retrieving, inserting, updating, and deleting data;
- creating or modifying databases and tables;
- creating or removing users;
- assigning permissions.

The following examples use MySQL/MariaDB. SQL keywords are generally case-insensitive, but writing them in uppercase improves readability. The case sensitivity of database and table names depends on the operating system and server configuration, so always use their exact spelling.

## Command-Line Access

The `mysql` client authenticates a user and opens a session with the server:

```bash
mysql -u root -p
```

- `-u root`: sets the username to `root`;
- `-p`: prompts for the password interactively.

Do not place the password immediately after `-p`, as it may be exposed in shell history, logs, or the process list.

To access a remote server on a specific port:

```bash
mysql -u root -h docker.hackthebox.eu -P 3306 -p
```

- `-h`: server address;
- `-P`: TCP port (uppercase letter);
- `3306`: the default MySQL/MariaDB port, although it can be changed.

Without `-h`, the client uses the configured local connection. Use accounts and credentials only in authorized environments. The connected user can execute only the operations allowed by their privileges.

## Databases

Each statement sent through the client must end with a semicolon (`;`). To create a database, list the available databases, and select the one to use:

```sql
CREATE DATABASE users;
SHOW DATABASES;
USE users;
```

## Tables and Data Types

A table organizes data into rows (records) and columns (fields). Each column has a type, such as a number, text, date/time, or binary data.

```sql
CREATE TABLE logins (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    date_of_joining DATETIME DEFAULT NOW(),
    PRIMARY KEY (id)
);
```

The properties used above are:

- `INT`: integer number;
- `VARCHAR(100)`: text limited to 100 characters;
- `DATETIME`: date and time;
- `NOT NULL`: requires a value;
- `AUTO_INCREMENT`: automatically generates the next number;
- `UNIQUE`: prevents duplicate values in the column;
- `DEFAULT NOW()`: uses the current date and time when no value is provided;
- `PRIMARY KEY`: uniquely identifies each record.

To list the tables in the current database and inspect a table's structure:

```sql
SHOW TABLES;
DESCRIBE logins;
```

## Inserting Data

`INSERT` adds records. Explicitly listing the columns makes a query clearer and avoids depending on the table's column order:

```sql
INSERT INTO logins (username, password)
VALUES ('administrator', 'adm1n_p@ss');
```

Multiple records can be inserted with one statement:

```sql
INSERT INTO logins (username, password)
VALUES
    ('john', 'john123!'),
    ('tom', 'tom123!');
```

`NOT NULL` columns without a default value cannot be omitted. The `id` and `date_of_joining` values were omitted because `AUTO_INCREMENT` and `DEFAULT NOW()` populate them.

> Plaintext passwords are used only for demonstration. Real applications should store passwords with a dedicated password-hashing function such as Argon2id or bcrypt, using a salt and appropriate parameters.

## Retrieving Data

`SELECT` retrieves data from a table:

```sql
SELECT * FROM logins;
SELECT username, password FROM logins;
```

The asterisk (`*`) selects every column. In real queries, selecting only the required columns usually improves clarity, security, and performance.

### Filtering with `WHERE`

`WHERE` limits an operation to records that satisfy a condition:

```sql
SELECT * FROM logins WHERE id > 1;
SELECT * FROM logins WHERE username = 'admin';
```

Text and date values must be enclosed in quotes. Numbers can be written directly.

### Pattern Matching with `LIKE`

```sql
SELECT * FROM logins WHERE username LIKE 'admin%';
SELECT * FROM logins WHERE username LIKE '___';
```

- `%` matches zero or more characters;
- `_` matches exactly one character.

The first example finds names beginning with `admin`. The second finds names containing exactly three characters.

### Sorting with `ORDER BY`

```sql
SELECT * FROM logins ORDER BY password;
SELECT * FROM logins ORDER BY password DESC;
SELECT * FROM logins ORDER BY password DESC, id ASC;
```

The default order is ascending (`ASC`). `DESC` reverses the order. Multiple columns define additional sorting criteria for ties.

### Limiting Results

```sql
SELECT * FROM logins LIMIT 2;
SELECT * FROM logins LIMIT 1, 2;
```

The first command returns at most two records. In the second, `1` is the zero-based offset and `2` is the number of records. Combine `LIMIT` with `ORDER BY` for predictable pagination.

## Updating Records

`UPDATE` changes records that satisfy the `WHERE` condition:

```sql
UPDATE logins
SET password = 'change_password'
WHERE id > 1;
```

Without `WHERE`, every record in the table is updated. Before an important change, run a `SELECT` with the same condition to confirm which records will be affected.

## Modifying the Structure

`ALTER TABLE` modifies an existing table:

```sql
ALTER TABLE logins ADD newColumn INT;
ALTER TABLE logins RENAME COLUMN newColumn TO newerColumn;
ALTER TABLE logins MODIFY newerColumn DATE;
ALTER TABLE logins DROP COLUMN newerColumn;
```

These commands add a column, rename it, change its type, and remove it, respectively. Exact syntax may vary depending on the MySQL/MariaDB version.

## Removing Objects

`DROP` removes entire objects:

```sql
DROP TABLE logins;
```

This operation removes the table structure and its data, normally without confirmation. Verify the selected object and maintain backups before using it outside a laboratory.

## Logical Operators

The most common operators for combining or reversing conditions are:

- `AND`: true only when every condition is true;
- `OR`: true when at least one condition is true;
- `NOT`: reverses the logical result;
- `!=` or `<>`: not equal to.

```sql
SELECT * FROM logins WHERE username != 'john';
SELECT * FROM logins WHERE username != 'john' AND id > 1;
SELECT * FROM logins WHERE NOT username = 'tom';
```

MySQL also accepts `&&`, `||`, and `!` in certain modes, but `AND`, `OR`, and `NOT` are clearer and more portable. The meaning of `||` can change according to the SQL mode, so it should not be used as a general replacement for `OR`.

## Operator Precedence

In a simplified expression, arithmetic operations are evaluated before comparisons, which are evaluated before `NOT`, `AND`, and `OR`. Parentheses make the intent explicit:

```sql
SELECT *
FROM logins
WHERE username != 'tom' AND id > (3 - 2);
```

When a condition mixes several operators, group the relevant parts with parentheses.

## Privileges

The server authorizes each operation according to the account's privileges. To view the effective permissions for the current session:

```sql
SHOW GRANTS;
```

Apply the principle of least privilege: grant each account only the permissions it requires.
