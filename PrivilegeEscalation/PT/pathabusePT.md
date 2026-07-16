# Abuso de PATH

`PATH` é uma variável de ambiente que define o conjunto de diretórios onde um executável pode ser localizado. A variável `PATH` de uma conta é um conjunto de caminhos absolutos, permitindo que o usuário execute um comando sem informar o caminho completo do binário. Por exemplo, o usuário pode digitar `cat /tmp/test.txt` em vez de `/bin/cat /tmp/test.txt`. Podemos verificar o conteúdo da variável `PATH` com `env | grep PATH` ou `echo $PATH`.

```bash
htb_student@NIX02:~$ echo $PATH
```

```text
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
```

Criar um script ou programa em um diretório especificado no `PATH` faz com que ele possa ser executado de qualquer diretório do sistema.

```bash
htb_student@NIX02:~$ pwd && conncheck
```

```text
/usr/local/sbin
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1189/sshd
tcp        0     88 10.129.2.12:22          10.10.14.3:43218        ESTABLISHED 1614/sshd: mrb3n [p
tcp6       0      0 :::22                   :::*                    LISTEN      1189/sshd
tcp6       0      0 :::80                   :::*                    LISTEN      1304/apache2
```

Como mostrado abaixo, o script `conncheck` criado em `/usr/local/sbin` continua funcionando mesmo quando estamos no diretório `/tmp`, porque ele foi criado em um diretório presente no `PATH`.

```bash
htb_student@NIX02:~$ pwd && conncheck
```

```text
/tmp
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1189/sshd
tcp        0    268 10.129.2.12:22          10.10.14.3:43218        ESTABLISHED 1614/sshd: mrb3n [p
tcp6       0      0 :::22                   :::*                    LISTEN      1189/sshd
tcp6       0      0 :::80                   :::*                    LISTEN      1304/apache2
```

Adicionar `.` ao `PATH` de um usuário inclui o diretório de trabalho atual na lista. Por exemplo, se conseguirmos modificar o `PATH` de um usuário, poderíamos substituir um binário comum como `ls` por um script malicioso, como um reverse shell. Se adicionarmos `.` ao caminho com `PATH=.:$PATH` e depois `export PATH`, poderemos executar binários no diretório atual apenas digitando o nome do arquivo (ou seja, ao digitar `ls`, o sistema chamará o script malicioso `ls` no diretório atual em vez do binário real em `/bin/ls`).

```bash
htb_student@NIX02:~$ echo $PATH
```

```text
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
```

```bash
htb_student@NIX02:~$ PATH=.:${PATH}
htb_student@NIX02:~$ export PATH
htb_student@NIX02:~$ echo $PATH
```

```text
.:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
```

Neste exemplo, alteramos o `PATH` para executar um comando `echo` simples quando o comando `ls` é digitado.

```bash
htb_student@NIX02:~$ touch ls
htb_student@NIX02:~$ echo 'echo "PATH ABUSE!!"' > ls
htb_student@NIX02:~$ chmod +x ls
```

```bash
htb_student@NIX02:~$ ls
```

```text
PATH ABUSE!!
```
