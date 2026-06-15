# Comandos Principais de Enumeração

| Comando | Objetivo | Resultado esperado |
|---|---|---|
| `whoami` | Identificar o usuário atual | Nome do usuário em execução |
| `id` | Ver UID, GID e grupos do usuário | Informações de identidade e grupos |
| `hostname` | Descobrir o nome do host | Nome do servidor/alvo |
| `ifconfig` / `ip a` | Enumerar interfaces e IPs | Interfaces, sub-redes e endereços |
| `sudo -l` | Ver permissões sudo sem senha | Comandos permitidos via sudo |
| `cat /etc/os-release` | Identificar SO e versão | Distribuição e release do sistema |
| `echo $PATH` | Ver caminhos de busca de executáveis | Lista de diretórios do PATH |
| `env` | Listar variáveis de ambiente | Variáveis úteis ou sensíveis |
| `uname -a` | Obter versão do kernel | Nome do kernel e build |
| `lscpu` | Coletar dados da CPU | Arquitetura e detalhes do processador |
| `cat /etc/shells` | Listar shells válidos | Shells disponíveis no sistema |
| `lsblk` | Enumerar discos e partições | Dispositivos de bloco e montagens |
| `cat /etc/fstab` | Ver sistemas de arquivos configurados | Montagens permanentes e possíveis segredos |
| `route` / `netstat -rn` | Ver tabela de rotas | Redes acessíveis e interfaces |
| `arp -a` | Ver cache ARP | Hosts com os quais o alvo se comunicou |
| `cat /etc/passwd` | Enumerar usuários do sistema | Lista de contas locais |
| `cat /etc/passwd | cut -f1 -d:` | Extrair apenas nomes de usuário | Lista simples de usuários |
| `grep "sh$" /etc/passwd` | Encontrar usuários com shell de login | Contas interativas válidas |
| `cat /etc/group` | Enumerar grupos do sistema | Grupos e membros atribuídos |
| `getent group sudo` | Ver membros de um grupo específico | Usuários dentro do grupo `sudo` |
| `ls /home` | Listar diretórios home existentes | Contas com diretório pessoal |
| `df -h` | Ver sistemas de arquivos montados | Espaço usado, livre e pontos de montagem |
| `cat /etc/fstab | grep -v "#" | column -t` | Ver montagens não comentadas | Sistemas de arquivos configurados |
| `find / -type f -name ".*" -exec ls -l {} \; 2>/dev/null` | Encontrar arquivos ocultos | Arquivos escondidos relevantes |
| `find / -type d -name ".*" -ls 2>/dev/null` | Encontrar diretórios ocultos | Diretórios escondidos relevantes |
| `ls -l /tmp /var/tmp /dev/shm` | Ver arquivos temporários | Artefatos temporários e possíveis pistas |

