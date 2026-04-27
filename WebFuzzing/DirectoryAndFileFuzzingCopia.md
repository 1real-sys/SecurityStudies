# Fuzzing de Diretórios e Arquivos

Aplicações web frequentemente têm diretórios e arquivos que não estão diretamente linkados ou visíveis para os usuários. Esses recursos ocultos podem conter informações sensíveis, arquivos de backup, arquivos de configuração ou até versões antigas e vulneráveis da aplicação. O fuzzing de diretórios e arquivos busca revelar esses ativos ocultos, fornecendo aos atacantes possíveis pontos de entrada ou informações valiosas para exploração posterior.

## Descobrindo ativos ocultos

Aplicações web costumam guardar um verdadeiro tesouro de recursos ocultos — diretórios, arquivos e endpoints que não ficam acessíveis pela interface principal. Essas áreas escondidas podem conter informações valiosas para atacantes, incluindo:

- **Dados sensíveis:** arquivos de backup, configurações ou logs contendo credenciais de usuários e outras informações confidenciais.
- **Conteúdo desatualizado:** versões antigas de arquivos ou scripts que podem estar vulneráveis a exploits conhecidos.
- **Recursos de desenvolvimento:** ambientes de teste, sites de staging ou painéis administrativos que podem ser usados em ataques.
- **Funcionalidades ocultas:** recursos ou endpoints não documentados que podem expor vulnerabilidades inesperadas.

Descobrir esses ativos ocultos é crucial para pesquisadores de segurança e pentesters, pois oferece uma visão mais profunda da superfície de ataque da aplicação e de suas possíveis falhas.

## A importância de encontrar ativos ocultos

Encontrar esses recursos escondidos está longe de ser trivial. Cada descoberta contribui para um entendimento completo da estrutura e funcionalidade da aplicação web, algo essencial em uma avaliação de segurança séria. Essas áreas ocultas muitas vezes não têm o mesmo nível de proteção das partes públicas da aplicação, tornando-se alvos prioritários de exploração.

Mesmo que um ativo oculto não revele uma vulnerabilidade imediata, a informação obtida pode ser extremamente útil em etapas futuras do pentest — desde entender a stack tecnológica até encontrar dados sensíveis que podem sustentar novos ataques.

O fuzzing de diretórios e arquivos está entre os métodos mais eficazes para revelar esses ativos. Ele consiste em testar sistematicamente a aplicação com listas de possíveis nomes de diretórios e arquivos, analisando as respostas do servidor para identificar recursos válidos.

## Wordlists

Wordlists são a base do fuzzing de diretórios e arquivos. Elas fornecem os possíveis nomes de diretórios e arquivos que a ferramenta escolhida vai usar para testar a aplicação. Wordlists eficientes aumentam bastante as chances de encontrar ativos ocultos.

Essas listas normalmente são compiladas de várias fontes, como coleta de nomes comuns na web, análise de vazamentos públicos e extração de informações de diretórios com base em vulnerabilidades conhecidas. Depois, passam por curadoria para remover duplicatas e entradas irrelevantes, garantindo eficiência e efetividade.

As ferramentas citadas — **ffuf**, **wfuzz**, etc. — não possuem wordlists embutidas, mas foram feitas para funcionar perfeitamente com arquivos de wordlist externos. Essa flexibilidade permite usar listas prontas ou criar listas próprias para cenários específicos.

Uma das coleções de wordlists mais completas e usadas é a **SecLists**, projeto open source no GitHub:  
https://github.com/danielmiessler/SecLists

No pwnbox, especificamente, a pasta costuma estar em:

```bash
/usr/share/seclists/
```

Tudo em minúsculo. Em outras distribuições, pode aparecer como `SecLists`, igual ao repositório. Se um comando não funcionar, verifique o caminho.

A SecLists contém wordlists para:

- Nomes comuns de diretórios e arquivos
- Arquivos de backup
- Arquivos de configuração
- Scripts vulneráveis
- E muito mais

As wordlists mais usadas da SecLists para fuzzing de diretórios e arquivos web são:

