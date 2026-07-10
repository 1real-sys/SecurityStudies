# Comandos Principais - Path Abuse

| Comando | Objetivo | Resultado esperado |
|---|---|---|
| `env \| grep PATH` | Ver a variável `PATH` filtrada | Caminhos usados para localizar executáveis |
| `echo $PATH` | Exibir o conteúdo atual do `PATH` | Lista de diretórios na ordem de busca |
| `pwd && conncheck` | Ver diretório atual e testar execução via `PATH` | `conncheck` executando mesmo fora do diretório original |
| `PATH=.:${PATH}` | Adicionar o diretório atual (`.`) ao início do `PATH` | Prioridade de execução para binários do diretório atual |
| `export PATH` | Aplicar/exportar a alteração do `PATH` na sessão | Novo `PATH` ativo para comandos seguintes |
| `touch ls` | Criar arquivo chamado `ls` no diretório atual | Arquivo base para simular sequestro de comando |
| `echo 'echo "PATH ABUSE!!"' > ls` | Escrever payload simples no arquivo `ls` | Script malicioso pronto |
| `chmod +x ls` | Tornar o script `ls` executável | Script apto para execução |
| `ls` | Executar `ls` após manipular `PATH` | Execução do script malicioso no lugar do `/bin/ls` |

