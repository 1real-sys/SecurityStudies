# Enumeração do Ambiente

A enumeração é a chave para a escalada de privilégios. Existem diversos scripts auxiliares, como LinPEAS e LinEnum, para ajudar nesse processo. Ainda assim, é importante entender quais informações procurar e conseguir realizar a enumeração manualmente. Quando você obtém acesso inicial ao host, é importante verificar alguns detalhes principais.

## Informações iniciais importantes

**Versão do sistema operacional:** saber a distribuição (Ubuntu, Debian, FreeBSD, Fedora, SUSE, Red Hat, CentOS etc.) ajuda a entender quais ferramentas podem estar disponíveis. Isso também identifica a versão do sistema operacional, para a qual podem existir exploits públicos.

**Versão do kernel:** assim como na versão do SO, podem existir exploits públicos direcionados a uma vulnerabilidade em uma versão específica do kernel. Exploits de kernel podem causar instabilidade no sistema ou até uma falha completa. Tenha cuidado ao executá-los em sistemas de produção e entenda totalmente o exploit e suas possíveis consequências antes de usá-lo.

**Serviços em execução:** saber quais serviços estão ativos no host é importante, especialmente os que rodam como root. Um serviço vulnerável ou mal configurado executado como root pode ser uma vitória fácil para escalada de privilégios. Falhas já foram encontradas em vários serviços comuns, como Nagios, Exim, Samba, ProFTPd etc. Existem PoCs públicas para muitos deles, como a CVE-2016-9566, uma falha de escalada local de privilégios no Nagios Core < 4.2.4.

## Obter noção do ambiente

Suponha que acabamos de obter acesso a um host Linux explorando uma vulnerabilidade de upload irrestrito de arquivos durante um teste de invasão externo. Depois de estabelecer nosso reverse shell (e, idealmente, algum tipo de persistência), devemos começar reunindo informações básicas sobre o sistema com o qual estamos lidando.

Primeiro, precisamos responder à pergunta fundamental: qual sistema operacional estamos enfrentando? Se estivermos em um host CentOS ou Red Hat Enterprise Linux, a enumeração provavelmente será um pouco diferente daquela em um host baseado em Debian, como Ubuntu. Se cairmos em um host como FreeBSD, Solaris, ou algo mais incomum, como os sistemas proprietários HP-UX ou AIX, os comandos que usaremos provavelmente serão diferentes. Embora os comandos mudem, e às vezes precisemos consultar a referência de um comando, os princípios permanecem os mesmos. Para este material, começaremos com um alvo Ubuntu para cobrir táticas e técnicas gerais. Depois de aprender o básico e combiná-lo com uma nova forma de pensar e com as etapas do processo de teste de invasão, isso não deve importar, porque teremos um processo completo e repetível.

Existem muitos cheatsheets para enumeração em Linux, e algumas informações que queremos obter podem ter duas ou mais maneiras de serem coletadas. Neste módulo, cobriremos uma metodologia que provavelmente funciona para a maioria dos sistemas Linux que encontrarmos no mundo real. Dito isso, certifique-se de entender o que os comandos fazem e como adaptá-los ou encontrar a informação de outra forma, caso um comando específico não funcione. Desafie-se durante este módulo a tentar abordagens diferentes para praticar sua metodologia e descobrir o que funciona melhor para você. Qualquer pessoa pode copiar comandos de um cheatsheet, mas um entendimento profundo do que você está procurando e de como obter isso ajudará no sucesso em qualquer ambiente.

Normalmente, queremos executar alguns comandos básicos para nos orientar:

- `whoami` - qual usuário estamos usando
- `id` - a quais grupos nosso usuário pertence?
- `hostname` - como o servidor se chama? Conseguimos tirar algo útil da convenção de nomes?
- `ifconfig` ou `ip a` - em qual sub-rede caímos? O host tem outras interfaces em outras sub-redes?
- `sudo -l` - nosso usuário pode executar algo com sudo (como outro usuário ou como root) sem precisar de senha? Isso às vezes é a vitória mais fácil, e podemos usar algo como `sudo su` para cair diretamente em um shell root.

