# Comandos Principais - Escaping Restricted Shells

| Comando | Objetivo | Resultado esperado |
|---|---|---|
| `ls -l \`pwd\`` | Injetar/substituir comando dentro de um comando permitido (`ls`) | Execução de `pwd` indiretamente e exibição do diretório atual |
| `ls -l` | Exemplo de comando permitido no shell restrito | Listagem detalhada de arquivos (sem escapar da restrição) |
| `ls -a` | Outro exemplo comum de comando permitido no shell restrito | Listagem incluindo arquivos ocultos |
| `comando1 ; comando2` | Encadear comandos com `;` para tentar executar um comando não restrito | Execução sequencial de dois comandos |
| `comando1 \| comando2` | Encadear comandos com pipe para tentar contornar filtros | Saída de `comando1` usada como entrada de `comando2` |

