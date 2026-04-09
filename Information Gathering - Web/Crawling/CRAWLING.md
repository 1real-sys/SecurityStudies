# Crawling

Crawling (ou *spidering*) é a navegação automatizada e sistemática da web. Um crawler segue links de página em página para descobrir, mapear e indexar conteúdo para busca, análise de dados e reconhecimento web.

## Como funciona

1. Começa por uma URL semente.
2. Coleta a página e extrai os links.
3. Adiciona os links em fila.
4. Repete o processo iterativamente.

Isso permite explorar desde um único site até grandes porções da web.

## Exemplo simples

```text
Homepage
├── link1
├── link2
└── link3
```

Ao visitar `link1`, novos links podem surgir:

```text
link1 Page
├── Homepage
├── link2
├── link4
└── link5
```

O crawler segue esses caminhos e coleta páginas e relacionamentos. Diferente de fuzzing, aqui a descoberta ocorre por links reais já existentes.

## Estratégias de crawling

- **Breadth-First (largura):** visita primeiro os links do nível atual, ideal para visão geral da estrutura.
- **Depth-First (profundidade):** segue um caminho até o fim antes de voltar, útil para alcançar conteúdo mais profundo.

## Informações extraídas

- **Links internos e externos:** mapeamento da estrutura e dependências.
- **Comentários:** possíveis pistas de processos internos e falhas.
- **Metadados:** contexto de conteúdo (título, descrição, autor, datas).
- **Arquivos sensíveis:** backups, configs, logs e possíveis credenciais expostas.

## Importância do contexto

O valor do crawling está na correlação dos achados. Um item isolado pode parecer inofensivo, mas, combinado com outros sinais (como diretórios expostos, metadados desatualizados e comentários), pode indicar vulnerabilidades relevantes.