Incluir capturas de tela dessas informações pode ser útil em um relatório ao cliente, como evidência de execução remota de código (RCE) bem-sucedida e para identificar claramente o sistema afetado. Agora vamos para uma enumeração mais detalhada e passo a passo.

## Sistema operacional e versão

Vamos começar verificando qual sistema operacional e versão estamos usando.

```bash
JLMreal@htb[/htb]$ cat /etc/os-release
```

```text
NAME="Ubuntu"
VERSION="20.04.4 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.4 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```

Podemos ver que o alvo está executando Ubuntu 20.04.4 LTS ("Focal Fossa"). Independentemente da versão encontrada, é importante verificar se ela está desatualizada ou ainda recebe manutenção. A Ubuntu publica seu ciclo de releases, e com isso vemos que "Focal Fossa" só chega ao fim da vida útil em abril de 2030. A partir dessa informação, podemos supor que talvez não encontremos uma vulnerabilidade de kernel bem conhecida, porque o cliente pode estar mantendo seu ativo exposto à internet atualizado — mas ainda assim vamos verificar.

## PATH e variáveis de ambiente

Em seguida, queremos verificar o `PATH` do usuário atual, que é onde o sistema Linux procura sempre que um comando é executado para encontrar executáveis com o nome digitado, por exemplo `id`, que neste sistema está em `/usr/bin/id`. Como veremos mais adiante, se a variável `PATH` do usuário alvo estiver mal configurada, podemos explorá-la para elevar privilégios. Por enquanto, vamos anotar isso no nosso método de registro.

```bash
JLMreal@htb[/htb]$ echo $PATH
```

```text
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

Também podemos verificar todas as variáveis de ambiente definidas para o usuário atual; talvez encontremos algo sensível, como uma senha. Vamos anotar isso e seguir.

```bash
JLMreal@htb[/htb]$ env
```

```text
SHELL=/bin/bash
PWD=/home/htb-student
LOGNAME=htb-student
XDG_SESSION_TYPE=tty
MOTD_SHOWN=pam
HOME=/home/htb-student
LANG=en_US.UTF-8

<SNIP>
```

## Versão do kernel

Agora anotamos a versão do kernel. Podemos fazer buscas para ver se o alvo está executando um kernel vulnerável — algo que poderemos explorar mais adiante no módulo — e que tenha um PoC público conhecido. Há algumas formas de obter isso; outra opção seria `cat /proc/version`, mas aqui vamos usar `uname -a`.

```bash
JLMreal@htb[/htb]$ uname -a
```

```text
Linux nixlpe02 5.4.0-122-generic #138-Ubuntu SMP Wed Jun 22 15:00:31 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
```

## Informações adicionais do host

Também podemos reunir algumas informações extras sobre o host, como o tipo e a versão da CPU:

```bash
JLMreal@htb[/htb]$ lscpu
```

```text
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   43 bits physical, 48 bits virtual
CPU(s):                          2
On-line CPU(s) list:             0,1
Thread(s) per core:              1
Core(s) per socket:              2
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       AuthenticAMD
CPU family:                      23
Model:                           49
Model name:                      AMD EPYC 7302P 16-Core Processor
Stepping:                        0
CPU MHz:                         2994.375
BogoMIPS:                        5988.75
Hypervisor vendor:               VMware

