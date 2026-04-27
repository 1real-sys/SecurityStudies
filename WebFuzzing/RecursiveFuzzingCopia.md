# Fuzzing Recursivo

Até agora, focamos em fuzzing de diretórios diretamente sob a raiz web e em arquivos dentro de um único diretório. Mas e se o alvo tiver uma estrutura complexa com vários diretórios aninhados? Fazer fuzzing manualmente em cada nível seria cansativo e demorado. É aí que o fuzzing recursivo se torna útil.

## Como o fuzzing recursivo funciona

O fuzzing recursivo é uma forma automatizada de explorar a estrutura de diretórios de uma aplicação web em profundidade. É um processo básico de 3 etapas:

1. **Fuzzing inicial**
   - O processo começa no diretório de topo, normalmente a raiz web (`/`).
   - O fuzzer envia requisições com base na wordlist fornecida, contendo nomes potenciais de diretórios e arquivos.
   - O fuzzer analisa as respostas do servidor, procurando resultados válidos (por exemplo, `HTTP 200 OK`) que indiquem a existência de um diretório.

2. **Descoberta e expansão de diretórios**
   - Quando um diretório válido é encontrado, o fuzzer não apenas registra esse resultado. Ele cria um novo ramo para esse diretório, basicamente adicionando seu nome à URL base.
   - Exemplo: se o diretório `admin` for encontrado na raiz, um novo ramo como `http://localhost/admin/` é criado.
   - Esse novo ramo vira o ponto inicial de um novo processo de fuzzing. O fuzzer percorre novamente a wordlist, acrescentando cada entrada à URL do ramo (por exemplo, `http://localhost/admin/FUZZ`).

3. **Profundidade iterativa**
   - O processo se repete para cada diretório descoberto, criando novos ramos e expandindo o escopo para níveis mais profundos.
   - Isso continua até atingir o limite de profundidade definido (por exemplo, no máximo 3 níveis) ou até não haver mais diretórios válidos.

Imagine uma árvore: a raiz web é o tronco, cada diretório descoberto é um ramo. O fuzzing recursivo explora cada ramo sistematicamente, avançando até as folhas (arquivos) ou até um ponto de parada predeterminado.

## Por que usar fuzzing recursivo?

Em aplicações web complexas, fuzzing recursivo é uma necessidade prática:

- **Eficiência:** automatizar a descoberta de diretórios aninhados economiza muito tempo em comparação com exploração manual.
- **Cobertura:** explora sistematicamente cada ramo da estrutura, reduzindo o risco de perder ativos ocultos.
- **Menos esforço manual:** não é necessário informar cada novo diretório manualmente; a ferramenta faz isso.
- **Escalabilidade:** é especialmente valioso em aplicações grandes, onde a exploração manual é inviável.

Em resumo, fuzzing recursivo é sobre trabalhar de forma mais inteligente: você investiga a aplicação com mais eficiência e profundidade, revelando vulnerabilidades que podem estar escondidas.

## Fuzzing recursivo com ffuf

Para acompanhar, inicie o sistema alvo na seção de perguntas ao final da página e substitua `IP:PORT` pelo endereço da sua instância. Usaremos a wordlist:

```text
/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
```

Exemplo com `ffuf`:

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -ic -v -u http://IP:PORT/FUZZ -e .html -recursion
```

Saída de exemplo (resumo):

```text
[Status: 301] http://IP:PORT/level1 -> /level1/
[INFO] Adding a new job to the queue: http://IP:PORT/level1/FUZZ

[Status: 200] http://IP:PORT/level1/index.html
[Status: 301] http://IP:PORT/level1/level2 -> /level1/level2/
[Status: 301] http://IP:PORT/level1/level3 -> /level1/level3/

[Status: 200] http://IP:PORT/level1/level2/index.html
[Status: 200] http://IP:PORT/level1/level3/index.html
```

Observe o uso da flag `-recursion`. Ela instrui o ffuf a fazer fuzzing recursivamente em qualquer diretório descoberto. Exemplo: se encontrar `admin`, ele inicia automaticamente um novo processo em `http://localhost/admin/FUZZ`.

Quando a wordlist tem comentários (linhas começando com `#`), a opção `-ic` é útil: o ffuf ignora essas linhas, evitando tratá-las como entradas válidas.

O fuzzing começa em `http://IP:PORT/FUZZ`. Primeiro, o ffuf identifica `level1` com resposta `301 (Moved Permanently)`, indicando redirecionamento e disparando uma nova busca dentro desse diretório.

Ao explorar `level1` recursivamente, ele encontra `level2` e `level3`, adiciona ambos na fila e amplia a profundidade da busca. Também encontra um `index.html` em `level1`.

Depois, o fuzzer processa a fila e encontra `index.html` em `level2` e `level3`. O arquivo de `level3` se destaca por ter tamanho maior.

Análise adicional mostra que esse arquivo contém a flag:

```text
HTB{r3curs1v3_fuzz1ng_w1ns}
```

Isso confirma uma exploração bem-sucedida de uma estrutura de diretórios aninhada.

## Seja responsável

Embora poderoso, o fuzzing recursivo pode consumir muitos recursos, principalmente em aplicações grandes. Excesso de requisições pode sobrecarregar o servidor, causar degradação de desempenho ou acionar mecanismos de defesa.

Para mitigar riscos, o ffuf oferece opções de ajuste fino:

- `-recursion-depth`: define profundidade máxima da exploração recursiva.
  - Exemplo: `-recursion-depth 2` limita a dois níveis (diretório inicial + subdiretórios imediatos).
- `-rate`: controla a taxa de requisições por segundo.
- `-timeout`: define timeout por requisição, evitando travamentos em alvos sem resposta.

Exemplo:

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
