# Comandos Principais de Enumeração de Serviços e Internals

| Comando | Objetivo | Resultado esperado |
|---|---|---|
| `ip a` | Ver interfaces e endereçamento IP | Interfaces ativas, IPs e IPv6 |
| `cat /etc/hosts` | Checar mapeamentos locais | Hostnames e entradas locais úteis |
| `lastlog` | Ver último login de cada usuário | Histórico de acesso por conta |
| `w` | Ver usuários logados agora | Sessões ativas no sistema |
| `history` | Ver histórico do shell atual | Comandos recentes do usuário |
| `find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null` | Encontrar arquivos de histórico | Arquivos de histórico adicionais |
| `ls -la /etc/cron.daily/` | Enumerar cron jobs diários | Tarefas agendadas e scripts executados |
| `find /proc -name cmdline -exec cat {} \; 2>/dev/null pipe tr " " "\n"` | Ver linhas de comando dos processos | Processos e argumentos em execução |
| `apt list --installed pipe tr "/" " " pipe cut -d" " -f1,3 pipe sed 's/[0-9]://g' pipe tee -a installed_pkgs.list` | Listar pacotes instalados | Inventário de software do host |
| `sudo -V` | Ver versão do sudo | Versão e detalhes do sudo |
| `ls -l /bin /usr/bin/ /usr/sbin/` | Enumerar binários disponíveis | Ferramentas e utilitários instalados |
| for i in $(curl -s https://gtfobins.org/api.json pipe jq -r '.executables pipe keys[]'); do if grep -q "$i" installed_pkgs.list; then echo "Check for GTFO: $i";fi; done | Listar binários do GTFOBins | Binários potencialmente abusáveis |
| `strace ping -c1 <IP>` | Rastrear chamadas de sistema de um binário | Comportamento interno e acessos |
| `find / -type f \( -name *.conf -o -name *.config \) -exec ls -l {} \; 2>/dev/null` | Encontrar arquivos de configuração | Configs legíveis e possíveis segredos |
| `find / -type f -name "*.sh" 2>/dev/null | grep -v "src\|snap\|share"` | Encontrar scripts no sistema | Scripts úteis para análise |
| `ps aux | grep root` | Ver processos executados por root | Serviços e binários privilegiados |