<SNIP>
```

## Shells disponíveis

Quais shells de login existem no servidor? Anote isso e destaque que tanto Tmux quanto Screen estão disponíveis.

```bash
JLMreal@htb[/htb]$ cat /etc/shells
```

```text
# /etc/shells: valid login shells
/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/bin/dash
/usr/bin/dash
/usr/bin/tmux
/usr/bin/screen
```

## Defesas e proteções

Também devemos verificar se há defesas em uso e tentar enumerar informações sobre elas. Alguns itens para procurar incluem:

- Exec Shield
- iptables
- AppArmor
- SELinux
- Fail2ban
- Snort
- Uncomplicated Firewall (ufw)

Muitas vezes não teremos privilégios para enumerar a configuração dessas proteções, mas saber o que está em uso, se houver algo, ajuda a evitar perda de tempo em certas atividades.

## Discos, montagens e compartilhamentos

Em seguida, podemos examinar os discos e compartilhamentos no sistema. Primeiro, usamos `lsblk` para obter informações sobre dispositivos de bloco no sistema (discos rígidos, USB, unidades ópticas etc.). Se descobrirmos e conseguirmos montar um disco adicional ou um sistema de arquivos desmontado, podemos encontrar arquivos sensíveis, senhas ou backups que possam ser usados para escalada de privilégios.

```bash
JLMreal@htb[/htb]$ lsblk
```

```text
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
loop0                       7:0    0   55M  1 loop /snap/core18/1705
loop1                       7:1    0   69M  1 loop /snap/lxd/14804
loop2                       7:2    0   47M  1 loop /snap/snapd/16292
loop3                       7:3    0  103M  1 loop /snap/lxd/23339
loop4                       7:4    0   62M  1 loop /snap/core20/1587
loop5                       7:5    0 55.6M  1 loop /snap/core18/2538
sda                         8:0    0   20G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0    1G  0 part /boot
└─sda3                      8:3    0   19G  0 part
  └─ubuntu--vg-ubuntu--lv 253:0    0   18G  0 lvm  /
sr0                        11:0    1  908M  0 rom
```

O comando `lpstat` pode ser usado para encontrar informações sobre impressoras conectadas ao sistema. Se houver trabalhos ativos ou na fila, poderemos acessar algum tipo de informação sensível?

Também devemos verificar se há unidades montadas e desmontadas. Podemos montar uma unidade não montada e obter acesso a dados sensíveis? Podemos encontrar credenciais em `fstab` para sistemas montados pesquisando palavras comuns como `password`, `username`, `credential`, etc. em `/etc/fstab`?

```bash
JLMreal@htb[/htb]$ cat /etc/fstab
```

```text
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/ubuntu-vg/ubuntu-lv during curtin installation
/dev/disk/by-id/dm-uuid-LVM-BdLsBLE4CvzJUgtkugkof4S0dZG7gWR8HCNOlRdLWoXVOba2tYUMzHfFQAP9ajul / ext4 defaults 0 0
# /boot was on /dev/sda2 during curtin installation
/dev/disk/by-uuid/20b1770d-a233-4780-900e-7c99bc974346 /boot ext4 defaults 0 0
```

## Tabela de rotas e ARP

Verifique a tabela de rotas digitando `route` ou `netstat -rn`. Aqui conseguimos ver quais outras redes estão disponíveis e por qual interface.

```bash
JLMreal@htb[/htb]$ route
```

```text
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         _gateway        0.0.0.0         UG    0      0        0 ens192
10.129.0.0      0.0.0.0         255.255.0.0     U     0      0        0 ens192
```

Em um ambiente de domínio, certamente vamos querer verificar `/etc/resolv.conf`. Se o host estiver configurado para usar DNS interno, isso pode nos dar um ponto de partida para consultar o ambiente do Active Directory.

Também vamos querer verificar a tabela ARP para ver com quais outros hosts o alvo já se comunicou.

```bash
JLMreal@htb[/htb]$ arp -a
```

```text
_gateway (10.129.0.1) at 00:50:56:b9:b9:fc [ether] on ens192
```

## Usuários existentes

A enumeração do ambiente também inclui conhecer os usuários que existem no sistema alvo. Isso é importante porque usuários individuais geralmente são configurados durante a instalação de aplicativos e serviços para limitar os privilégios do serviço. O objetivo disso é manter a segurança do sistema. Se um serviço estiver rodando com privilégios máximos (root) e for comprometido por um atacante, esse atacante passa a ter o maior nível de acesso sobre todo o sistema. Todos os usuários do sistema ficam armazenados em `/etc/passwd`. O formato nos dá algumas informações, como:

- Nome de usuário
- Senha
- UID
- GID
- Informações do usuário
- Diretório home
- Shell

### Usuários existentes

```bash
JLMreal@htb[/htb]$ cat /etc/passwd
```

```text
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
tcpdump:x:108:115::/nonexistent:/usr/sbin/nologin
mrb3n:x:1000:1000:mrb3n:/home/mrb3n:/bin/bash
bjones:x:1001:1001::/home/bjones:/bin/sh
administrator.ilfreight:x:1002:1002::/home/administrator.ilfreight:/bin/sh
backupsvc:x:1003:1003::/home/backupsvc:/bin/sh
cliff.moore:x:1004:1004::/home/cliff.moore:/bin/bash
logger:x:1005:1005::/home/logger:/bin/sh
shared:x:1006:1006::/home/shared:/bin/sh
stacey.jenkins:x:1007:1007::/home/stacey.jenkins:/bin/bash
htb-student:x:1008:1008::/home/htb-student:/bin/bash
<SNIP>
```

Às vezes vemos hashes de senha diretamente em `/etc/passwd`. Esse arquivo é legível por todos os usuários e, assim como hashes em `/etc/shadow`, pode ser alvo de ataque offline de cracking. Essa configuração não é comum, mas às vezes aparece em dispositivos embarcados e roteadores.

```bash
JLMreal@htb[/htb]$ cat /etc/passwd | cut -f1 -d:
```

```text
root
daemon
bin
sys

