# Fuzzing Recursivo

Até aqui, o foco foi fuzzing de diretórios no nível da raiz web e arquivos dentro de uma única pasta. Porém, alvos reais podem ter estruturas profundas com múltiplos níveis. Fazer isso manualmente é demorado; o fuzzing recursivo resolve esse problema.

## Como o fuzzing recursivo funciona

É um processo automatizado em 3 etapas:

1. **Fuzzing inicial:** começa na raiz (`/`) usando uma wordlist de possíveis nomes.
2. **Descoberta e expansão:** ao encontrar um diretório válido, a ferramenta cria uma nova fila para fuzzing dentro dele.
3. **Profundidade iterativa:** repete o processo para cada diretório descoberto até atingir o limite de profundidade ou não encontrar novos caminhos.

Pense em uma árvore: a raiz web é o tronco, diretórios descobertos são galhos e o fuzzing percorre cada galho até os “nós finais” (arquivos) ou até o limite definido.

## Por que usar

- **Eficiência:** automatiza descoberta de diretórios aninhados.
- **Cobertura:** reduz o risco de perder ativos ocultos.
- **Menos trabalho manual:** não precisa lançar cada etapa na mão.
- **Escalabilidade:** funciona melhor em aplicações grandes.

## Fuzzing recursivo com ffuf

Substitua `IP:PORT` pelo seu alvo. Exemplo de comando:

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -ic -v -u http://IP:PORT/FUZZ -e .html -recursion
```

Parâmetros importantes:

- `-recursion`: ativa o fuzzing recursivo em diretórios encontrados.
- `-ic`: ignora linhas comentadas (`#`) na wordlist.
- `-e .html`: testa também essa extensão.

Exemplo de descoberta:

```text
/level1  ->  /level1/
/level1/level2  ->  /level1/level2/
/level1/level3  ->  /level1/level3/
```

Com isso, o ffuf cria novos jobs automaticamente para cada diretório válido e segue explorando níveis mais profundos.

No cenário demonstrado, o processo encontrou arquivos `index.html` em diferentes níveis e, ao aprofundar a análise, revelou a flag:

```text
HTB{r3curs1v3_fuzz1ng_w1ns}
```

## Use com responsabilidade

Fuzzing recursivo pode gerar alta carga no servidor. Para controlar isso:

- `-recursion-depth`: limita a profundidade máxima.
- `-rate`: limita requisições por segundo.
- `-timeout`: define timeout por requisição.

Exemplo com limites:

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -ic -u http://IP:PORT/FUZZ -e .html -recursion -recursion-depth 2 -rate 500
```

**Não excluir:** para fuzzing de diretórios, pode ser interessante usar:

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://IP:PORT/recursive_fuzz/level1/FUZZ -t 300
```

Para fuzzing de arquivos, pode ser interessante usar:

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://IP:PORT/recursive_fuzz/finalDirectory/FUZZ -t 300 -e .html,.txt,.bak,.js -v
```
