# Enumeração de Serviços e Internals no Linux

Depois de explorar o ambiente e entender o contexto geral, além de descobrir o máximo possível sobre permissões de usuário e grupo relacionadas a arquivos, scripts, binários e diretórios, vamos um passo além e olhar mais profundamente os internals do sistema operacional hospedeiro. Nesta fase, vamos enumerar os seguintes pontos, que ajudam a orientar vários dos ataques discutidos nas seções posteriores deste módulo:

- Quais serviços e aplicações estão instalados?
- Quais serviços estão em execução?
- Quais sockets estão em uso?
- Quais usuários, administradores e grupos existem no sistema?
- Quem está logado agora? Quais usuários fizeram login recentemente?
- Quais políticas de senha, se houver, são aplicadas no host?
- O host está ingressado em um domínio Active Directory?
- Que tipos de informações interessantes podemos encontrar em arquivos de histórico, log e backup?
- Quais arquivos foram modificados recentemente e com que frequência? Há algum padrão interessante que possa indicar um cron job que possamos sequestrar?
- Informações atuais de endereçamento IP
- Há algo interessante no arquivo `/etc/hosts`?
- Existem conexões de rede interessantes com outros sistemas na rede interna ou até fora dela?
- Quais ferramentas estão instaladas no sistema e que podem ser úteis para nós? (Netcat, Perl, Python, Ruby, Nmap, tcpdump, gcc etc.)
- Conseguimos acessar o `bash_history` de algum usuário e descobrir algo útil a partir do histórico de comandos?
- Há algum cron job em execução no sistema que possamos sequestrar?

Neste momento, também queremos reunir o máximo possível de informações de rede. Qual é nosso IP atual? O sistema tem outras interfaces e, por isso, poderia ser usado para pivotar para uma sub-rede antes inacessível? Fazemos isso com `ip a` ou `ifconfig`, mas esse comando pode não funcionar em alguns sistemas se o pacote `net-tools` não estiver presente.

## Internals

Quando falamos em internals, queremos dizer a configuração interna e a forma de funcionamento do sistema, incluindo processos integrados projetados para executar tarefas específicas. Então começamos pelas interfaces pelas quais o sistema alvo pode se comunicar.

### Interfaces de rede

```bash
JLMreal@htb[/htb]$ ip a
```

```text
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:50:56:b9:ed:2a brd ff:ff:ff:ff:ff:ff
    inet 10.129.203.168/16 brd 10.129.255.255 scope global dynamic ens192
       valid_lft 3092sec preferred_lft 3092sec
    inet6 dead:beef::250:56ff:feb9:ed2a/64 scope global dynamic mngtmpaddr
       valid_lft 86400sec preferred_lft 14400sec
    inet6 fe80::250:56ff:feb9:ed2a/64 scope link
       valid_lft forever preferred_lft forever
```

### `/etc/hosts`

Também é útil verificar se há algo interessante em `/etc/hosts`.

```bash
JLMreal@htb[/htb]$ cat /etc/hosts
```

```text
127.0.0.1 localhost
127.0.1.1 nixlpe02
# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

### Último login dos usuários

Também pode ser útil verificar a hora do último login de cada usuário para entender quando eles normalmente acessam o sistema e com que frequência. Isso nos dá uma ideia de quão usado esse sistema é e se isso pode abrir espaço para mais falhas de configuração ou diretórios e históricos "bagunçados".

```bash
JLMreal@htb[/htb]$ lastlog
```

```text
Username         Port     From             Latest
root                                       **Never logged in**
daemon                                     **Never logged in**
...
mrb3n            pts/1    10.10.14.15      Tue Aug  2 19:33:16 +0000 2022
...
htb-student      pts/0    10.10.14.15      Wed Aug  3 13:37:22 +0000 2022
```

### Usuários logados agora

Também é importante verificar quem está atualmente no sistema conosco. Há algumas formas de fazer isso, como o comando `who`. O comando `finger` também pode exibir essa informação em alguns sistemas Linux. Aqui vemos que o usuário `cliff.moore` está logado no sistema junto conosco.

```bash
JLMreal@htb[/htb]$ w
```

```text
  12:27:21 up 1 day, 16:55,  1 user,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
