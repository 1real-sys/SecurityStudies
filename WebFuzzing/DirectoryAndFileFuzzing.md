# Fuzzing de Diretórios e Arquivos

Aplicações web frequentemente possuem diretórios e arquivos que não estão linkados nem visíveis para usuários. Esses recursos ocultos podem conter informações sensíveis, backups, arquivos de configuração ou versões antigas e vulneráveis da aplicação. O objetivo do fuzzing de diretórios e arquivos é descobrir esses ativos ocultos, que podem servir como ponto de entrada ou fonte de informação para exploração posterior.

## Descobrindo ativos ocultos

Essas áreas escondidas podem incluir:

- **Dados sensíveis:** backups, configurações ou logs com credenciais e outras informações confidenciais.
- **Conteúdo desatualizado:** versões antigas de arquivos/scripts vulneráveis a exploits conhecidos.
- **Recursos de desenvolvimento:** ambientes de teste, staging ou painéis administrativos.
- **Funcionalidades ocultas:** endpoints e recursos não documentados.

Encontrar esses ativos é essencial em testes de segurança, pois amplia a visão da superfície de ataque da aplicação.

## Por que isso importa

Cada descoberta ajuda a montar um mapa mais completo da estrutura e do funcionamento da aplicação. Em muitos casos, áreas ocultas têm controles de segurança mais fracos que componentes públicos, tornando-se alvos mais fáceis.

Mesmo quando um ativo oculto não revela uma falha imediata, ele pode fornecer informações valiosas para as próximas etapas do pentest (por exemplo, stack tecnológica, padrões de nomes e dados sensíveis).

## Wordlists

Wordlists são a base do fuzzing. Elas reúnem nomes potenciais de diretórios e arquivos que serão testados pela ferramenta.

Essas listas costumam ser construídas a partir de múltiplas fontes, como nomes comuns coletados na web, vazamentos públicos e dados de vulnerabilidades conhecidas, passando por curadoria para remover duplicados e ruído.

Ferramentas como **ffuf** e **wfuzz** não trazem wordlists próprias por padrão, mas funcionam com listas externas.

Uma das coleções mais usadas é a **SecLists**:  
https://github.com/danielmiessler/SecLists

No pwnbox, geralmente o caminho é:

```bash
/usr/share/seclists/
```

Dependendo da distribuição, o nome da pasta pode variar para `SecLists`. Se um comando falhar, valide o caminho.

A SecLists inclui listas para:

- Nomes comuns de diretórios e arquivos
- Backups
- Arquivos de configuração
- Scripts vulneráveis

Wordlists comuns para esse cenário:

- `Discovery/Web-Content/common.txt`
- `Discovery/Web-Content/directory-list-2.3-medium.txt`
- `Discovery/Web-Content/raft-large-directories.txt`
- `Discovery/Web-Content/big.txt`

## Fuzzing na prática com ffuf

Substitua `IP:PORT` pelo alvo do seu laboratório.

### Como o ffuf funciona

1. Você fornece uma wordlist.
2. Define uma URL com a palavra-chave `FUZZ`.
3. O ffuf substitui `FUZZ` por cada entrada da lista e envia requisições HTTP.
4. Ele analisa as respostas (status code, tamanho, etc.) e mostra resultados válidos.

Exemplo de URL:

```text
http://localhost/FUZZ
```

### Fuzzing de diretórios

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://IP:PORT/FUZZ
```

Exemplo de resultado relevante:

```text
w2ksvrus [Status: 301]
```

- `-w`: caminho da wordlist
- `-u`: URL alvo com o placeholder `FUZZ`

Nesse caso, o diretório `w2ksvrus` foi identificado (status `301`), indicando um possível ponto para investigação.

### Fuzzing de arquivos

Depois de identificar diretórios, o próximo passo é buscar arquivos dentro deles (ou na raiz), incluindo extensões comuns:

- `.php`
- `.html`
- `.txt`
- `.bak`
- `.js`

Exemplo:

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://IP:PORT/w2ksvrus/FUZZ -e .php,.html,.txt,.bak,.js -v
```

Saída com arquivos encontrados:

```text
http://IP:PORT/w2ksvrus/dblclk.html
http://IP:PORT/w2ksvrus/index.html
```

- `dblclk.html`: arquivo pequeno que pode valer análise manual.
- `index.html`: provavelmente a página padrão do diretório.
