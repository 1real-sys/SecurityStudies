# Crawling

**Crawling** (ou *spidering*) é o processo automatizado de navegar de forma sistemática pela World Wide Web. Assim como uma aranha percorre sua teia, um crawler segue links de uma página para outra e coleta informações. Esses crawlers são bots que usam algoritmos pré-definidos para descobrir e indexar páginas, tornando-as acessíveis para mecanismos de busca, análise de dados ou reconhecimento web.

## Como os Web Crawlers Funcionam

O funcionamento básico de um crawler é simples e poderoso:

1. Começa com uma **URL semente** (a primeira página a ser visitada).
2. Faz o download da página.
3. Analisa o conteúdo e extrai os links.
4. Coloca esses links em uma fila.
5. Repete o processo de forma iterativa.

Dependendo do escopo e da configuração, o crawler pode explorar um site inteiro ou uma grande parte da web.

### Exemplo prático

Você começa na homepage com os links `link1`, `link2` e `link3`:

```text
Homepage
├── link1
├── link2
└── link3
```

Ao visitar `link1`, o crawler encontra novamente a homepage, `link2` e também `link4` e `link5`:

```text
link1 Page
├── Homepage
├── link2
├── link4
└── link5
```

Em seguida, continua seguindo os links sistematicamente, coletando todas as páginas acessíveis e suas relações.

Esse exemplo mostra como o crawling descobre informação por navegação estruturada de links, diferente de **fuzzing**, que tenta adivinhar caminhos potenciais.

## Estratégias de Crawling

Existem duas estratégias principais:

### Breadth-First Crawling (Busca em Largura)

Prioriza explorar a **largura** do site antes de aprofundar. Primeiro varre os links da página semente, depois os links dessas páginas, e assim por diante. É útil para obter uma visão ampla da estrutura e do conteúdo do site.

### Depth-First Crawling (Busca em Profundidade)

Prioriza a **profundidade**. Segue um único caminho de links até o fim antes de voltar e explorar caminhos alternativos. É útil para encontrar conteúdo específico ou alcançar áreas profundas da estrutura do site.

A escolha da estratégia depende dos objetivos do processo de crawling.

## Extração de Informações Valiosas

Crawlers podem extrair diferentes tipos de dados para reconhecimento:

- **Links internos e externos:** mapeiam a estrutura do site, revelam páginas ocultas e mostram relações com recursos externos.
- **Comentários:** podem expor detalhes sensíveis, processos internos ou pistas de vulnerabilidades.
- **Metadados:** títulos, descrições, palavras-chave, autor e datas ajudam a contextualizar conteúdo e relevância.
- **Arquivos sensíveis:** backups (`.bak`, `.old`), configurações (`web.config`, `settings.php`), logs (`error_log`, `access_log`) e arquivos com credenciais ou chaves podem estar expostos por engano.

## A Importância do Contexto

Entender o **contexto** dos dados extraídos é essencial.

Uma informação isolada (por exemplo, um comentário citando versão de software) pode parecer irrelevante. Porém, ao ser correlacionada com metadados desatualizados ou arquivos de configuração vulneráveis encontrados no crawling, pode se tornar um forte indicador de vulnerabilidade.

O valor real está em conectar os pontos e montar uma visão completa da superfície digital do alvo.

### Exemplo de correlação

Uma lista de links pode parecer comum. Mas, ao notar várias URLs apontando para `/files/`, você decide verificar manualmente e encontra *directory listing* habilitado, com backups, documentos internos e dados sensíveis.

Da mesma forma, um comentário aparentemente inocente sobre um “file server” ganha relevância quando combinado com a descoberta do diretório `/files/`, reforçando a hipótese de exposição pública de informações confidenciais.

Por isso, a análise deve ser holística: considerar relações entre os dados e suas implicações para os objetivos de reconhecimento.