cliff.mo  pts/0    10.10.14.16      Tue19   40:54m  0.02s  0.02s -bash
```

### Histórico de comandos

Também é importante verificar o histórico do bash de um usuário, pois ele pode estar passando senhas como argumento na linha de comando, trabalhando com repositórios git, configurando cron jobs e muito mais. Revisar o que o usuário tem feito pode fornecer bastante contexto sobre o tipo de servidor em que caímos e dar pistas sobre caminhos de escalada de privilégio.

```bash
JLMreal@htb[/htb]$ history
```

```text
    1  id
    2  cd /home/cliff.moore
    3  exit
    4  touch backup.sh
    5  tail /var/log/apache2/error.log
    6  ssh ec2-user@dmz02.inlanefreight.local
    7  history
```

### Encontrando arquivos de histórico

Às vezes também encontramos arquivos de histórico especiais criados por scripts ou programas. Isso pode ocorrer, entre outros casos, em scripts que monitoram certas atividades dos usuários e verificam atividades suspeitas.

```bash
JLMreal@htb[/htb]$ find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null
```

```text
-rw------- 1 htb-student htb-student 387 Nov 27 14:02 /home/htb-student/.bash_history
```

### Cron

Também é uma boa ideia verificar se há cron jobs no sistema. Cron jobs em Linux são semelhantes às tarefas agendadas do Windows. Normalmente são configurados para manutenção e backup. Em conjunto com outras falhas de configuração, como paths relativos ou permissões fracas, eles podem ser explorados para escalar privilégios quando o cron job for executado.

```bash
JLMreal@htb[/htb]$ ls -la /etc/cron.daily/
```

```text
total 48
drwxr-xr-x  2 root root 4096 Aug  2 17:36 .
drwxr-xr-x 96 root root 4096 Aug  2 19:34 ..
-rwxr-xr-x  1 root root  376 Dec  4  2019 apport
...
```

### Proc

O filesystem `proc` (`proc` / `procfs`) é um filesystem especial no Linux que contém informações sobre processos do sistema, hardware e outros dados. Ele é a principal forma de acessar informações de processos e pode ser usado para ver e modificar configurações do kernel. É virtual e não existe como um filesystem real; ele é gerado dinamicamente pelo kernel. Pode ser usado para obter informações como o estado de processos em execução, parâmetros do kernel, memória do sistema e dispositivos.

```bash
JLMreal@htb[/htb]$ find /proc -name cmdline -exec cat {} \; 2>/dev/null | tr " " "\n"
```

```text
...SNIP...
root@10.129.14.200sshroot@10.129.14.200sshd:
htb-student
[priv]sshd:
htb-student
...
```

## Serviços

Se for um sistema Linux um pouco mais antigo, aumenta a chance de encontrarmos pacotes instalados que já tenham pelo menos uma vulnerabilidade. Porém, distribuições mais novas também podem ter pacotes ou softwares antigos instalados. Por isso, veremos uma forma de detectar pacotes potencialmente perigosos. Para isso, primeiro criamos uma lista de pacotes instalados para trabalhar.

### Pacotes instalados

```bash
JLMreal@htb[/htb]$ apt list --installed | tr "/" " " | cut -d" " -f1,3 | sed 's/[0-9]://g' | tee -a installed_pkgs.list
```

```text
accountsservice-ubuntu-schemas 0.0.7+17.10.20170922-0ubuntu1
accountsservice 0.6.55-0ubuntu12~20.04.5
acl 2.2.53-6
...
```

### Versão do sudo

Também é uma boa ideia verificar se a versão do sudo instalada no sistema é vulnerável a exploits antigos ou recentes.

```bash
JLMreal@htb[/htb]$ sudo -V
```

```text
Sudo version 1.8.31
Sudoers policy plugin version 1.8.31
Sudoers file grammar version 46
Sudoers I/O plugin version 1.8.31
```

### Binários

Às vezes não há pacotes diretamente instalados no sistema, mas sim programas compilados na forma de binários. Eles não precisam de instalação e podem ser executados diretamente pelo sistema.

```bash
JLMreal@htb[/htb]$ ls -l /bin /usr/bin/ /usr/sbin/
```

```text
lrwxrwxrwx 1 root root     7 Oct 27 11:14 /bin -> usr/bin