...SNIP...

mrb3n
lxd
bjones
administrator.ilfreight
backupsvc
cliff.moore
logger
shared
stacey.jenkins
htb-student
```

No Linux, vários algoritmos diferentes podem ser usados para tornar as senhas irreconhecíveis. Identificá-los pelos primeiros blocos do hash pode ajudar no uso posterior. Eis os mais comuns:

| Algoritmo | Hash |
|---|---|
| Salted MD5 | `$1$...` |
| SHA-256 | `$5$...` |
| SHA-512 | `$6$...` |
| BCrypt | `$2a$...` |
| Scrypt | `$7$...` |
| Argon2 | `$argon2i$...` |

Também vamos querer verificar quais usuários têm shells de login. Depois de ver quais shells existem no sistema, podemos checar cada versão por vulnerabilidades. Por exemplo, versões desatualizadas do Bash, como a 4.1, são vulneráveis ao Shellshock.

```bash
JLMreal@htb[/htb]$ grep "sh$" /etc/passwd
```

```text
root:x:0:0:root:/root:/bin/bash
mrb3n:x:1000:1000:mrb3n:/home/mrb3n:/bin/bash
bjones:x:1001:1001::/home/bjones:/bin/sh
administrator.ilfreight:x:1002:1002::/home/administrator.ilfreight:/bin/sh
backupsvc:x:1003:1003::/home/backupsvc:/bin/sh
cliff.moore:x:1004:1004::/home/cliff.moore:/bin/bash
logger:x:1005:1005::/home/logger:/bin/sh
shared:x:1006:1006::/home/shared:/bin/sh
stacey.jenkins:x:1007:1007::/home/stacey.jenkins:/bin/bash
htb-student:x:1008:1008::/home/htb-student:/bin/bash
```

## Grupos

Cada usuário em sistemas Linux é atribuído a um ou mais grupos e, assim, recebe privilégios específicos. Por exemplo, se houver uma pasta chamada `dev` apenas para desenvolvedores, o usuário precisa estar no grupo apropriado para acessá-la. As informações sobre os grupos disponíveis ficam em `/etc/group`, que mostra o nome do grupo e os nomes de usuários atribuídos.

### Grupos existentes

```bash
JLMreal@htb[/htb]$ cat /etc/group
```

```text
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,htb-student
tty:x:5:syslog
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:
fax:x:21:
voice:x:22:
cdrom:x:24:htb-student
floppy:x:25:
tape:x:26:
sudo:x:27:mrb3n,htb-student
audio:x:29:pulse
dip:x:30:htb-student
www-data:x:33:
...SNIP...
```

O arquivo `/etc/group` lista todos os grupos do sistema. Podemos usar o comando `getent` para listar membros de qualquer grupo interessante.

```bash
JLMreal@htb[/htb]$ getent group sudo
```

```text
sudo:x:27:mrb3n
```

## Diretórios /home

Também podemos verificar quais usuários têm uma pasta em `/home`. Vamos enumerar cada uma para ver se algum usuário do sistema está armazenando dados sensíveis ou arquivos com senhas. Devemos checar se arquivos como `.bash_history` são legíveis e se contêm comandos interessantes, além de procurar arquivos de configuração. Não é incomum encontrar arquivos com credenciais que podem ser usadas para acessar outros sistemas ou até ganhar entrada em um ambiente de Active Directory. Também é importante procurar chaves SSH de todos os usuários, pois elas podem ser usadas para persistência, escalada de privilégios ou para pivoting e port forwarding dentro da rede interna. No mínimo, verifique o cache ARP para ver quais hosts estão sendo acessados e cruze isso com quaisquer chaves privadas SSH utilizáveis.

```bash
JLMreal@htb[/htb]$ ls /home
```

```text
administrator.ilfreight  bjones       htb-student  mrb3n   stacey.jenkins
backupsvc                cliff.moore  logger       shared
```

## Arquivos de configuração e "low hanging fruit"

Por fim, podemos procurar por arquivos de fácil acesso, como arquivos de configuração e outros que possam conter informações sensíveis. Arquivos de configuração podem guardar uma grande quantidade de informações. Vale a pena pesquisar todos os arquivos com extensões como `.conf` e `.config` em busca de nomes de usuário, senhas e outros segredos.

Se encontrarmos senhas, devemos testá-las imediatamente em todos os usuários presentes no sistema. Reutilização de senha é comum, então podemos ter sorte.

Em Linux, existem muitos locais onde esses arquivos podem ser armazenados, incluindo sistemas de arquivos montados. Um sistema de arquivos montado é um sistema conectado a um diretório específico do sistema e acessado por meio desse diretório. Muitos sistemas de arquivos, como ext4, NTFS e FAT32, podem ser montados. Cada tipo tem vantagens e desvantagens. Por exemplo, alguns podem ser apenas leitura para o sistema operacional, enquanto outros podem ser lidos e gravados pelo usuário. Sistemas de arquivos que podem ser lidos e gravados são chamados de read/write. Montar um sistema de arquivos permite acessar os arquivos e pastas armazenados nele. Para montar um sistema de arquivos, o usuário deve ter privilégios de root. Depois de montado, ele pode ser desmontado pelo usuário com privilégios de root. Podemos ter acesso a esses sistemas e encontrar informações sensíveis, documentação ou aplicações.

### Sistemas de arquivos montados

```bash
JLMreal@htb[/htb]$ df -h
```

```text
Filesystem      Size  Used Avail Use% Mounted on
udev            1,9G     0  1,9G   0% /dev
tmpfs           389M    1,8M   388M   1% /run
/dev/sda5        20G   7,9G    11G  44% /
tmpfs           1,9G     0  1,9G   0% /dev/shm
tmpfs           5,0M   4,0K  5,0M   1% /run/lock
tmpfs           1,9G     0  1,9G   0% /sys/fs/cgroup
/dev/loop0      128K  128K     0 100% /snap/bare/5
/dev/loop1       62M   62M     0 100% /snap/core20/1611
/dev/loop2       92M   92M     0 100% /snap/gtk-common-themes/1535
/dev/loop4       55M   55M     0 100% /snap/snap-store/558
/dev/loop3      347M  347M     0 100% /snap/gnome-3-38-2004/115
/dev/loop5       47M   47M     0 100% /snap/snapd/16292
/dev/sda1       511M  4,0K  511M   1% /boot/efi
tmpfs           389M   24K  389M   1% /run/user/1000
/dev/sr0        3,6G  3,6G     0 100% /media/htb-student/Ubuntu 20.04.5 LTS amd64
/dev/loop6       50M   50M     0 100% /snap/snapd/17576
/dev/loop7       64M   64M     0 100% /snap/core20/1695
/dev/loop8       46M   46M     0 100% /snap/snap-store/599
/dev/loop9      347M  347M     0 100% /snap/gnome-3-38-2004/119
```

Quando um sistema de arquivos é desmontado, ele deixa de estar acessível pelo sistema. Isso pode acontecer por vários motivos, como a remoção de um disco ou porque o sistema de arquivos não é mais necessário. Outra razão pode ser impedir que arquivos, scripts, documentos e outras informações importantes sejam montados e visualizados por um usuário comum. Portanto, se conseguirmos aumentar nossos privilégios até root, poderemos montar e ler esses sistemas nós mesmos. Sistemas de arquivos desmontados podem ser vistos da seguinte forma:

### Sistemas de arquivos não montados

```bash
JLMreal@htb[/htb]$ cat /etc/fstab | grep -v "#" | column -t
```

```text
UUID=5bf16727-fcdf-4205-906c-0620aa4a058f  /          ext4  errors=remount-ro  0  1
UUID=BE56-AAE0                             /boot/efi  vfat  umask=0077         0  1
/swapfile                                  none       swap  sw                 0  0
```

## Arquivos e diretórios ocultos

Muitas pastas e arquivos são ocultados em um sistema Linux para não ficarem óbvios e para evitar edições acidentais. Existem muitos motivos para manter esses itens ocultos, além dos já mencionados. Mesmo assim, precisamos conseguir localizar todos os arquivos e diretórios ocultos, porque eles podem conter informações sensíveis, mesmo quando só temos permissão de leitura.

### Todos os arquivos ocultos

```bash
JLMreal@htb[/htb]$ find / -type f -name ".*" -exec ls -l {} \; 2>/dev/null | grep htb-student
```

```text
-rw-r--r-- 1 htb-student htb-student 3771 Nov 27 11:16 /home/htb-student/.bashrc
-rw-rw-r-- 1 htb-student htb-student 180 Nov 27 11:36 /home/htb-student/.wget-hsts
-rw------- 1 htb-student htb-student 387 Nov 27 14:02 /home/htb-student/.bash_history
-rw-r--r-- 1 htb-student htb-student 807 Nov 27 11:16 /home/htb-student/.profile
-rw-r--r-- 1 htb-student htb-student 0 Nov 27 11:31 /home/htb-student/.sudo_as_admin_successful
-rw-r--r-- 1 htb-student htb-student 220 Nov 27 11:16 /home/htb-student/.bash_logout
-rw-rw-r-- 1 htb-student htb-student 162 Nov 28 13:26 /home/htb-student/.notes
```

### Todos os diretórios ocultos

```bash
JLMreal@htb[/htb]$ find / -type d -name ".*" -ls 2>/dev/null
```

```text
   684822      4 drwx------   3 htb-student htb-student     4096 Nov 28 12:32 /home/htb-student/.gnupg
   790793      4 drwx------   2 htb-student htb-student     4096 Okt 27 11:31 /home/htb-student/.ssh
   684804      4 drwx------  10 htb-student htb-student     4096 Okt 27 11:30 /home/htb-student/.cache
   790827      4 drwxrwxr-x   8 htb-student htb-student     4096 Okt 27 11:32 /home/htb-student/CVE-2021-3156/.git
   684796      4 drwx------  10 htb-student htb-student     4096 Okt 27 11:30 /home/htb-student/.config
   655426      4 drwxr-xr-x   3 htb-student htb-student     4096 Okt 27 11:19 /home/htb-student/.local
   524808      4 drwxr-xr-x   7 gdm         gdm             4096 Okt 27 11:19 /var/lib/gdm3/.cache
   544027      4 drwxr-xr-x   7 gdm         gdm             4096 Okt 27 11:19 /var/lib/gdm3/.config
   544028      4 drwxr-xr-x   3 gdm         gdm             4096 Aug 31 08:54 /var/lib/gdm3/.local
   524938      4 drwx------   2 colord      colord          4096 Okt 27 11:19 /var/lib/colord/.cache
     1408      2 dr-xr-xr-x   1 htb-student htb-student     2048 Aug 31 09:17 /media/htb-student/Ubuntu\ 20.04.5\ LTS\ amd64/.disk
   280101      4 drwxrwxrwt   2 root        root            4096 Nov 28 12:31 /tmp/.font-unix
   262364      4 drwxrwxrwt   2 root        root            4096 Nov 28 12:32 /tmp/.ICE-unix
   262362      4 drwxrwxrwt   2 root        root            4096 Nov 28 12:32 /tmp/.X11-unix
   280103      4 drwxrwxrwt   2 root        root            4096 Nov 28 12:31 /tmp/.Test-unix
   262830      4 drwxrwxrwt   2 root        root            4096 Nov 28 12:31 /tmp/.XIM-unix
   661820      4 drwxr-xr-x   5 root        root            4096 Aug 31 08:55 /usr/lib/modules/5.15.0-46-generic/vdso/.build-id
   666709      4 drwxr-xr-x   5 root        root            4096 Okt 27 11:18 /usr/lib/modules/5.15.0-52-generic/vdso/.build-id
   657527      4 drwxr-xr-x 170 root        root            4096 Aug 31 08:55 /usr/lib/debug/.build-id