- `Discovery/Web-Content/common.txt`: lista de uso geral com muitos nomes comuns de diretórios e arquivos; excelente ponto de partida.
- `Discovery/Web-Content/directory-list-2.3-medium.txt`: lista mais extensa focada em nomes de diretórios.
- `Discovery/Web-Content/raft-large-directories.txt`: grande coleção de diretórios compilada de diversas fontes.
- `Discovery/Web-Content/big.txt`: wordlist massiva com nomes de diretórios e arquivos para varreduras amplas.

## Fuzzing na prática

Agora que você entende o conceito de wordlists, vamos ao processo de fuzzing com **ffuf**, uma ferramenta poderosa e flexível para revelar diretórios e arquivos ocultos em aplicações web.

Para acompanhar, inicie o sistema alvo na seção de perguntas ao final da página e substitua `IP:PORT` pelo endereço da sua instância.

## ffuf

Usaremos o ffuf nesta tarefa. Em termos gerais, ele funciona assim:

1. **Wordlist:** você fornece uma lista com possíveis nomes de diretórios/arquivos.
2. **URL com FUZZ:** você monta uma URL contendo a palavra-chave `FUZZ` como placeholder.
3. **Requisições:** o ffuf percorre a wordlist, substitui `FUZZ` por cada item e envia requisições HTTP.
4. **Análise de resposta:** ele analisa as respostas (status code, tamanho do conteúdo etc.) e filtra os resultados com base nos critérios definidos.

Exemplo de URL para fuzzing de diretórios:

```text
http://localhost/FUZZ
```

O ffuf trocará `FUZZ` por palavras como `admin`, `backup`, `uploads` etc. e fará requisições para `http://localhost/admin`, `http://localhost/backup` e assim por diante.

## Fuzzing de diretórios

O primeiro passo é fazer fuzzing de diretórios para descobrir pastas ocultas no servidor web.

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://IP:PORT/FUZZ
```

Exemplo de saída relevante:

```text
w2ksvrus [Status: 301, Size: 0, Words: 1, Lines: 1]
```

- `-w` (**wordlist**): caminho da lista usada.
- `-u` (**URL**): URL base com o placeholder `FUZZ`.

A saída acima mostra que o ffuf encontrou um diretório chamado `w2ksvrus`, indicado pelo status **301 (Moved Permanently)**. Isso pode ser um ponto de entrada para investigação posterior.

## Fuzzing de arquivos

Enquanto o fuzzing de diretórios busca pastas, o fuzzing de arquivos vai além e tenta encontrar arquivos específicos dentro desses diretórios (ou na raiz da aplicação).

Extensões comuns:

- `.php`: arquivos com código PHP.
- `.html`: estrutura e conteúdo de páginas web.
- `.txt`: texto simples, muitas vezes com logs ou informações básicas.
- `.bak`: backups de versões anteriores.
- `.js`: código JavaScript para interatividade e comportamento dinâmico.

Ao testar essas extensões com uma wordlist de nomes comuns, você aumenta a chance de encontrar arquivos expostos ou mal configurados, o que pode levar a vazamento de informação e outras falhas.

Por exemplo: se o site usa PHP, encontrar `config.php.bak` pode expor credenciais de banco de dados ou chaves de API. Da mesma forma, scripts antigos como `test.php` podem conter vulnerabilidades exploráveis.

Use o ffuf para procurar arquivos ocultos com extensões específicas:

```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://IP:PORT/w2ksvrus/FUZZ -e .php,.html,.txt,.bak,.js -v
```

Exemplo de saída:

```text
http://IP:PORT/w2ksvrus/dblclk.html
http://IP:PORT/w2ksvrus/index.html
```

Isso indica dois arquivos encontrados dentro de `/w2ksvrus`:

- `dblclk.html`: arquivo com 111 bytes, 2 palavras e 2 linhas; pode exigir análise manual para entender sua função.
- `index.html`: arquivo com 112 bytes, 6 palavras e 2 linhas; provavelmente a página padrão do diretório.