/usr/bin/:
total 175160
...

/usr/sbin/:
total 32500
...
```

O projeto GTFObins oferece uma excelente base com uma lista de binários que podem ser explorados para elevar privilégios no sistema alvo. Com o oneliner a seguir, podemos comparar os binários existentes com os do GTFObins para ver quais merecem investigação posterior.

```bash
JLMreal@htb[/htb]$ for i in $(curl -s https://gtfobins.org/api.json | jq -r '.executables | keys[]'); do if grep -q "$i" installed_pkgs.list; then echo "Check for GTFO: $i";fi; done
```

## Ferramentas úteis para análise

Podemos usar a ferramenta de diagnóstico `strace` em sistemas Linux para rastrear e analisar system calls e o tratamento de sinais. Ela permite acompanhar o fluxo de um programa e entender como ele acessa recursos do sistema, processa sinais e envia/recebe dados do sistema operacional. Também pode ser usada para monitorar atividades relacionadas à segurança e identificar vetores de ataque potenciais, como requisições específicas a hosts remotos usando senhas ou tokens.

```bash
JLMreal@htb[/htb]$ strace ping -c1 10.129.112.20
```

```text
execve("/usr/bin/ping", ["ping", "-c1", "10.129.112.20"], 0x7ffdc8b96cc0 /* 80 vars */) = 0
...
```

## Arquivos de configuração

Usuários conseguem ler quase todos os arquivos de configuração em um sistema Linux se o administrador os tiver mantido com permissões padrão. Esses arquivos frequentemente revelam como um serviço foi configurado e nos ajudam a entender melhor como usá-lo. Além disso, eles podem conter informações sensíveis, como chaves e caminhos para arquivos em diretórios que não conseguimos ver. Porém, se o arquivo tiver permissão de leitura para todos, ainda poderemos lê-lo mesmo sem permissão no diretório.

```bash
JLMreal@htb[/htb]$ find / -type f \( -name *.conf -o -name *.config \) -exec ls -l {} \; 2>/dev/null
```

```text
-rw-r--r-- 1 root root 448 Nov 28 12:31 /run/tmpfiles.d/static-nodes.conf
-rw-r--r-- 1 root root 71 Nov 28 12:31 /run/NetworkManager/resolv.conf
...
```

## Scripts

Os scripts são parecidos com os arquivos de configuração. Muitas vezes os administradores são descuidados e confiam excessivamente na segurança da rede, negligenciando a segurança interna dos sistemas. Em alguns casos, esses scripts têm permissões incorretas, mas mesmo sem isso o conteúdo já é muito importante. Através deles, podemos descobrir processos internos e individuais que podem ser muito úteis.

```bash
JLMreal@htb[/htb]$ find / -type f -name "*.sh" 2>/dev/null | grep -v "src\|snap\|share"
```

```text
/home/htb-student/automation.sh
/etc/wpa_supplicant/action_wpa.sh
/etc/wpa_supplicant/ifupdown.sh
...
```

## Serviços em execução por usuário

Se olharmos a lista de processos, ela pode nos dar informações sobre quais scripts ou binários estão em uso e por qual usuário. Então, por exemplo, se for um script criado pelo administrador em seu path e cujos direitos não foram restringidos, podemos executá-lo sem entrar no diretório root.

```bash
JLMreal@htb[/htb]$ ps aux | grep root
```

```text
root           1  2.0  0.2 168196 11364 ?        Ss   12:31   0:01 /sbin/init splash
root         378  0.5  0.4  62648 17212 ?        S<s  12:31   0:00 /lib/systemd/systemd-journald
...
```

Esse levantamento já nos dá uma boa visão geral do sistema alvo, então podemos seguir com mais detalhes e descobrir as permissões individuais dos componentes que encontramos.