```

Além disso, três pastas padrão são destinadas a arquivos temporários. Elas são visíveis para todos os usuários e podem ser lidas. Logs temporários ou saída de scripts também podem ser encontrados ali. Tanto `/tmp` quanto `/var/tmp` são usados para armazenar dados temporariamente. No entanto, a diferença principal é por quanto tempo os dados permanecem nesses sistemas de arquivos. O tempo de retenção em `/var/tmp` é bem maior do que em `/tmp`. Por padrão, todos os arquivos e dados armazenados em `/var/tmp` são mantidos por até 30 dias. Em `/tmp`, por outro lado, os dados são automaticamente excluídos após dez dias.

Além disso, todos os arquivos temporários armazenados em `/tmp` são apagados imediatamente quando o sistema é reiniciado. Por isso, `/var/tmp` é usado por programas para guardar dados que precisam permanecer entre reinicializações por um período temporário.

### Arquivos temporários

```bash
JLMreal@htb[/htb]$ ls -l /tmp /var/tmp /dev/shm
```

```text
/dev/shm:
total 0

/tmp:
total 52
-rw------- 1 htb-student htb-student    0 Nov 28 12:32 config-err-v8LfEU
drwx------ 3 root        root        4096 Nov 28 12:37 snap.snap-store
drwx------ 2 htb-student htb-student 4096 Nov 28 12:32 ssh-OKlLKjlc98xh
<SNIP>
drwx------ 2 htb-student htb-student 4096 Nov 28 12:37 tracker-extract-files.1000
drwx------ 2 gdm         gdm         4096 Nov 28 12:31 tracker-extract-files.125

/var/tmp:
total 28
drwx------ 3 root root 4096 Nov 28 12:31 systemd-private-7b455e62ec09484b87eff41023c4ca53-colord.service-RrPcyi
drwx------ 3 root root 4096 Nov 28 12:31 systemd-private-7b455e62ec09484b87eff41023c4ca53-ModemManager.service-4Rej9e
...SNIP...
```

## Indo adiante

Já obtivemos uma visão inicial do ambiente e, com sorte, alguns dados sensíveis ou úteis que podem nos ajudar a escalar privilégios ou até nos mover lateralmente na rede interna. Em seguida, vamos focar em permissões e verificar quais diretórios, scripts, binários etc. podemos ler e escrever com os privilégios atuais do usuário.

Embora este módulo foque em enumeração manual, vale a pena executar o linPEAS nesse ponto em uma avaliação real para termos o máximo de dados possível para analisar. Muitas vezes encontramos uma vitória fácil, mas ter essa saída em mãos pode revelar problemas mais sutis que a enumeração manual deixou passar. Ainda assim, devemos praticar bastante a enumeração manual e criar — e continuar ampliando — nosso próprio cheatsheet de comandos importantes (e alternativas para diferentes sistemas Linux). Assim, vamos desenvolver nosso próprio estilo, preferências de comandos e até identificar áreas que podemos automatizar por conta própria. Ferramentas são ótimas e têm seu lugar, mas muitas falham quando precisamos executar uma tarefa e não conseguimos colocá-las no sistema.
